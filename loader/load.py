import sys
import time

from boto3.session import Session
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from tqdm import tqdm

from . import config, credentials, db, utils

service = Service(executable_path=credentials.path_to_msedgedriver)
options = Options()
options.add_argument('--headless')
options.add_argument('log-level=3')
driver = webdriver.Edge(service=service, options=options)


def fetch_group_info(group_id, year, type, group_name):
    type_tag = '-women' if type == 'womens' else ''
    url = f'https://fantasy.espn.com/games/tournament-challenge-bracket{type_tag}-{year}/group?id={group_id}'

    driver.get(url)
    time.sleep(8)
    soup = BeautifulSoup(driver.page_source, features='lxml')

    bracket_ids = []
    bracket_names = []
    users = []
    for x in soup.select('.EntryLink-nameContainer'):
        username = x.select_one('.EntryLink-memberName').text
        entry_link = x.select_one('.AnchorLink')
        bracket_name = entry_link.text
        bracket_id = entry_link['href'].rsplit('?id=', 1)[1]
        bracket_ids.append(bracket_id)
        bracket_names.append(utils.clean_text(bracket_name))
        users.append(utils.clean_text(username))

    return {
        'group_id': group_id,
        'group_name': group_name,
        'url': url,
        'year': str(year),
        'type': type,
        'brackets': bracket_ids,
        'bracket_names': bracket_names,
        'users': users,
        'analysis': {},
    }


def get_display_name(username, bracket_name):
    if username in config.username_alias:
        return config.username_alias[username]
    elif 'espn' in username.lower():
        if 'espn' in bracket_name.lower():
            return 'espn-%s' % (username[-4:])
        else:
            return bracket_name[:12].strip()
    else:
        return username[:12].strip()


def fetch_bracket(bracket_id, year, type, username, bracket_name):
    type_tag = '-women' if type == 'womens' else ''
    url = f'https://fantasy.espn.com/games/tournament-challenge-bracket{type_tag}-{year}/bracket?id={bracket_id}'

    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    assert len(soup.select('.BracketPropositionHeader-pickName')) == 63

    picks = {}
    for x in soup.select('.BracketPropositionHeader-pickName'):
        t = x.text
        if t not in picks:
            picks[t] = 1
        else:
            picks[t] += 1

    picks = {
        k: v for k, v in sorted(
            picks.items(),
            key=lambda x: x[1],
            reverse=True
        )
    }
    champ = list(picks.keys())[0]

    return {
        'id': str(bracket_id),
        'username': username,
        'bracket_name': bracket_name,
        'display_name': get_display_name(username, bracket_name),
        'url': url,
        'year': str(year),
        'type': type,
        'champion': champ,
        'selections': picks,
    }


def fetch_group_brackets(group_info, year, type):
    brackets = {}
    for i in tqdm(range(len(group_info['brackets']))):
        bracket_id = group_info['brackets'][i]
        bracket_name = group_info['bracket_names'][i]
        username = group_info['users'][i]
        b = fetch_bracket(bracket_id, year, type, username, bracket_name)
        if b:
            brackets[bracket_id] = b
        else:
            group_info['brackets'].pop(i)
        time.sleep(4)
    return brackets


if __name__ == '__main__':
    # check args
    args = sys.argv
    group_to_load = sys.argv[1] if len(sys.argv) > 1 else None

    if not group_to_load:
        print('group not spcified')
        print('must be one of:', list(config.groups.keys()))
        exit(1)
    elif group_to_load not in config.groups:
        print('invalid group name')
        print('must be one of:', list(config.groups.keys()))
        exit(1)

    # connect to aws sdk
    session = Session(
        aws_access_key_id=credentials.aws_access_key,
        aws_secret_access_key=credentials.aws_secret_access_key,
        region_name=credentials.aws_region
    )
    aws_dynamodb = session.resource('dynamodb')
    group_db = db.GroupDB(aws_dynamodb)
    bracket_db = db.BracketDB(aws_dynamodb)
    print('--> aws sdk connected')

    # fetch group, brackets
    group_id = config.groups[group_to_load]['group_id']
    year = config.groups[group_to_load]['year']
    group_type = config.groups[group_to_load]['type']
    group_name = config.groups[group_to_load]['name']

    print('--> loading %s' % group_to_load)
    group = fetch_group_info(group_id, year, group_type, group_name)

    brackets = fetch_group_brackets(group, year, group_type)

    # insert into db
    group_db.insert_group(group)
    for b in brackets.values():
        bracket_db.insert_bracket(b)
    print('--> saved to db')
