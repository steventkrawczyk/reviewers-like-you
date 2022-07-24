'''
This client is used to upload pandas dataframes to our database.
'''
from pandas import DataFrame

from app.ingestion.main_datastore_proxy import MainDatastoreProxy


class DataframeIngestionClient:
    def __init__(self, database: MainDatastoreProxy):
        self.database = database

    def upload(self, input_data: DataFrame) -> None:
        batch = [(row['author'], row['movie'], row['rating'])
                 for _, row in input_data.iterrows()]
        self.database.batch_upload(batch)
