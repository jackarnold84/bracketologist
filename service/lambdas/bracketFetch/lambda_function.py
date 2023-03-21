from utils import response
from db import GroupDB

group_db = GroupDB()


def lambda_handler(event, context):

    # read query
    params = event['queryStringParameters']
    group_id = params['groupID'] if 'groupID' in params else ''

    if not group_id:
        return response({'error': 'invalid query parameters'}, status=400)

    # read group
    group = group_db.read_group(group_id)
    if not group:
        return response({'error': 'group %s not found' % group_id}, status=400)

    if 'analysis' not in group or not group['analysis']:
        return response({'error': 'no analysis for group %s' % group_id}, status=400)

    return response({
        'group': group
    })
