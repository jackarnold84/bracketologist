# class interfaces for dynamodb tables

import json
from decimal import Decimal


def format_item(item):
    return json.loads(json.dumps(item), parse_float=Decimal)


class GroupDB:
    def __init__(self, dynamodb_resource):
        self.table = dynamodb_resource.Table('bracketologistGroups')

    def insert_group(self, group):
        self.table.put_item(
            Item=format_item(group)
        )


class BracketDB:
    def __init__(self, dynamodb_resource):
        self.table = dynamodb_resource.Table('bracketologistBrackets')

    def insert_bracket(self, bracket):
        self.table.put_item(
            Item=format_item(bracket)
        )
