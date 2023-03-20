# class interfaces for dynamodb tables

import json
from decimal import Decimal

def format_item(item):
    return json.loads(json.dumps(item), parse_float=Decimal)


class GroupDB:
    def __init__(self, dynamodb_resource):
        self.table = dynamodb_resource.Table('bracketologistGroups')

    def read_group(self, group_id):
        data = self.table.get_item(
            Key={'group_id': str(group_id)}
        )
        assert 'Item' in data, 'item not found: %s' % group_id
        return data['Item']

    def insert_group(self, group):
        self.table.put_item(
            Item=format_item(group)
        )


class BracketDB:
    def __init__(self, dynamodb_resource):
        self.table = dynamodb_resource.Table('bracketologistBrackets')

    def read_bracket(self, id):
        data = self.table.get_item(
            Key={'id': str(id)}
        )
        assert 'Item' in data, 'item not found: %s' % id
        bracket = data['Item']
        bracket['selections'] = {
            int(k): v for k, v in bracket['selections'].items()
        }
        bracket['selections'] = {
            k: v for k, v in sorted(bracket['selections'].items())
        }
        return data['Item']

    def insert_bracket(self, bracket):
        self.table.put_item(
            Item=format_item(bracket)
        )
