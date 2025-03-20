# class interfaces for dynamodb tables

import os
from decimal import Decimal

import boto3
import simplejson as json

GROUP_TABLE_NAME = os.environ.get('GROUP_TABLE', 'BracketologistGroups')
DB_WRITE = os.environ.get('DB_WRITE', 'mock')


def format_item(item):
    json_str = json.dumps(item, use_decimal=True)
    return json.loads(json_str, parse_float=Decimal)


class GroupDB:
    def __init__(self):
        dynamodb_resource = boto3.resource('dynamodb')
        self.table = dynamodb_resource.Table(GROUP_TABLE_NAME)

    def read_key(self, key_id):
        data = self.table.get_item(
            Key={'group_id': str(key_id)}
        )
        return data['Item'] if 'Item' in data else None

    def insert_key(self, item):
        if DB_WRITE != 'prod':
            print(f"Mock write: {item}")
            return
        self.table.put_item(
            Item=format_item(item)
        )
