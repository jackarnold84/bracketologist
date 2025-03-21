# class interfaces for dynamodb tables

import json
import os
import time
from decimal import Decimal

import boto3

GROUP_TABLE_NAME = os.environ.get('GROUP_TABLE', 'BracketologistGroups')
DB_WRITE = os.environ.get('DB_WRITE', 'mock')

CACHE_TTL = 180  # 3 minutes
cache = {}


def format_item(item):
    return json.loads(json.dumps(item), parse_float=Decimal)


class GroupDB:
    def __init__(self):
        dynamodb_resource = boto3.resource('dynamodb')
        self.table = dynamodb_resource.Table(GROUP_TABLE_NAME)

    def read_group(self, group_id):
        current_time = time.time()
        if group_id in cache:
            cached_data, timestamp = cache[group_id]
            if current_time - timestamp < CACHE_TTL:
                return cached_data

        data = self.table.get_item(
            Key={'group_id': str(group_id)}
        )
        if 'Item' in data:
            cache[group_id] = (data['Item'], current_time)
            return data['Item']
        return None

    def insert_group(self, group):
        if DB_WRITE != 'prod':
            print(f"Mock write: {group}")
            return
        self.table.put_item(
            Item=format_item(group)
        )
