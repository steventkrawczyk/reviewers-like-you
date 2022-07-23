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

    def batch_upload(self, reviews: List[Tuple[str, str, str]]) -> None:
        with localcontext() as ctx:
            ctx.prec = 3
            with self.database.batch_writer() as batch:
                for review in reviews:
                    reviewData = {'author': review[0], 'movie': review[1],
                                'rating': ctx.create_decimal(review[2])}
                    batch.put_item(Item=reviewData)
