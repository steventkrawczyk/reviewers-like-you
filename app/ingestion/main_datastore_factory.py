'''
This is the client for the primary storage for raw input to the system,
ingested from web scrapers, manual uploads, and user input.
'''
import logging

from app.ingestion.dynamodb_datastore import DynamoDbDatastore
from app.ingestion.in_memory_datastore import InMemoryDatastore
from app.ingestion.main_datastore_proxy import MainDatastoreProxy


class MainDatastoreFactory:
    def __init__(self, in_memory: bool = False):
        self.in_memory = in_memory

    def build(self, endpoint_url: str = "http://dynamodb-local:8000",
              table_name: str = "movie_reviews") -> MainDatastoreProxy:
        if self.in_memory:
            logging.info("Using in memory mode for main datastore.")
            return InMemoryDatastore()
        else:
            logging.info("Connecting to dynamodb as main datastore.")
            return DynamoDbDatastore(endpoint_url, table_name)
