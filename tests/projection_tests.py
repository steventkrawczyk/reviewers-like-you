import pandas as pd
from pathlib import Path
import sys
import unittest


sys.path.append("..")
from app.projection.projection_engine import ProjectionEngine
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.ingestion.dataframe_ingestion_client import DataframeIngestionClient
from app.ingestion.main_datastore_proxy import MainDatastoreProxy

TEST_DATA_FILE = Path(__file__).parent / "test_data.csv"


class ProjectionTests(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.read_csv(TEST_DATA_FILE, header=0)
        self.database = MainDatastoreProxy(in_memory=True)
        self.client = DataframeIngestionClient(self.database)
        self.client.upload(self.test_data)
        self.authors = list(self.database.get_keys())
        self.projection_databse = ProjectionDatastoreFactory().build()
        self.projection_engine = ProjectionEngine(
            self.database, self.projection_databse)

    def test_create_projection(self):
        self.projection_engine.create_projection()
        projection = self.projection_databse.get()
        self.assertEqual(len(projection), len(self.authors),
                         'Incorrect number of authors')

        # TODO Make this more robust
        self.assertEqual(len(projection[self.authors[0]]), 1,
                         'Incorrect proj. space size')


if __name__ == '__main__':
    unittest.main()
