from db import GroupDB
from utils import response

group_db = GroupDB()


def lambda_handler(event, context):

    # read request
    params = event.get('pathParameters', {})
    group_id = params.get('groupId', '')

    if not group_id:
        return response({'error': 'groupId is empty'}, status=400)

    # read group
    group = group_db.read_group(group_id)
    if not group:
        return response({'error': 'group %s not found' % group_id}, status=404)

    if 'analysis' not in group or not group['analysis']:
        return response({'error': 'no analysis for group %s' % group_id}, status=404)

    return response({
        'group': group
    })
