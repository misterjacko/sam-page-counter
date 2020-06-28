import boto3
import json

client = boto3.client('dynamodb')

def get_update_visit_counter(site_url):
    response = client.update_item(
        TableName='jakobondrey_visitor_count',
        Key={
            'site_url': {
                'S': 'jakobondrey.com'
            },
        },
        ReturnValues='UPDATED_NEW',
        UpdateExpression='SET count = count + 1',
    )
    print(response)