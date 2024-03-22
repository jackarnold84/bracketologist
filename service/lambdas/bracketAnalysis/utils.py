import json


def response(body={}, status=200, cors=True):

    headers = {
        'Access-Control-Allow-Headers': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    } if cors else {}

    return {
        'statusCode': status,
        'headers': headers,
        'body': json.dumps(body)
    }


def parseInt(x):
    try:
        return int(x)
    except:
        return None
    

def pct_limit(x):
    if x > 99.999:
        return 100
    elif x < 0.001:
        return 0
    else:
        return min(max(x, 0.1), 99.9)


# bracketology utils

matchup_sequence = {
    # r64 -> r32
    0: 32, 1: 32, 2: 33, 3: 33, 4: 34, 5: 34, 6: 35, 7: 35,
    8: 36, 9: 36, 10: 37, 11: 37, 12: 38, 13: 38, 14: 39, 15: 39,
    16: 40, 17: 40, 18: 41, 19: 41, 20: 42, 21: 42, 22: 43, 23: 43,
    24: 44, 25: 44, 26: 45, 27: 45, 28: 46, 29: 46, 30: 47, 31: 47,

     # r32 -> s16
    32: 48, 33: 48, 34: 49, 35: 49, 36: 50, 37: 50, 38: 51, 39: 51,
    40: 52, 41: 52, 42: 53, 43: 53, 44: 54, 45: 54, 46: 55, 47: 55,

    # s16 -> e8
    48: 56, 49: 56, 50: 57, 51: 57, 52: 58, 53: 58, 54: 59, 55: 59,

    # e8 -> f4
    56: 60, 57: 60, 58: 61, 59: 61,
    
    # f4 -> ncg
    60: 62, 61: 62,

    # ngc -> champ
    62: 63,
}

rounds = ['R64', 'R32', 'S16', 'E8', 'F4', 'NCG']

round_to_wins = {
    'R64': 0,
    'R32': 1,
    'S16': 2,
    'E8': 3,
    'F4': 4,
    'NCG': 5,
    'CHAMP': 6,
}

wins_to_round = {
    0: 'R64',
    1: 'R32',
    2: 'S16',
    3: 'E8',
    4: 'F4',
    5: 'NCG',
    6: 'CHAMP',
}

wins_to_points = {
    0: 0,
    1: 10,
    2: 30,
    3: 70,
    4: 150,
    5: 310,
    6: 630,
}

seed_chalk_wins = {
    1: 4,
    2: 3,
    3: 2,
    4: 2,
    5: 1,
    6: 1,
    7: 1,
    8: 1,
}


def get_score(n_wins, round_cap='NCG'):
    return wins_to_points[
        min(n_wins, round_to_wins[round_cap] + 1)
    ]


def get_initial_matchups(b):
    return [
        [b[0][1], b[0][16]],
        [b[0][8], b[0][9]],
        [b[0][5], b[0][12]],
        [b[0][4], b[0][13]],
        [b[0][6], b[0][11]],
        [b[0][3], b[0][14]],
        [b[0][7], b[0][10]],
        [b[0][2], b[0][15]],

        [b[1][1], b[1][16]],
        [b[1][8], b[1][9]],
        [b[1][5], b[1][12]],
        [b[1][4], b[1][13]],
        [b[1][6], b[1][11]],
        [b[1][3], b[1][14]],
        [b[1][7], b[1][10]],
        [b[1][2], b[1][15]],

        [b[2][1], b[2][16]],
        [b[2][8], b[2][9]],
        [b[2][5], b[2][12]],
        [b[2][4], b[2][13]],
        [b[2][6], b[2][11]],
        [b[2][3], b[2][14]],
        [b[2][7], b[2][10]],
        [b[2][2], b[2][15]],

        [b[3][1], b[3][16]],
        [b[3][8], b[3][9]],
        [b[3][5], b[3][12]],
        [b[3][4], b[3][13]],
        [b[3][6], b[3][11]],
        [b[3][3], b[3][14]],
        [b[3][7], b[3][10]],
        [b[3][2], b[3][15]],
    ]


def get_team_list(bracket):
    return [
        *list(bracket[0].values()),
        *list(bracket[1].values()),
        *list(bracket[2].values()),
        *list(bracket[3].values()),
    ]
