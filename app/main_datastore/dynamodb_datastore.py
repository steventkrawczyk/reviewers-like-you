'''
This is the client for the primary storage for raw input to the system,
ingested from web scrapers, manual uploads, and user input.

NOTE: The current implementation uses a simple in memory database, a
dictionary. At scale, we will need to replace this with a big data
key-value store that supports appending to list values.

TODO: We need our schema to protect against duplicate reviews. Today
it does not.
'''
from decimal import localcontext
import boto3
from boto3.dynamodb.conditions import Key
from typing import List, Set, Tuple


class DynamoDbDatastore:
    def __init__(self, ):
        self.dynamodb = boto3.resource(
            'dynamodb', endpoint_url="http://localhost:8000")
        self.database = self.dynamodb.Table("movie_reviews")

    def upload(self, author: str, movie: str, rating: str) -> None:
        with localcontext() as ctx:
            ctx.prec = 3
            reviewData = {'author': author, 'movie': movie,
                          'rating': ctx.create_decimal(rating)}
            self.database.put_item(Item=reviewData)

    def get(self, author: str) -> List[Tuple[str, str]]:
        queryResponse = self.database.query(
            KeyConditionExpression=Key('author').eq(author))
        return [(item['movie'], item['rating']) for item in queryResponse['Items']]

    def get_keys(self) -> Set[str]:
        scanResponse = self.database.scan(ProjectionExpression='author')
        return [item['author'] for item in scanResponse['Items']]

    # TODO Use dynamodb batch upload
    def batch_upload(self, reviews: List[Tuple[str, str, str]]) -> None:
        for review in reviews:
            self.upload(review)
