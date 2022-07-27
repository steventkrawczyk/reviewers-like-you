from pandas import DataFrame

from app.ingestion.datastore.main_datastore_proxy import MainDatastoreProxy
from app.model.review import Review


class DataframeIngestionClient:
    '''
    This client is used to upload pandas dataframes to our database.
    '''

    def __init__(self, database: MainDatastoreProxy):
        self.database = database

    def upload(self, input_data: DataFrame) -> None:
        batch = [Review(row['author'], row['movie'], row['rating'])
                 for _, row in input_data.iterrows()]
        self.database.batch_upload(batch)
