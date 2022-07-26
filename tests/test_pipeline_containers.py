import json
import logging
import unittest
import pandas as pd
import urllib

import urllib3

from app.model.review import Review
from tools.infra.container_orchestrator import ContainerOrchestrator
from tools.infra.database_manager import DatabaseManager

TEST_DATA_FILE = "tests/test_data.csv"
TABLE_NAME = 'movie_reviews'

URL_BASE = "http://localhost:"
INGESTION_PORT = "5001"
PROJECTION_PORT = "5002"
RECOMMENDATION_PORT = "5000"

UPLOAD_API = "/upload?"
BATCH_API = "/batch?"
CREATE_API = "/create"
MOVIES_API = "/movies"
MATCH_API = "/match?"


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        logging.info("Initializing...")
        self.table_name = TABLE_NAME
        self.data = pd.read_csv(TEST_DATA_FILE, header=0)

        self.orchestrator = ContainerOrchestrator()
        self.orchestrator.start_containers()

        self.database_manager = DatabaseManager()

        self.http = urllib3.PoolManager()

    def tearDown(self):
        logging.info("Tearing down...")
        self.orchestrator.stop_containers()

    def _do_ingestion_batch(self, filename):
        query_parameters = urllib.parse.urlencode({"filepath": filename})
        request = URL_BASE + INGESTION_PORT + BATCH_API + query_parameters
        response = self.http.request('PUT', request)
        self.assertEqual(response.status, 200)

    def _do_ingestion_single_review(self, review):
        query_parameters = urllib.parse.urlencode(review.serialize())
        request = URL_BASE + INGESTION_PORT + UPLOAD_API + query_parameters
        response = self.http.request('PUT', request)
        self.assertEqual(response.status, 200)

    def _do_projection(self):
        request = URL_BASE + PROJECTION_PORT + CREATE_API
        response = self.http.request('PUT', request)
        self.assertEqual(response.status, 200)

    def _do_recommendation(self, test_user_input):
        request = URL_BASE + RECOMMENDATION_PORT + MOVIES_API
        response = self.http.request('GET', request)
        self.assertEqual(response.status, 200)

        query_parameters = urllib.parse.urlencode(test_user_input)
        request = URL_BASE + RECOMMENDATION_PORT + MATCH_API + query_parameters
        response = self.http.request('GET', request)
        self.assertEqual(response.status, 200)

        result = json.loads(response.data.decode('utf-8'))
        self.assertIn("data", result)
        self.assertIn("author", result["data"])
        self.assertIn("reviews", result["data"])
        return (result["data"]["author"], result["data"]["reviews"])

    def test_pipeline(self):
        self.database_manager.create_reviews_table(self.table_name)

        logging.info("Doing ingestion...")
        review = Review("steven", "bladerunner", 0.8)
        self._do_ingestion_batch(TEST_DATA_FILE)
        self._do_ingestion_single_review(review)

        logging.info("Doing projection...")
        self._do_projection()

        logging.info("Doing recommendation...")
        test_user_input = {'bladerunner': 0.4}
        match = self._do_recommendation(test_user_input)

        self.assertEqual(match[0], "steven")
        logging.info("Success!")
        self.database_manager.delete_table(self.table_name)
