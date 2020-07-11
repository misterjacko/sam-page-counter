import json
import os
import boto3

from app import UpdateItem
from unittest import TestCase, mock

client = boto3.client(
    "dynamodb", 
    endpoint_url="http://localhost:8000",
    aws_access_key_id="ACCKEY111",
    aws_secret_access_key="SECKEY999")

TEST_TABLE_NAME = "Fake_table"
TEST_SITE_URL = "fake_site.com"

class DynamoTest(TestCase):
    def test_fail(self):
        self.assertEqual("2", "1")
    
    def setUp(self):
        # Create table
        client.create_table(
            TableName=TEST_TABLE_NAME,
            KeySchema=[
                {
                    "AttributeName": "site_url",
                    "KeyType": "HASH"
                }
            ],
            AttributeDefinitions=[
                {
                    "AttributeName": "site_url",
                    "AttributeType": "S"
                }
            ],
            BillingMode="PAY_PER_REQUEST"
        )

    def tearDown(self):
        client.delete_table(
            TableName=TEST_TABLE_NAME
        )

    @mock.patch('app.TABLE_NAME', TEST_TABLE_NAME)
    @mock.patch('app.SITE_URL', TEST_SITE_URL)
    def test_update(self):
        test_obj = UpdateItem(client)
        response = test_obj.update_count()
        body_response = json.loads(response["body"])
        # assert count was incremented by one
        self.assertEqual(200, response['statusCode'])
        # assert incremented by 1
        self.assertEqual("1", body_response["Visit_Count"])

    @mock.patch('app.TABLE_NAME', TEST_TABLE_NAME)
    @mock.patch('app.SITE_URL', TEST_SITE_URL)
    def test_update_when_already_exists(self):
        test_obj = UpdateItem(client)
        response = test_obj.update_count()
        body_response = json.loads(response["body"])
        # assert count was incremented by one
        self.assertEqual(200, response['statusCode'])
        # assert incremented by 1
        self.assertEqual("1", body_response["Visit_Count"])

        response2 = test_obj.update_count()
        body_response2 = json.loads(response2["body"])
        self.assertEqual("2", body_response2["Visit_Count"])

# response1 = get_update_visit_counter({}, {})
# response2 = get_update_visit_counter({}, {})

# def test_response():
#     count1 = int(json.loads(response1["body"])["Visit_Count"])
#     count2 = int(json.loads(response2["body"])["Visit_Count"])
#     assert count2 - count1 == 1
