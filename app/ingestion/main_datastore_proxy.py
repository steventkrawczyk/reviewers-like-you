'''
This is the client for the primary storage for raw input to the system,
ingested from web scrapers, manual uploads, and user input.
'''
import logging
from typing import List, Set, Tuple

from app.ingestion.dynamodb_datastore import DynamoDbDatastore
from app.ingestion.in_memory_datastore import InMemoryDatastore


class MainDatastoreProxy:
    def __init__(self, endpoint_url: str = "http://localhost:8000", 
                 table_name: str = "movie_reviews", in_memory: bool = False):
        if in_memory:
            logging.info("Using in memory mode for main datastore.")
            self.datastore = InMemoryDatastore()
        else:
            logging.info("Connecting to dynamodb as main datastore.")
            self.datastore = DynamoDbDatastore(endpoint_url, table_name)

    def upload(self, author: str, movie: str, rating: str) -> None:
        self.datastore.upload(author, movie, rating)

    def batch_upload(self, reviews: List[Tuple[str, str, str]]) -> None:
        self.datastore.batch_upload(reviews)

    def get(self, author: str) -> List[Tuple[str, str]]:
        return self.datastore.get(author)

    def get_keys(self) -> Set[str]:
        return self.datastore.get_keys()
