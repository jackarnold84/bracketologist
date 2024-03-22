import time
from random import random

import numpy as np
from config import CURRENT_YEAR, mens_bracket
from utils import (get_initial_matchups, get_score, get_team_list,
                   matchup_sequence, pct_limit, rounds, seed_chalk_wins,
                   wins_to_round)


def fetch_bracket_key(group_db, year=CURRENT_YEAR, type='mens'):
    item = group_db.read_group('key-mens')
    team_list = get_team_list(mens_bracket)
    
    key = {t: item['key'].get(t, 0) for t in team_list}
    eliminated = item['eliminated']
    return key, set(eliminated)


def apply_alt_display_names(brackets):
    display_names = [b['display_name'] for b in brackets.values()]
    for b in brackets:
        dname = brackets[b]['display_name']
        bname = brackets[b]['bracket_name']
        if display_names.count(dname) > 1:
            brackets[b]['display_name'] = bname[:12].strip()


def get_bracket_score(picks, key, eliminated, round='NCG'):
    score = 0
    max_score = 0
    for t in key:
        curr_pts = get_score(min(key[t], picks.get(t, 0)), round)
        total_pts = get_score(picks.get(t, 0), round)
        score += curr_pts
        if t in eliminated:
            max_score += curr_pts
        else:
            max_score += total_pts

    return score, max_score


def get_bracket_upsets(picks, key, eliminated, teams):
    upsets_chosen = 0
    upsets_correct = 0
    upsets_played = 0

    for t in picks:
        chalk_wins = seed_chalk_wins.get(teams[t]['seed'], 0)
        chosen = picks[t] - chalk_wins
        if chosen > 0:
            upsets_chosen += chosen
            upsets_correct += max(min(picks[t], key[t]) - chalk_wins, 0)
            if t in eliminated:
                upsets_played += chosen
            else:
                upsets_played += max(key[t] - chalk_wins, 0)

    return upsets_chosen, upsets_correct, upsets_played


def get_bracket_selections(picks):
    categories = ['CHAMP', 'NCG', 'F4', 'E8', 'S16', 'R32']
    selections = {c: [] for c in categories}
    for t in picks:
        selections[wins_to_round[picks[t]]].append(t)

    return selections


def sim_game(t1, t2, teams):
    t1_seed = teams[t1]['stat_seed'] or teams[t1]['seed']
    t2_seed = teams[t2]['stat_seed'] or teams[t2]['seed']
    pr = 0.5 + 0.028*(t2_seed - t1_seed)
    return t1 if random() < pr else t2


def sim_bracket(key, teams):
    sim_key = {t: 0 for t in teams}
    matchups = get_initial_matchups(mens_bracket) + [[] for _ in range(32)]
    keyr = {**key}

    for i, m in enumerate(matchups[:-1]):
        next = matchup_sequence[i]
        if keyr[m[0]] > 0:
            winner = m[0]
        elif keyr[m[1]] > 0:
            winner = m[1]
        else:
            winner = sim_game(m[0], m[1], teams)

        keyr[winner] -= 1
        sim_key[winner] += 1
        matchups[next].append(winner)

    sim_champ = matchups[63][0]
    return sim_key, sim_champ


def group_simulation(brackets, key, teams, eliminated, N=10000):
    sim_data = {
        b: {r: {'scores': [], 'ranks': []} for r in rounds}
        for b in brackets
    }
    team_champ = {t: 0 for t in teams}
    for _ in range(N):
        sim_key, sim_champ = sim_bracket(key, teams)
        team_champ[sim_champ] += 1
        scores = {
            b: {
                r: get_bracket_score(brackets[b]['selections'], sim_key, set(), r)[0]
                for r in rounds
            } for b in brackets
        }
        ranks = {
            r: sorted(
                scores,
                key=lambda x: (scores[x][r], scores[x]['NCG'], x),
                reverse=True
            )
            for r in rounds
        }
        for b in brackets:
            for r in rounds:
                sim_data[b][r]['scores'].append(scores[b][r])
                sim_data[b][r]['ranks'].append(ranks[r].index(b) + 1)

    team_champ = {t: team_champ[t] / N for t in team_champ}
    return sim_data, team_champ


def get_final_four(picks):
    selections = get_bracket_selections(picks)
    return [*selections['CHAMP'], *selections['NCG'], *selections['F4']]


def get_team_round_status(t, key):
    return wins_to_round[key[t]]


# MAIN ANALYSIS FUNCTION

def group_analysis(brackets, sim_results, team_champ, key, eliminated, teams):

    # current scores
    current_scores = [
        {
            'id': b['id'],
            'name': b['display_name'],
            'pts': get_bracket_score(b['selections'], key, eliminated)[0],
            'max': get_bracket_score(b['selections'], key, eliminated)[1],
            'ff': get_final_four(b['selections']),
        } for b in brackets.values()
    ]
    current_scores = sorted(
        current_scores,
        key=lambda x: (x['pts'], x['max']),
        reverse=True
    )

    # projection board (by round)
    projection_board = {
        r: [
            {
                'id': brackets[b]['id'],
                'name': brackets[b]['display_name'],
                'exp': round(np.mean(sim_results[b][r]['scores'])),
                'max': get_bracket_score(brackets[b]['selections'], key, eliminated, r)[1],
                'win': pct_limit(np.mean([x == 1 for x in sim_results[b][r]['ranks']]) * 100),
            } for b in brackets
        ] for r in rounds
    }
    for r in projection_board:
        projection_board[r] = sorted(
            projection_board[r],
            key=lambda x: (x['win'], x['exp'], x['max']),
            reverse=True
        )

    # projected rank
    rankings = [
        {
            'id': brackets[b]['id'],
            'name': brackets[b]['display_name'],
            'avg': round(np.mean(sim_results[b]['NCG']['ranks']), 3),
            'worst': max(sim_results[b]['NCG']['ranks']),
            'best': min(sim_results[b]['NCG']['ranks']),
        } for b in brackets
    ]
    rankings = sorted(
        rankings,
        key=lambda x: (x['avg'], x['best']),
    )

    # upsets chosen
    upsets_chosen = [
        {
            'id': b['id'],
            'name': b['display_name'],
            'chosen': get_bracket_upsets(b['selections'], key, eliminated, teams)[0],
            'n_correct': get_bracket_upsets(b['selections'], key, eliminated, teams)[1],
            'correct': '%d/%d' % (
                get_bracket_upsets(b['selections'], key, eliminated, teams)[1],
                get_bracket_upsets(b['selections'], key, eliminated, teams)[2],
            ),
        } for b in brackets.values()
    ]
    upsets_chosen = sorted(
        upsets_chosen,
        key=lambda x: (x['chosen'], x['n_correct']),
        reverse=True
    )

    # team info
    team_info = {
        t: {
            **teams[t],
            'eliminated': t in eliminated,
            'display_name': teams[t]['name'] if len(teams[t]['name']) < 11 else t,
            'display_seed': '%s (%d)' % (
                teams[t]['name'] if len(teams[t]['name']) < 11 else t,
                teams[t]['seed'],
            ),
            'round': get_team_round_status(t, key),
        } for t in teams
    }

    # most popular teams
    team_popularity = [
        {
            'abbrev': t,
            'team': team_info[t]['display_name'],
            'seed': team_info[t]['seed'],
            'avg': round(
                np.mean(
                    [b['selections'].get(t, 0) for b in brackets.values()],
                ),
                3,
            ),
            'win': pct_limit(round(team_champ[t] * 100, 3)),
        } for t in teams
    ]
    team_popularity = sorted(
        team_popularity,
        key=lambda x: (x['avg'], -x['seed']),
        reverse=True
    )

    # bracket selections
    bracket_selections = {
        b['id']: get_bracket_selections(b['selections'])
        for b in brackets.values()
    }

    # return analysis
    timestamp = round(time.time())
    return {
        'timestamp': timestamp,
        'current_scores': current_scores,
        'projection_board': projection_board,
        'rankings': rankings,
        'upsets_chosen': upsets_chosen,
        'team_info': team_info,
        'team_popularity': team_popularity,
        'bracket_selections': bracket_selections,
    }
