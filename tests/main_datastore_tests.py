import pandas as pd
from pathlib import Path
import sys 
import unittest

sys.path.append("..")
from app.main_datastore.main_datastore_proxy import MainDatastoreProxy
from app.main_datastore.dataframe_ingestion_client import DataframeIngestionClient

TEST_DATA_FILE = Path(__file__).parent / "test_data.csv"

class MainDatastoreTests(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.read_csv(TEST_DATA_FILE, header=0)
        self.database = MainDatastoreProxy()
        self.client = DataframeIngestionClient(self.database)

    def test_client_upload(self):
        self.client.upload(self.test_data)
        
        author_counts = self.test_data['author'].value_counts()
        for index, row in self.test_data.iterrows():
            author = row['author']
            stored_data = self.database.get(author)
            self.assertEqual(len(stored_data), author_counts[author],
                         'wrong list size of stored data')
            # TODO Check for correct authors/movies

if __name__ == '__main__':
    unittest.main()
