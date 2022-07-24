'''
Creates a DynamoDb table for the main data store.
'''
import logging
import boto3


def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.create_table(
        # TODO Change this to 'movie_reviews_PROD' when we want to create prod table
        TableName='movie_reviews',
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
            # {
            #     'AttributeName': 'rating',
            #     'AttributeType': 'N'
            # }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    table = create_table()
    logging.info("Table status:", table.table_status)
