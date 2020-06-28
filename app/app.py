import boto3
import json

ec2Client = boto3.client('ec2')

def get_update_visit_counter(event, context):
    pop1 = "Good "
    pop2 = "Morning!"
    string1 = pop1 + pop2
    return {
        "statusCode": 200,
        "body": json.dumps({"message": string1})
    }