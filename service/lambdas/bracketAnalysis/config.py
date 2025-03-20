CURRENT_YEAR = '2025'

mens_bracket = [
    {
        1:  'AUB',
        16: 'ALST',
        8:  'LOU',
        9:  'CREI',
        5:  'MICH',
        12: 'UCSD',
        4:  'TA&M',
        13: 'YALE',
        6:  'MISS',
        11: 'UNC',
        3:  'ISU',
        14: 'LIP',
        7:  'MARQ',
        10: 'UNM',
        2:  'MSU',
        15: 'BRY',
    },
    {
        1:  'FLA',
        16: 'NORF',
        8:  'CONN',
        9:  'OU',
        5:  'MEM',
        12: 'CSU',
        4:  'MD',
        13: 'GCU',
        6:  'MIZ',
        11: 'DRKE',
        3:  'TTU',
        14: 'UNCW',
        7:  'KU',
        10: 'ARK',
        2:  'SJU',
        15: 'OMA',
    },
    {
        1:  'DUKE',
        16: 'MSM',
        8:  'MSST',
        9:  'BAY',
        5:  'ORE',
        12: 'LIB',
        4:  'ARIZ',
        13: 'AKR',
        6:  'BYU',
        11: 'VCU',
        3:  'WIS',
        14: 'MONT',
        7:  'SMC',
        10: 'VAN',
        2:  'ALA',
        15: 'RMU',
    },
    {
        1:  'HOU',
        16: 'SIUE',
        8:  'GONZ',
        9:  'UGA',
        5:  'CLEM',
        12: 'MCN',
        4:  'PUR',
        13: 'HPU',
        6:  'ILL',
        11: 'XAV',
        3:  'UK',
        14: 'TROY',
        7:  'UCLA',
        10: 'USU',
        2:  'TENN',
        15: 'WOF',
    }
]

mens_team_metadata = {
    'AUB': {'abbrev': 'AUB', 'name': 'Auburn', 'seed': 1, 'stat_seed': 1.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2.png'},
    'FLA': {'abbrev': 'FLA', 'name': 'Florida', 'seed': 1, 'stat_seed': 0.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/57.png'},
    'DUKE': {'abbrev': 'DUKE', 'name': 'Duke', 'seed': 1, 'stat_seed': 0.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/150.png'},
    'HOU': {'abbrev': 'HOU', 'name': 'Houston', 'seed': 1, 'stat_seed': 1.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/248.png'},
    'MSU': {'abbrev': 'MSU', 'name': 'Michigan St', 'seed': 2, 'stat_seed': 2.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/127.png'},
    'ALA': {'abbrev': 'ALA', 'name': 'Alabama', 'seed': 2, 'stat_seed': 1.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/333.png'},
    'SJU': {'abbrev': 'SJU', 'name': "St. John's", 'seed': 2, 'stat_seed': 2.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2599.png'},
    'TENN': {'abbrev': 'TENN', 'name': 'Tennessee', 'seed': 2, 'stat_seed': 1.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2633.png'},
    'ISU': {'abbrev': 'ISU', 'name': 'Iowa State', 'seed': 3, 'stat_seed': 2.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/66.png'},
    'UK': {'abbrev': 'UK', 'name': 'Kentucky', 'seed': 3, 'stat_seed': 4.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/96.png'},
    'WIS': {'abbrev': 'WIS', 'name': 'Wisconsin', 'seed': 3, 'stat_seed': 3.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/275.png'},
    'TTU': {'abbrev': 'TTU', 'name': 'Texas Tech', 'seed': 3, 'stat_seed': 2.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2641.png'},
    'ARIZ': {'abbrev': 'ARIZ', 'name': 'Arizona', 'seed': 4, 'stat_seed': 3.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/12.png'},
    'MD': {'abbrev': 'MD', 'name': 'Maryland', 'seed': 4, 'stat_seed': 3.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/120.png'},
    'TA&M': {'abbrev': 'TA&M', 'name': 'Texas A&M', 'seed': 4, 'stat_seed': 4.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/245.png'},
    'PUR': {'abbrev': 'PUR', 'name': 'Purdue', 'seed': 4, 'stat_seed': 5.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2509.png'},
    'MICH': {'abbrev': 'MICH', 'name': 'Michigan', 'seed': 5, 'stat_seed': 6.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/130.png'},
    'CLEM': {'abbrev': 'CLEM', 'name': 'Clemson', 'seed': 5, 'stat_seed': 4.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/228.png'},
    'MEM': {'abbrev': 'MEM', 'name': 'Memphis', 'seed': 5, 'stat_seed': 9.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/235.png'},
    'ORE': {'abbrev': 'ORE', 'name': 'Oregon', 'seed': 5, 'stat_seed': 8.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2483.png'},
    'MIZ': {'abbrev': 'MIZ', 'name': 'Missouri', 'seed': 6, 'stat_seed': 5.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/142.png'},
    'MISS': {'abbrev': 'MISS', 'name': 'Ole Miss', 'seed': 6, 'stat_seed': 7.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/145.png'},
    'BYU': {'abbrev': 'BYU', 'name': 'BYU', 'seed': 6, 'stat_seed': 4.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/252.png'},
    'ILL': {'abbrev': 'ILL', 'name': 'Illinois', 'seed': 6, 'stat_seed': 5.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/356.png'},
    'UCLA': {'abbrev': 'UCLA', 'name': 'UCLA', 'seed': 7, 'stat_seed': 7.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/26.png'},
    'MARQ': {'abbrev': 'MARQ', 'name': 'Marquette', 'seed': 7, 'stat_seed': 7.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/269.png'},
    'KU': {'abbrev': 'KU', 'name': 'Kansas', 'seed': 7, 'stat_seed': 5.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2305.png'},
    'SMC': {'abbrev': 'SMC', 'name': "Saint Mary's", 'seed': 7, 'stat_seed': 6.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2608.png'},
    'CONN': {'abbrev': 'CONN', 'name': 'UConn', 'seed': 8, 'stat_seed': 6.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/41.png'},
    'LOU': {'abbrev': 'LOU', 'name': 'Louisville', 'seed': 8, 'stat_seed': 6.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/97.png'},
    'MSST': {'abbrev': 'MSST', 'name': 'Mississippi St', 'seed': 8, 'stat_seed': 8.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/344.png'},
    'GONZ': {'abbrev': 'GONZ', 'name': 'Gonzaga', 'seed': 8, 'stat_seed': 3.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2250.png'},
    'UGA': {'abbrev': 'UGA', 'name': 'Georgia', 'seed': 9, 'stat_seed': 9.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/61.png'},
    'CREI': {'abbrev': 'CREI', 'name': 'Creighton', 'seed': 9, 'stat_seed': 7.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/156.png'},
    'OU': {'abbrev': 'OU', 'name': 'Oklahoma', 'seed': 9, 'stat_seed': 10.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/201.png'},
    'BAY': {'abbrev': 'BAY', 'name': 'Baylor', 'seed': 9, 'stat_seed': 8.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/239.png'},
    'ARK': {'abbrev': 'ARK', 'name': 'Arkansas', 'seed': 10, 'stat_seed': 10.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/8.png'},
    'UNM': {'abbrev': 'UNM', 'name': 'New Mexico', 'seed': 10, 'stat_seed': 11.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/167.png'},
    'VAN': {'abbrev': 'VAN', 'name': 'Vanderbilt', 'seed': 10, 'stat_seed': 10.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/238.png'},
    'USU': {'abbrev': 'USU', 'name': 'Utah State', 'seed': 10, 'stat_seed': 11.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/328.png'},
    'UNC': {'abbrev': 'UNC', 'name': 'North Carolina', 'seed': 11, 'stat_seed': 8.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/153.png'},
    'DRKE': {'abbrev': 'DRKE', 'name': 'Drake', 'seed': 11, 'stat_seed': 11.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2181.png'},
    'VCU': {'abbrev': 'VCU', 'name': 'VCU', 'seed': 11, 'stat_seed': 9.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2670.png'},
    'XAV': {'abbrev': 'XAV', 'name': 'Xavier', 'seed': 11, 'stat_seed': 9.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2752.png'},
    'UCSD': {'abbrev': 'UCSD', 'name': 'UC San Diego', 'seed': 12, 'stat_seed': 12.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/28.png'},
    'CSU': {'abbrev': 'CSU', 'name': 'Colorado St', 'seed': 12, 'stat_seed': 11.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/36.png'},
    'LIB': {'abbrev': 'LIB', 'name': 'Liberty', 'seed': 12, 'stat_seed': 12.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2335.png'},
    'MCN': {'abbrev': 'MCN', 'name': 'McNeese', 'seed': 12, 'stat_seed': 13.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2377.png'},
    'YALE': {'abbrev': 'YALE', 'name': 'Yale', 'seed': 13, 'stat_seed': 13.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/43.png'},
    'AKR': {'abbrev': 'AKR', 'name': 'Akron', 'seed': 13, 'stat_seed': 12.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2006.png'},
    'GCU': {'abbrev': 'GCU', 'name': 'Grand Canyon', 'seed': 13, 'stat_seed': 12.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2253.png'},
    'HPU': {'abbrev': 'HPU', 'name': 'High Point', 'seed': 13, 'stat_seed': 13.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2272.png'},
    'MONT': {'abbrev': 'MONT', 'name': 'Montana', 'seed': 14, 'stat_seed': 14.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/149.png'},
    'LIP': {'abbrev': 'LIP', 'name': 'Lipscomb', 'seed': 14, 'stat_seed': 13.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/288.png'},
    'UNCW': {'abbrev': 'UNCW', 'name': 'UNCW', 'seed': 14, 'stat_seed': 14.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/350.png'},
    'TROY': {'abbrev': 'TROY', 'name': 'Troy', 'seed': 14, 'stat_seed': 14.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2653.png'},
    'OMA': {'abbrev': 'OMA', 'name': 'Omaha', 'seed': 15, 'stat_seed': 15.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2437.png'},
    'RMU': {'abbrev': 'RMU', 'name': 'Robert Morris', 'seed': 15, 'stat_seed': 15.0, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2523.png'},
    'WOF': {'abbrev': 'WOF', 'name': 'Wofford', 'seed': 15, 'stat_seed': 14.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2747.png'},
    'BRY': {'abbrev': 'BRY', 'name': 'Bryant', 'seed': 15, 'stat_seed': 15.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2803.png'},
    'MSM': {'abbrev': 'MSM', 'name': 'MSM', 'seed': 16, 'stat_seed': 16.25, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/116.png'},
    'ALST': {'abbrev': 'ALST', 'name': 'Alabama St', 'seed': 16, 'stat_seed': 16.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2011.png'},
    'NORF': {'abbrev': 'NORF', 'name': 'Norfolk State', 'seed': 16, 'stat_seed': 15.75, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2450.png'},
    'SIUE': {'abbrev': 'SIUE', 'name': 'SIUE', 'seed': 16, 'stat_seed': 16.5, 'img': 'https://a.espncdn.com/i/teamlogos/ncaa/500/2565.png'},
}
