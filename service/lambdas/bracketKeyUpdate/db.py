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

    def read_key(self, key_id):
        data = self.table.get_item(
            Key={'group_id': str(key_id)}
        )
        return data['Item'] if 'Item' in data else None

    def insert_key(self, item):
        self.table.put_item(
            Item=format_item(item)
        )
