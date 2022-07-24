'''
This is an in memory datastore, which is mostly used for debugging.
'''
from collections import defaultdict
from typing import List, Set

from app.model.review import Review


class InMemoryDatastore:
    def __init__(self, ):
        self.database = defaultdict(list)
        self.keys = set()

    def upload(self, review: Review) -> None:
        self.database[review.author].append(Review(review.author, review.movie, review.rating))
        self.keys.add(review.author)

    def batch_upload(self, reviews: List[Review]) -> None:
        for review in reviews:
            self.upload(review)

    def get(self, author: str) -> List[Review]:
        return self.database[author]

    def get_keys(self) -> Set[str]:
        return self.keys
