import boto3
import logging

from app.ingestion.datastore.dynamodb_datastore import DynamoDbDatastore
from app.ingestion.datastore.in_memory_datastore import InMemoryDatastore
from app.ingestion.main_datastore_proxy import MainDatastoreProxy


class MainDatastoreFactory:
    '''
    This is the client for the primary storage for raw input to the system,
    ingested from web scrapers, manual uploads, and user input.
    '''

    def __init__(self, endpoint_url: str = "http://dynamodb-local:8000", table_name: str = "movie_reviews", in_memory: bool = False):
        if not in_memory:
            self.endpoint_url = endpoint_url
            self.table_name = table_name
        self.in_memory = in_memory

    def build(self) -> MainDatastoreProxy:
        if self.in_memory:
            logging.info("Using in memory mode for main datastore.")
            return InMemoryDatastore()
        else:
            logging.info("Connecting to dynamodb as main datastore.")
            self.dynamodb = boto3.resource(
                'dynamodb', endpoint_url=self.endpoint_url)
            return DynamoDbDatastore(self.dynamodb, self.table_name)
