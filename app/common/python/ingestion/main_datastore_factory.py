import logging

from app.common.python.ingestion.in_memory_datastore import InMemoryDatastore
from app.common.python.ingestion.main_datastore_proxy import MainDatastoreProxy


class MainDatastoreFactory:
    '''
    This is the client for the primary storage for raw input to the system,
    ingested from web scrapers, manual uploads, and user input.
    '''

    def __init__(self):
        pass

    def build(self) -> MainDatastoreProxy:
        logging.debug("Using in memory mode for main datastore.")
        return InMemoryDatastore()
