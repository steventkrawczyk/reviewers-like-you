import docker
import logging
import time
import unittest
import boto3
import pandas as pd
from pathlib import Path
import subprocess

from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.ingestion.dataframe_ingestion_client import DataframeIngestionClient
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.projection.projection_engine import ProjectionEngine
from app.recommendation.match_generator_factory import MatchGeneratorFactory


TEST_DATA_FILE = Path(__file__).parent / "test_data.csv"
TABLE_NAME = 'movie_reviews_test'


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        logging.info("Initializing...")
        self.table_name = TABLE_NAME
        self.data = pd.read_csv(TEST_DATA_FILE, header=0)
        self.dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:8000", region_name="us-west-2")
        self._start_dynamo_docker_container()
        
    def tearDown(self):
        logging.info("Tearing down...")
        self._stop_and_delete_dynamo_docker_container()

    def _start_dynamo_docker_container(self):
        subprocess.Popen("docker compose up", shell=True)

        client = docker.client.DockerClient()
        while len(client.containers.list()) == 0:
            time.sleep(0.1)
        container = client.containers.get("dynamodb-local")
        assert container.status == "running"

    def _stop_and_delete_dynamo_docker_container(self):
        client = docker.client.DockerClient()
        container = client.containers.get("dynamodb-local")
        container.stop()
        client.containers.prune()
        
        
    def _create_test_table(self):
        table = self.dynamodb.create_table(
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'author',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'movie',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'author',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'movie',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        return table

    def _delete_test_table(self):
        self.dynamodb.delete_table(TableName=self.table_name)

    def _do_ingestion(self, database, data):
        client = DataframeIngestionClient(database)
        client.upload(data)

    def _do_projection(self, database, projection_databse):
        projection_engine = ProjectionEngine(
                database, projection_databse)
        projection_engine.create_projection()

    def _do_recommendation(self, database, projection_databse):
        match_generator = \
            MatchGeneratorFactory(database, projection_databse).build()
        test_user_input = {'bladerunner': 0.4}
        return match_generator.get_match(test_user_input)
        
    def test_pipeline(self):
        self.ddb_table = self._create_test_table()
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
        self._delete_test_table()
