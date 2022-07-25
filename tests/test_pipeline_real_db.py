import logging

import unittest
import pandas as pd
from pathlib import Path


from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.ingestion.dataframe_ingestion_client import DataframeIngestionClient
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.projection.projection_engine_factory import ProjectionEngineFactory
from app.recommendation.match_generator_factory import MatchGeneratorFactory
from tools.infra.container_orchestrator import ContainerOrchestrator
from tools.infra.database_manager import DatabaseManager

TEST_DATA_FILE = Path(__file__).parent / "test_data.csv"
TABLE_NAME = 'movie_reviews_test'


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        logging.info("Initializing...")
        self.table_name = TABLE_NAME
        self.data = pd.read_csv(TEST_DATA_FILE, header=0)

        self.orchestrator = ContainerOrchestrator()
        self.orchestrator.start_containers()

        self.database_manager = DatabaseManager()
        
    def tearDown(self):
        logging.info("Tearing down...")
        self.orchestrator.stop_containers()

    def _do_ingestion(self, database, data):
        client = DataframeIngestionClient(database)
        client.upload(data)

    def _do_projection(self, database, projection_databse):
        projection_engine = ProjectionEngineFactory(
                database, projection_databse).build()
        projection_engine.create_projection()

    def _do_recommendation(self, database, projection_databse):
        match_generator = \
            MatchGeneratorFactory(database, projection_databse).build()
        test_user_input = {'bladerunner': 0.4}
        return match_generator.get_match(test_user_input)
        
    def test_pipeline(self):
        self.database_manager.create_reviews_table(self.table_name)
        database = MainDatastoreFactory().build(table_name=self.table_name)
        projection_databse = ProjectionDatastoreFactory(
            in_memory=False).build()

        logging.info("Doing ingestion...")
        self._do_ingestion(database, self.data)
        logging.info("Doing projection...")
        self._do_projection(database, projection_databse)
        logging.info("Doing recommendation...")
        match = self._do_recommendation(database, projection_databse)

        assert match[0] == 'steven', 'wrong match'
        logging.info("Success!")
        self.database_manager.delete_table(self.table_name)
