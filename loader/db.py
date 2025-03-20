# class interfaces for dynamodb tables

import json
import os
from decimal import Decimal

GROUP_TABLE_NAME = os.environ.get('GROUP_TABLE', 'BracketologistGroups')
BRACKET_TABLE_NAME = os.environ.get('BRACKET_TABLE', 'BracketologistBrackets')


def format_item(item):
    return json.loads(json.dumps(item), parse_float=Decimal)


class GroupDB:
    def __init__(self, dynamodb_resource):
        self.table = dynamodb_resource.Table(GROUP_TABLE_NAME)

    def insert_group(self, group):
        self.table.put_item(
            Item=format_item(group)
        )


class BracketDB:
    def __init__(self, dynamodb_resource):
        self.table = dynamodb_resource.Table(BRACKET_TABLE_NAME)

    def insert_bracket(self, bracket):
        self.table.put_item(
            Item=format_item(bracket)
        )
