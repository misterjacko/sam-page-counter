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
        UpdateExpression='SET visit_count = visit_count + :val',
        ExpressionAttributeValues={
            ":val": {
                "N": "1"
            }
        }
    )
    visit_count = response["Attributes"]["visit_count"]["N"]
    return {
        "statusCode": 200,
        "body": json.dumps({"Visit_Count": visit_count})
    }
    