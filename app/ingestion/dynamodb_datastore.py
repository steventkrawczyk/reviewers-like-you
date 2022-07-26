from boto3.dynamodb.conditions import Key
from boto3.resources.base import ServiceResource
from typing import List, Set
from app.ingestion.main_datastore_proxy import MainDatastoreProxy

from app.model.review import Review


class DynamoDbDatastore(MainDatastoreProxy):
    '''
    This is our client for DynamoDb.
    '''

    def __init__(self, dynamodb: ServiceResource, table_name: str):
        self.database = dynamodb.Table(table_name)

    def _get_table(self):
        return

    def upload(self, review: Review) -> None:
        reviewData = review.to_dict()
        self.database.put_item(Item=reviewData)

    def batch_upload(self, reviews: List[Review]) -> None:
        with self.database.batch_writer() as batch:
            for review in reviews:
                reviewData = review.to_dict()
                batch.put_item(Item=reviewData)

    def get(self, author: str) -> List[Review]:
        queryResponse = self.database.query(
            KeyConditionExpression=Key('author').eq(author))
        return [Review.from_dict(item) for item in queryResponse['Items']]

    def get_keys(self) -> Set[str]:
        scanResponse = self.database.scan(ProjectionExpression='author')
        return set([item['author'] for item in scanResponse['Items']])

    # TODO work on paging
    # def scan(self) -> List[Review]:
    #     scanResponse = self.database.scan()
    #     return [Review.from_dict(item) for item in scanResponse['Items']]
