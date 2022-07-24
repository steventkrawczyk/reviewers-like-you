'''
This is the client for the primary storage for raw input to the system,
ingested from web scrapers, manual uploads, and user input.
'''
import logging
from typing import List, Set

from app.ingestion.dynamodb_datastore import DynamoDbDatastore
from app.ingestion.in_memory_datastore import InMemoryDatastore
from app.model.review import Review


class MainDatastoreProxy:
    def __init__(self, endpoint_url: str = "http://localhost:8000", 
                 table_name: str = "movie_reviews", in_memory: bool = False):
        if in_memory:
            logging.info("Using in memory mode for main datastore.")
            self.datastore = InMemoryDatastore()
        else:
            logging.info("Connecting to dynamodb as main datastore.")
            self.datastore = DynamoDbDatastore(endpoint_url, table_name)

    def upload(self, review: Review) -> None:
        self.datastore.upload(review)

    def batch_upload(self, reviews: List[Review]) -> None:
        self.datastore.batch_upload(reviews)

    def get(self, author: str) -> List[Review]:
        return self.datastore.get(author)

    def get_keys(self) -> Set[str]:
        return self.datastore.get_keys()
