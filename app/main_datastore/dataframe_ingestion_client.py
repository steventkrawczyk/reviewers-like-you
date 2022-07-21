'''
This client is used to upload pandas dataframes to our database. It
expects that rows are structured as (author, movie, review) where
author and movie are strings and review is a float from 0 to 1.
'''
import pandas as pd

class DataframeIngestionClient:
    def __init__(self, database):
        self.database = database

    def _upload_row(self, row) -> None:
        self.database.upload(row['author'], row['movie'], row['review'])
    
    def upload(self, input_data: pd.DataFrame) -> None:    
        input_data.apply(self._upload_row, axis=1)
        
