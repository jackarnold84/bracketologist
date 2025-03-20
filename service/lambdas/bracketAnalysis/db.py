# class interfaces for dynamodb tables

import os
from decimal import Decimal

import boto3
import simplejson as json

GROUP_TABLE_NAME = os.environ.get('GROUP_TABLE', 'BracketologistGroups')
BRACKET_TABLE_NAME = os.environ.get('BRACKET_TABLE', 'BracketologistBrackets')
DB_WRITE = os.environ.get('DB_WRITE', 'mock')


def format_item(item):
    json_str = json.dumps(item, use_decimal=True)
    return json.loads(json_str, parse_float=Decimal)


class GroupDB:
    def __init__(self):
        dynamodb_resource = boto3.resource('dynamodb')
        self.table = dynamodb_resource.Table(GROUP_TABLE_NAME)

    def read_group(self, group_id):
        data = self.table.get_item(
            Key={'group_id': str(group_id)}
        )
        return data['Item'] if 'Item' in data else None

    def insert_group(self, group):
        if DB_WRITE != 'prod':
            print(f"Mock write: {group}")
            return
        self.table.put_item(
            Item=format_item(group)
        )


class BracketDB:
    def __init__(self):
        dynamodb_resource = boto3.resource('dynamodb')
        self.table = dynamodb_resource.Table(BRACKET_TABLE_NAME)

    def read_bracket(self, id):
        data = self.table.get_item(
            Key={'id': str(id)}
        )
        if 'Item' not in data:
            return None
        return data['Item']
