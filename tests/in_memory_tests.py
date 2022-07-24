import pandas as pd
from pathlib import Path
import unittest

from app.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.ingestion.dataframe_ingestion_client import DataframeIngestionClient
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.projection.projection_engine import ProjectionEngine
from app.recommendation.match_generator_factory import MatchGeneratorFactory

TEST_DATA_FILE = Path(__file__).parent / "test_data.csv"


class InMemoryTests(unittest.TestCase):
    def setUp(self):
        self.test_data = pd.read_csv(TEST_DATA_FILE, header=0)
        self.database = MainDatastoreProxy(in_memory=True)
        self.projection_databse = ProjectionDatastoreFactory(
            in_memory=True).build()

    def _do_ingestion(self):
        self.client = DataframeIngestionClient(self.database)
        self.client.upload(self.test_data)

    def _do_projection(self):
        self.projection_engine = ProjectionEngine(
            self.database, self.projection_databse)
        self.projection_engine.create_projection()

    def _do_recommendation(self):
        self.match_generator = \
            MatchGeneratorFactory(self.database,
                                  self.projection_databse).build()
        test_user_input = {'bladerunner': 0.4}
        match = self.match_generator.get_match(test_user_input)
        self.assertEqual(match[0], 'steven',
                         'wrong match')
    
    def test_pipeline(self):
        self._do_ingestion()
        self._do_projection()
        self._do_recommendation()


if __name__ == '__main__':
    unittest.main()
