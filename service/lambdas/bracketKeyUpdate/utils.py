import json
from decimal import Decimal


def response(body={}, status=200, cors=True):

    headers = {
        'Access-Control-Allow-Headers': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    } if cors else {}

    return {
        'statusCode': status,
        'headers': headers,
        'body': json.dumps(body, default=decimal_dumper)
    }


def decimal_dumper(obj):
    if isinstance(obj, Decimal):
        if float(obj) == int(obj):
            return int(obj)
        else:
            return float(obj)
    raise TypeError
