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


# bracketology utils

rounds = ['R64', 'R32', 'S16', 'E8', 'F4', 'NCG']

round_matchups = {
    'R64': [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
    ],
    'R32': [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
    'S16': [49, 50, 51, 52, 53, 54, 55, 56],
    'E8': [57, 58, 59, 60],
    'F4': [61, 62],
    'NCG': [63]
}

matchup_sequence = {
    1: {'matchup': 33, 'slot': 'team1'},
    2: {'matchup': 33, 'slot': 'team2'},
    3: {'matchup': 34, 'slot': 'team1'},
    4: {'matchup': 34, 'slot': 'team2'},
    5: {'matchup': 35, 'slot': 'team1'},
    6: {'matchup': 35, 'slot': 'team2'},
    7: {'matchup': 36, 'slot': 'team1'},
    8: {'matchup': 36, 'slot': 'team2'},
    9: {'matchup': 37, 'slot': 'team1'},
    10: {'matchup': 37, 'slot': 'team2'},
    11: {'matchup': 38, 'slot': 'team1'},
    12: {'matchup': 38, 'slot': 'team2'},
    13: {'matchup': 39, 'slot': 'team1'},
    14: {'matchup': 39, 'slot': 'team2'},
    15: {'matchup': 40, 'slot': 'team1'},
    16: {'matchup': 40, 'slot': 'team2'},
    17: {'matchup': 41, 'slot': 'team1'},
    18: {'matchup': 41, 'slot': 'team2'},
    19: {'matchup': 42, 'slot': 'team1'},
    20: {'matchup': 42, 'slot': 'team2'},
    21: {'matchup': 43, 'slot': 'team1'},
    22: {'matchup': 43, 'slot': 'team2'},
    23: {'matchup': 44, 'slot': 'team1'},
    24: {'matchup': 44, 'slot': 'team2'},
    25: {'matchup': 45, 'slot': 'team1'},
    26: {'matchup': 45, 'slot': 'team2'},
    27: {'matchup': 46, 'slot': 'team1'},
    28: {'matchup': 46, 'slot': 'team2'},
    29: {'matchup': 47, 'slot': 'team1'},
    30: {'matchup': 47, 'slot': 'team2'},
    31: {'matchup': 48, 'slot': 'team1'},
    32: {'matchup': 48, 'slot': 'team2'},
    33: {'matchup': 49, 'slot': 'team1'},
    34: {'matchup': 49, 'slot': 'team2'},
    35: {'matchup': 50, 'slot': 'team1'},
    36: {'matchup': 50, 'slot': 'team2'},
    37: {'matchup': 51, 'slot': 'team1'},
    38: {'matchup': 51, 'slot': 'team2'},
    39: {'matchup': 52, 'slot': 'team1'},
    40: {'matchup': 52, 'slot': 'team2'},
    41: {'matchup': 53, 'slot': 'team1'},
    42: {'matchup': 53, 'slot': 'team2'},
    43: {'matchup': 54, 'slot': 'team1'},
    44: {'matchup': 54, 'slot': 'team2'},
    45: {'matchup': 55, 'slot': 'team1'},
    46: {'matchup': 55, 'slot': 'team2'},
    47: {'matchup': 56, 'slot': 'team1'},
    48: {'matchup': 56, 'slot': 'team2'},
    49: {'matchup': 57, 'slot': 'team1'},
    50: {'matchup': 57, 'slot': 'team2'},
    51: {'matchup': 58, 'slot': 'team1'},
    52: {'matchup': 58, 'slot': 'team2'},
    53: {'matchup': 59, 'slot': 'team1'},
    54: {'matchup': 59, 'slot': 'team2'},
    55: {'matchup': 60, 'slot': 'team1'},
    56: {'matchup': 60, 'slot': 'team2'},
    57: {'matchup': 61, 'slot': 'team1'},
    58: {'matchup': 61, 'slot': 'team2'},
    59: {'matchup': 62, 'slot': 'team1'},
    60: {'matchup': 62, 'slot': 'team2'},
    61: {'matchup': 63, 'slot': 'team1'},
    62: {'matchup': 63, 'slot': 'team2'}
}

matchup_score_value = {
    1: 10, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10,
    9: 10, 10: 10, 11: 10, 12: 10, 13: 10, 14: 10, 15: 10, 16: 10,
    17: 10, 18: 10, 19: 10, 20: 10, 21: 10, 22: 10, 23: 10, 24: 10,
    25: 10, 26: 10, 27: 10, 28: 10, 29: 10, 30: 10, 31: 10, 32: 10,
    33: 20, 34: 20, 35: 20, 36: 20, 37: 20, 38: 20, 39: 20, 40: 20,
    41: 20, 42: 20, 43: 20, 44: 20, 45: 20, 46: 20, 47: 20, 48: 20,
    49: 40, 50: 40, 51: 40, 52: 40, 53: 40, 54: 40, 55: 40, 56: 40,
    57: 80, 58: 80, 59: 80, 60: 80, 61: 160, 62: 160, 63: 320
}

matchup_max_seeds = {
    1: 1, 2: 8, 3: 5, 4: 4, 5: 6, 6: 3, 7: 7, 8: 2,
    9: 1, 10: 8, 11: 5, 12: 4, 13: 6, 14: 3, 15: 7, 16: 2,
    17: 1, 18: 8, 19: 5, 20: 4, 21: 6, 22: 3, 23: 7, 24: 2,
    25: 1, 26: 8, 27: 5, 28: 4, 29: 6, 30: 3, 31: 7, 32: 2,
    33: 1, 34: 4, 35: 3, 36: 2, 37: 1, 38: 4, 39: 3, 40: 2,
    41: 1, 42: 4, 43: 3, 44: 2, 45: 1, 46: 4, 47: 3, 48: 2,
    49: 1, 50: 2, 51: 1, 52: 2, 53: 1, 54: 2, 55: 1, 56: 2,
    57: 1, 58: 1, 59: 1, 60: 1, 61: 1, 62: 1, 63: 1
}


