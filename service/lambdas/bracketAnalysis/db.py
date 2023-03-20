# class interfaces for dynamodb tables

import boto3
import json
from decimal import Decimal

def format_item(item):
    return json.loads(json.dumps(item), parse_float=Decimal)


class GroupDB:
    def __init__(self):
        dynamodb_resource = boto3.resource('dynamodb')
        self.table = dynamodb_resource.Table('bracketologistGroups')

    def read_group(self, group_id):
        data = self.table.get_item(
            Key={'group_id': str(group_id)}
        )
        return data['Item'] if 'Item' in data else None

    def insert_group(self, group):
        self.table.put_item(
            Item=format_item(group)
        )


class BracketDB:
    def __init__(self):
        dynamodb_resource = boto3.resource('dynamodb')
        self.table = dynamodb_resource.Table('bracketologistBrackets')

    def read_bracket(self, id):
        data = self.table.get_item(
            Key={'id': str(id)}
        )
        if 'Item' not in data:
            return None
        bracket = data['Item']
        bracket['selections'] = {
            int(k): v for k, v in bracket['selections'].items()
        }
        bracket['selections'] = {
            k: v for k, v in sorted(bracket['selections'].items())
        }
        return data['Item']

    def insert_bracket(self, bracket):
        bracket['selections'] = {
            str(k): v for k, v in bracket['selections'].items()
        }
        self.table.put_item(
            Item=format_item(bracket)
        )
