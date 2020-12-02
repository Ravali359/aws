import json
import boto3
import logging

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('LOANS')
def lambda_handler(event, context):

    table.put_item(Item=event)
    return {
        'statusCode': 200,
        'body': json.dumps(event),
        "message":"Loan Applied Successfully"
    }