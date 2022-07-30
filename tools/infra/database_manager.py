import logging
import time
import boto3
from botocore.exceptions import ClientError


class DatabaseManager:
    def __init__(self, endpoint_url: str = "http://localhost:8000", region_name: str = "us-west-2"):
        self.dynamodb = boto3.client(
            'dynamodb', endpoint_url=endpoint_url, region_name=region_name)

    def _wait_on_table_activation(self, table_name):
        while True:
            response = self.dynamodb.describe_table(TableName=table_name)
            if response['Table']['TableStatus'] == 'ACTIVE':
                return response['Table']['TableStatus']

            # TODO optimize this somehow: we can tolerate long sleep times for CI, but not local dev
            time.sleep(1)

    def create_reviews_table(self, table_name: str):
        try:
            table = self.dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        'AttributeName': 'author',
                        'KeyType': 'HASH'  # Partition key
                    },
                    {
                        'AttributeName': 'movie',
                        'KeyType': 'RANGE'  # Sort key
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'author',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'movie',
                        'AttributeType': 'S'
                    }
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10
                }
            )
            return self._wait_on_table_activation(table_name)
        except ClientError as error:
            if error.response['Error']['Code'] == 'ResourceInUseException':
                logging.warning(str(error.response['Error']['Message']))
                return 'ALREADY_EXISTS'
            else:
                raise error

    def delete_table(self, table_name: str):
        self.dynamodb.delete_table(TableName=table_name)
