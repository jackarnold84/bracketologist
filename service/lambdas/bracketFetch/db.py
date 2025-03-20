# class interfaces for dynamodb tables

import json
import os
from decimal import Decimal

import boto3

GROUP_TABLE_NAME = os.environ.get('GROUP_TABLE', 'BracketologistGroups')
DB_WRITE = os.environ.get('DB_WRITE', 'mock')


def format_item(item):
    return json.loads(json.dumps(item), parse_float=Decimal)


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
