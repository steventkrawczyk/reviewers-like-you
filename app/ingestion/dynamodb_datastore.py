'''
This is our client for DynamoDb.
'''
import boto3
from boto3.dynamodb.conditions import Key
from typing import List, Set
from app.ingestion.main_datastore_proxy import MainDatastoreProxy

from app.model.review import Review


class DynamoDbDatastore(MainDatastoreProxy):
    def __init__(self, endpoint_url: str, table_name: str):
        self.dynamodb = boto3.resource(
            'dynamodb', endpoint_url=endpoint_url)
        self.database = self.dynamodb.Table(table_name)

    def upload(self, review: Review) -> None:
        reviewData = review.serialize()
        self.database.put_item(Item=reviewData)

    def batch_upload(self, reviews: List[Review]) -> None:
        with self.database.batch_writer() as batch:
            for review in reviews:
                reviewData = review.serialize()
                batch.put_item(Item=reviewData)

    def get(self, author: str) -> List[Review]:
        queryResponse = self.database.query(
            KeyConditionExpression=Key('author').eq(author))
        return [Review.deserialize(item) for item in queryResponse['Items']]

    def get_keys(self) -> Set[str]:
        scanResponse = self.database.scan(ProjectionExpression='author')
        return set([item['author'] for item in scanResponse['Items']])

    # TODO work on paging
    def scan(self) -> List[Review]:
        scanResponse = self.database.scan()
        return [Review.deserialize(item) for item in scanResponse['Items']]

