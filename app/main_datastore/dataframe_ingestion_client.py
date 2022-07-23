'''
This client is used to upload pandas dataframes to our database. It
expects that rows are structured as (author, movie, rating) where
author and movie are strings and rating is a float from 0 to 1.
'''
from pandas import DataFrame, Series

from app.main_datastore.main_datastore_proxy import MainDatastoreProxy


class DataframeIngestionClient:
    def __init__(self, database: MainDatastoreProxy):
        self.database = database

    def _upload_row(self, row: Series) -> None:
        self.database.upload(row['author'], row['movie'], row['rating'])

    def upload(self, input_data: DataFrame) -> None:
        # TODO take advantage of batch upload once main data proxy uses dynamo batch processing
        input_data.apply(self._upload_row, axis=1)
