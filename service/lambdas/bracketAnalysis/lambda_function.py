import json
import auth
from utils import response
from db import GroupDB, BracketDB
from sim import (
    fetch_bracket_key, get_eliminated_teams, group_simulation,
    group_analysis, apply_alt_display_names,
)

group_db = GroupDB()
bracket_db = BracketDB()


def lambda_handler(event, context):

    # read payload
    params = event['queryStringParameters']
    group_id = params['groupID'] if 'groupID' in params else ''
    limit = params['limit'] if 'limit' in params else None
    body = json.loads(event['body']) if 'body' in event else {}
    auth_body = body['auth'] if 'auth' in body else {}

    # auth
    authorized = auth.is_authorized(auth_body)
    if 'auth' in params and params['auth'] == 'checkAuth':
        return response({'authorized': authorized})
    elif 'auth' in params and params['auth'] == 'requestAuth':
        token = auth.request_authorization(auth_body)
        if token:
            return response({'authorized': True, 'authToken': token})
        else:
            return response({'authorized': False})
    elif not authorized:
        return response({'authorized': False}, status=401)

    if not group_id:
        return response({'error': 'invalid query parameters'}, status=400)

    # read group
    group = group_db.read_group(group_id)
    if not group:
        return response({'error': 'group %s not found' % group_id}, status=400)

    # read brackets
    brackets = {}
    for id in group['brackets']:
        b = bracket_db.read_bracket(id)
        if not b:
            return response({'error': 'bracket %s not found' % id}, status=400)
        brackets[id] = b
    apply_alt_display_names(brackets)

    # fetch bracket key
    try:
        key, teams = fetch_bracket_key()
        eliminated = get_eliminated_teams(key)
    except Exception as e:
        return response({'error': 'fetching bracket key: %s' % e}, 500)

    # determine n iterations
    n_iter = 200000 // len(brackets)
    n_iter = min(max(2000, n_iter), 10000)

    # run simulation
    try:
        sim_results = group_simulation(
            brackets, key, teams, eliminated, n_iter
        )
    except Exception as e:
        return response({'error': 'group_simulation: %s' % e}, 500)

    # get analysis
    try:
        analysis = group_analysis(
            brackets, sim_results, key, eliminated, teams
        )
    except Exception as e:
        return response({'error': 'group_analysis: %s' % e}, 500)

    # write analysis
    group['analysis'] = analysis
    try:
        group_db.insert_group(group)
    except Exception as e:
        return response({'error': 'failed group_db write: %s' % e}, 500)

    return response({'success': True})
