import json
import decimal
import boto3  

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Accounts')

def lambda_handler(event, context):
    # TODO implement

    response = table.update_item(Key={'user_name': event['user_name']},
        ExpressionAttributeNames={
            '#state':'state'
        },
        ExpressionAttributeValues={
          ':state': event['state'],
        },
        UpdateExpression='SET #state = :state', 
        ReturnValues='ALL_NEW',)

    response = {
        "statusCode": 200,
        "body": json.dumps(response['Attributes'],cls=DecimalEncoder),
        "message":"User Details"
    }

    return response