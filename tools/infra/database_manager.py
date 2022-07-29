import logging
import boto3


class DatabaseManager:
    def __init__(self, endpoint_url: str = "http://localhost:8000", region_name: str = "us-west-2"):
        self.dynamodb = boto3.client(
            'dynamodb', endpoint_url=endpoint_url, region_name=region_name)

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
            if 'TableDescription' not in table:
                raise KeyError('TableDescription')
            if 'TableStatus' not in table['TableDescription']:
                raise KeyError('TableStatus')
            return table['TableDescription']['TableStatus']
        except:
            logging.warning("Unable to create table.")
            return "ALREADY_EXISTS"

    def delete_table(self, table_name: str):
        try:
            self.dynamodb.delete_table(TableName=table_name)
        except:
            logging.warning("Unable to delete table.")
