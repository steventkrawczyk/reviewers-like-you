'''
This class offers the scraper an API for submitting data to the main
data store, either directly or by saving the data off to a CSV for
upload at a later time.
'''
import os
from typing import List, Tuple
from pandas import DataFrame

from app.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.ingestion.dataframe_ingestion_client import DataframeIngestionClient
from app.model.review import Review


class DataSubmissionClient:
    def __init__(self, filepath: str = "data/scraped_data.csv"):
        if filepath != "":
            self.filepath = filepath
        else:
            self.database = MainDatastoreProxy()
            self.client = DataframeIngestionClient(self.database)

    def submit_dataframe(self, data: DataFrame) -> None:
        if self.filepath != "":
            data.to_csv(self.filepath, mode='a+')
        else:
            self.client.upload(data)

    # Preferred method for ingestion service performance.
    def submit_batch(self, reviews: List[Tuple[str, str, str]]) -> None:
        self.database.batch_upload(reviews)

    def submit(self, author: str, movie: str, rating: str) -> None:
        if self.filepath != "":
            # If the file does not exist, create it and add a header
            if not os.path.isfile(self.filepath):
                with open(self.filepath, 'a+') as f:
                    f.write(["author", "movie", "rating"])
            with open(self.filepath, 'a') as f:
                f.write([author, movie, rating])
        else:
            self.database.upload(Review(author, movie, rating))
