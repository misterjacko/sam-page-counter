import boto3
import json

client = boto3.client('dynamodb')


def get_update_visit_counter(event, context):
    response = client.update_item(
        TableName='jakobondrey_visitor_count',
        Key={
            'site_url': {
                'S': 'jakobondrey.com'
            }
        },
        ReturnValues='UPDATED_NEW',
        UpdateExpression='ADD visit_count :val',
        ExpressionAttributeValues={
            ":val": {
                "N": "1"
            }
        }
    )
    visit_count = response["Attributes"]["visit_count"]["N"]
    return {
        "statusCode": 200,
        "headers": {'Access-Control-Allow-Origin': '*'},
        "body": json.dumps({"Visit_Count": visit_count})  # to access this in front end http call to api gateway endpoint.
    }
