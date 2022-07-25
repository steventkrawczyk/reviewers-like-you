import boto3


class DatabaseManager:
    def __init__(self, endpoint_url: str ="http://localhost:8000", region_name: str ="us-west-2"):
        self.dynamodb = boto3.client('dynamodb', endpoint_url=endpoint_url, region_name=region_name)

    def create_reviews_table(self, table_name: str):
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
        return table

    def delete_table(self, table_name: str):
        self.dynamodb.delete_table(TableName=table_name)
        