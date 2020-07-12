import boto3
import json
import os

TABLE_NAME = os.getenv("TABLE_NAME", "Fake_table")
SITE_URL = os.getenv("SITE_URL", "fake_site.com")

client = None
    
class UpdateItem(object):  
    
    def __init__(self, client):
        self.client = client

    def update_count(self):
        response = self.client.update_item(
            TableName=TABLE_NAME,
            Key={
                'site_url': {
                    'S': SITE_URL
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

def get_update_visit_counter(event, context):
    global client
    if not client:
        client = boto3.client('dynamodb')
    obj = UpdateItem(client)
    obj.update_count()
