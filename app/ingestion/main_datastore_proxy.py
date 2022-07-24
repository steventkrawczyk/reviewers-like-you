'''
This is the client for the primary storage for raw input to the system,
ingested from web scrapers, manual uploads, and user input.
'''
from typing import List, Set, Tuple

from app.ingestion.dynamodb_datastore import DynamoDbDatastore
from app.ingestion.in_memory_datastore import InMemoryDatastore


class MainDatastoreProxy:
    def __init__(self, endpoint_url: str = "http://localhost:8000", 
                 table_name: str = "movie_reviews", in_memory=False):
        if in_memory:
            self.datastore = InMemoryDatastore()
        else:
            self.datastore = DynamoDbDatastore(endpoint_url, table_name)

    def upload(self, author: str, movie: str, rating: str) -> None:
        self.datastore.upload(author, movie, rating)

    def batch_upload(self, reviews: List[Tuple[str, str, str]]) -> None:
        self.datastore.batch_upload(reviews)

    def get(self, author: str) -> List[Tuple[str, str]]:
        return self.datastore.get(author)

    def get_keys(self) -> Set[str]:
        return self.datastore.get_keys()
