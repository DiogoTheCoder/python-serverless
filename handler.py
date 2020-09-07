import json


def hello(event, context):
    try:
        return {
            "statusCode": 200,
            "body": "Hello 👋"
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps(e)
        }
