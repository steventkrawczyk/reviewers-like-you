from collections import defaultdict
from typing import List, Set, Tuple


class InMemoryDatastore:
    def __init__(self, ):
        self.database = defaultdict(list)
        self.keys = set()

    def upload(self, author: str, movie: str, rating: str) -> None:
        self.database[author].append((movie, rating))
        self.keys.add(author)

    # TODO Use dynamodb batch upload
    def batch_upload(self, reviews: List[Tuple[str, str, str]]) -> None:
        for review in reviews:
            self.upload(review)

    def get(self, author: str) -> List[Tuple[str, str]]:
        return self.database[author]

    def get_keys(self) -> Set[str]:
        return self.keys
