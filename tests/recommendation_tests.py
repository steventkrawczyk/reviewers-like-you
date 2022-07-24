import pandas as pd
from pathlib import Path
import sys
import unittest




sys.path.append("..")
from app.recommendation.match_generator_factory import MatchGeneratorFactory
from app.projection.projection_engine import ProjectionEngine
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.main_datastore.dataframe_ingestion_client import DataframeIngestionClient
from app.main_datastore.main_datastore_proxy import MainDatastoreProxy

TEST_DATA_FILE = Path(__file__).parent / "test_data.csv"


class ProjectionTests(unittest.TestCase):
    def setUp(self):
        # Upload data
        self.test_data = pd.read_csv(TEST_DATA_FILE, header=0)
        self.database = MainDatastoreProxy(in_memory=True)
        self.client = DataframeIngestionClient(self.database)
        self.client.upload(self.test_data)

        # Create projection
        self.authors = list(self.database.get_keys())
        self.projection_databse = ProjectionDatastoreFactory().build()
        self.projection_engine = ProjectionEngine(
            self.database, self.projection_databse)
        self.projection_engine.create_projection()

        # Create match generator
        self.match_generator = \
            MatchGeneratorFactory(self.database, 
                                  self.projection_databse).build()

    def test_get_match(self):
        test_user_input = {'bladerunner': 0.4}
        match = self.match_generator.get_match(test_user_input)
        self.assertEqual(match[0], 'steven',
                         'wrong match')


if __name__ == '__main__':
    unittest.main()
