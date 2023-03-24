import hashlib
import time
import os

# config
TIMESTAMP_UNIT = 'day'
TOKEN_DURATION = 3
MASTER_KEY = int(os.environ['MASTER_KEY'])
SUB_KEY = int(os.environ['SUB_KEY'])
PASSWORD = str(os.environ['PASSWORD'])
PYTHONHASHSEED = str(os.environ['PYTHONHASHSEED'])


# helper functions

def get_current_timestamp():
    if TIMESTAMP_UNIT == 'hour':
        return int(time.time() / 3600)
    elif TIMESTAMP_UNIT == 'minute':
        return int(time.time() / 60)
    elif TIMESTAMP_UNIT == 'day':
        return int(time.time() / 86400)
    else:
        return int(time.time())


def trapdoor(x, key=0):
    return abs(hash(hashlib.sha1((str(x) + str(key)).encode()).hexdigest()))


def get_token():
    ts = get_current_timestamp()
    return str(MASTER_KEY + trapdoor(ts, key=SUB_KEY))


def check_token(token):
    token = int(token)
    ts = get_current_timestamp()
    for t in range(ts - TOKEN_DURATION, ts + 1):
        if token - trapdoor(t, key=SUB_KEY) == MASTER_KEY:
            return True
    return False


# auth functions

def is_authorized(auth_body):
    return 'token' in auth_body and check_token(auth_body['token'])


def request_authorization(auth_body):
    if 'password' in auth_body:
        if auth_body['password'] == PASSWORD:
            return get_token()
    else:
        return None
