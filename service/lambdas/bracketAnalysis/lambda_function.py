import json

from config import mens_team_metadata
from db import BracketDB, GroupDB
from sim import (apply_alt_display_names, fetch_bracket_key, group_analysis,
                 group_simulation)
from utils import response

group_db = GroupDB()
bracket_db = BracketDB()


def lambda_handler(event, context):
    print('--> received event: %s' % json.dumps(event))

    group_id = event.get('groupId', '')
    iter_override = int(event.get('iter', 0))

    if not group_id:
        return response({'error': 'missing groupId in request'}, status=400)

    # read group
    group = group_db.read_group(group_id)
    if not group:
        return response({'error': 'group %s not found' % group_id}, status=404)
    year = str(group['year'])

    # read brackets
    brackets = {}
    for id in group['brackets']:
        b = bracket_db.read_bracket(id)
        if not b:
            return response({'error': 'bracket %s not found' % id}, status=500)
        brackets[id] = b
    apply_alt_display_names(brackets)

    # fetch bracket key
    key, eliminated = fetch_bracket_key(
        group_db,
        year,
        group['type'],
    )
    teams = mens_team_metadata

    # determine n iterations
    n_iter = 200000 // len(brackets)
    n_iter = min(max(2000, n_iter), 5000)
    if iter_override:
        n_iter = iter_override

    # run simulation
    sim_results, team_champ = group_simulation(brackets, key, teams, n_iter)

    # get analysis
    analysis = group_analysis(
        brackets, sim_results, team_champ, key, eliminated, teams
    )

    # write analysis
    group['analysis'] = analysis
    group_db.insert_group(group)

    return response({
        'success': True,
        'groupID': group_id,
        'groupMeta': '%s, %s, %s' % (group['group_name'], group['type'], group['year']),
    })
