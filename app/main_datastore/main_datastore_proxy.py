'''
This is the client for the primary storage for raw input to the system,
ingested from web scrapers, manual uploads, and user input.

NOTE: The current implementation uses a simple in memory database, a
dictionary. At scale, we will need to replace this with a big data
key-value store that supports appending to list values.

TODO: We need our schema to protect against duplicate reviews. Today
it does not.
'''
from collections import defaultdict
from decimal import localcontext
import boto3
from boto3.dynamodb.conditions import Key
from typing import List, Set, Tuple


class MainDatastoreProxy:
    def __init__(self, in_memory=False):
        self.in_memory = in_memory
        if self.in_memory:
            self.database = defaultdict(list)
            self.keys = set()
        else:
            self.dynamodb = boto3.resource(
                'dynamodb', endpoint_url="http://localhost:8000")
            self.database = self.dynamodb.Table("movie_reviews")

    def _upload_to_dynamodb(self, author: str, movie: str, rating: str) -> None:
        with localcontext() as ctx:
            ctx.prec = 3
            reviewData = {'author': author, 'movie': movie,
                          'rating': ctx.create_decimal(rating)}
            self.database.put_item(Item=reviewData)

    def _get_from_dynamodb(self, author: str) -> List[Tuple[str, str]]:
        queryResponse = self.database.query(
            KeyConditionExpression=Key('author').eq(author))
        return [(item['movie'], item['rating']) for item in queryResponse['Items']]

    def _get_keys_from_dynamodb(self) -> Set[str]:
        scanResponse = self.database.scan(ProjectionExpression='author')
        return [item['author'] for item in scanResponse['Items']]

    def upload(self, author: str, movie: str, rating: str) -> None:
        if self.in_memory:
            self.database[author].append((movie, rating))
        else:
            self._upload_to_dynamodb(author, movie, rating)
        self.keys.add(author)

    # TODO Use dynamodb batch upload
    def batch_upload(self, reviews: List[Tuple[str, str, str]]) -> None:
        for review in reviews:
            self.upload(review)

    def get(self, author: str) -> List[Tuple[str, str]]:
        if self.in_memory:
            return self.database[author]
        else:
            return self._get_from_dynamodb(author)

    def get_keys(self) -> Set[str]:
        if self.in_memory:
            return self.keys
        else:
            return self._get_keys_from_dynamodb()
