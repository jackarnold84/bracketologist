# fetches groups, brackets and stores in dynamoDB
# aws credentials must be defined in credentials.py

import sys
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from boto3.session import Session
from tqdm import tqdm
import credentials
import config
import db


def fetch_group_info(group_id, year='2023'):
    url = 'https://fantasy.espn.com/tournament-challenge-bracket/%s/en/group?groupID=%s' % (
        str(year), str(group_id)
    )
    service = Service(executable_path=credentials.path_to_chromedriver)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)
    time.sleep(12)
    soup = BeautifulSoup(driver.page_source, features='lxml')
    driver.quit()

    group_name = soup.select('.group-header')[0].text
    entries = soup.select('.entry')
    bracket_ids = [e['href'].rsplit('=')[-1] for e in entries]

    return {
        'group_id': group_id,
        'group_name': group_name,
        'url': url,
        'year': str(year),
        'type': 'mens',
        'brackets': bracket_ids,
        'analysis': {},
    }


def get_display_name(username, bracket_name):
    if username in config.username_alias:
        return config.username_alias[username]
    elif 'espnfan' in username.lower():
        if 'espnfan' in bracket_name.lower():
            return 'espnfan-%s' % (username[-4:])
        else:
            return bracket_name[:12].strip()
    else:
        return username[:12].strip()


def fetch_bracket(id, year='2023'):
    url = 'https://fantasy.espn.com/tournament-challenge-bracket/%s/en/entry?entryID=%s' % (
        str(year), str(id)
    )
    req = requests.get(url)
    soup = BeautifulSoup(req.content, features='lxml')

    bracket_name = soup.select('.entry-details-entryname')[0].text
    profile_link = soup.select('.profileLink')[0]
    username = profile_link.text

    m_classes = ['.m_' + str(i+1) for i in range(63)]
    if not soup.select(m_classes[0]):
        print('could not load bracket: %s, %s' % (id, bracket_name))
        return None
    matchups = [soup.select(mc)[0] for mc in m_classes]

    selections = {}
    for i, m in enumerate(matchups):
        matchup = i + 1
        loc1 = 1 if matchup >= 33 else 0
        loc2 = 3 if matchup >= 33 else 1
        advanced = m.select('.selectedToAdvance')[0].select('.abbrev')[0].text

        abbrev1 = m.select('.abbrev')[loc1].text
        selected1 = abbrev1 == advanced
        abbrev2 = m.select('.abbrev')[loc2].text
        selected2 = abbrev2 == advanced

        selections[i+1] = {
            'team1': abbrev1,
            'team2': abbrev2,
            'selected': abbrev1 if selected1 else abbrev2 if selected2 else ''
        }

    return {
        'id': str(id),
        'username': username,
        'bracket_name': bracket_name,
        'display_name': get_display_name(username, bracket_name),
        'url': url,
        'year': str(year),
        'type': 'mens',
        'champion': selections[63]['selected'],
        'selections': selections,
    }


def fetch_group_brackets(group_info):
    brackets = {}
    for id in tqdm(group_info['brackets']):
        b = fetch_bracket(id)
        if b:
            brackets[id] = b
        else:
            group_info['brackets'].pop(
                group_info['brackets'].index(id)
            )
        time.sleep(8)
    return brackets


# check args
args = sys.argv
group_to_load = sys.argv[1] if len(sys.argv) > 1 else None

if not group_to_load:
    print('group not spcified')
    exit(1)
elif group_to_load not in config.groups:
    print('invalid group name')
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

print('--> loading %s' % group_to_load)
group = fetch_group_info(group_id)
brackets = fetch_group_brackets(group)


# insert into db
group_db.insert_group(group)
for b in brackets.values():
    bracket_db.insert_bracket(b)
print('--> saved to db')
