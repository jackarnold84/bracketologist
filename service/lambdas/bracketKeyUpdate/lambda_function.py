import datetime
import json
import os
import time
import urllib.request

import boto3
from config import autoUpdateGroups, game_date_to_wins
from dateutil import tz
from db import DB_WRITE, GroupDB
from utils import response

group_db = GroupDB()
lambda_client = boto3.client('lambda')

KEY_ID = 'key-mens'
PROCESSOR_FUNCTION = os.environ.get(
    'PROCESSOR_FUNCTION', 'BracketologistProcessor',
)


def lambda_handler(event, context):
    print("--> received event: %s" % json.dumps(event))

    # get current key
    current_item = group_db.read_key(KEY_ID) or {}
    current_key = current_item.get('key', {})
    current_eliminated = current_item.get('eliminated', [])

    # fetch api
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/scoreboard"
    res_bytes = urllib.request.urlopen(url).read()
    res = json.loads(res_bytes)

    key = {**current_key}
    eliminated = set([*current_eliminated])

    for evt in res['events']:
        status = evt['status']['type']['name']
        dt = datetime.datetime.fromisoformat(evt['date'])
        dt_central = dt.replace(tzinfo=tz.gettz('UTC')).astimezone(
            tz=tz.gettz('America/Chicago'))
        date = dt_central.date()
        if date not in game_date_to_wins:
            continue

        meta = [x.get('headline', '') for x in evt['competitions'][0]['notes']]
        if not any('Basketball Championship' in x for x in meta):
            continue

        team1_data = evt['competitions'][0]['competitors'][0]
        team2_data = evt['competitions'][0]['competitors'][1]

        team1 = team1_data['team']['abbreviation']
        team2 = team2_data['team']['abbreviation']

        team1_score = int(team1_data['score'])
        team2_score = int(team2_data['score'])

        if status == 'STATUS_FINAL':
            winner = team1 if team1_score > team2_score else team2
            loser = team2 if team1_score > team2_score else team1

            key[winner] = game_date_to_wins[date] + 1
            key[loser] = game_date_to_wins[date]
            eliminated.add(loser)
        else:
            key[team1] = game_date_to_wins[date]
            key[team2] = game_date_to_wins[date]

    # check if update needed
    update_entry = (key != current_key) or \
        (set(eliminated) != set(current_eliminated))

    # sort
    key = dict(sorted(key.items(), key=lambda x: (x[1], x[0]), reverse=True))
    eliminated = sorted(
        list(eliminated),
        key=lambda x: (key[x], x),
        reverse=True,
    )

    # update db and reprocess groups
    if update_entry:
        group_db.insert_key({
            'group_id': KEY_ID,
            'key': key,
            'eliminated': eliminated,
        })
        time.sleep(1)

        for group_id in autoUpdateGroups:
            if DB_WRITE != 'prod':
                print(f'--> skip reprocess in non-prod env')

            print(f'--> reprocess group {group_id}')
            resp = lambda_client.invoke(
                FunctionName=PROCESSOR_FUNCTION,
                InvocationType='Event',
                Payload=json.dumps({
                    'groupId': group_id,
                }),
            )
            if resp.get('StatusCode') >= 300:
                print(f'--> failed to trigger reprocess for group: {group_id}')

    return response({
        'status': 'SUCCESS',
        'updated': update_entry,
        'key': key,
        'eliminated': eliminated,
    })
