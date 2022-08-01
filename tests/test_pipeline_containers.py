import json
import unittest
from urllib import request, parse
import warnings

from app.model.review import Review
from tools.infra.database_manager import DatabaseManager


TEST_DATA_FILE = "tests/test_data.csv"
TABLE_NAME = 'movie_reviews'

EXTERNAL_PROXY = "http://externalproxy:5000"
INTERNAL_PROXY = "http://internalproxy:5000"

UPLOAD_API = "/upload?"
BATCH_API = "/batch?"
CREATE_API = "/create"
MOVIES_API = "/movies"
MATCH_API = "/match"


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.table_name = TABLE_NAME
        self.database_manager = DatabaseManager("http://dynamodb-local:8000")
        self.database_manager.create_reviews_table(self.table_name)

    def tearDown(self):
        self.database_manager.delete_table(self.table_name)

    def _do_ingestion_batch(self, filename):
        ingestion_query_parameters = parse.urlencode({"filepath": filename})
        ingestion_request_url = INTERNAL_PROXY + \
            BATCH_API + ingestion_query_parameters
        ingestion_request = request.Request(
            ingestion_request_url, method="PUT")
        ingestion_response = request.urlopen(ingestion_request)
        self.assertEqual(ingestion_response.status, 200)

    def _do_ingestion_single_review(self, review):
        ingestion_query_parameters = parse.urlencode(review.to_dict())
        ingestion_request_url = INTERNAL_PROXY + \
            UPLOAD_API + ingestion_query_parameters
        ingestion_request = request.Request(
            ingestion_request_url, method="PUT")
        ingestion_response = request.urlopen(ingestion_request)
        self.assertEqual(ingestion_response.status, 200)

    def _do_projection(self):
        create_request_url = INTERNAL_PROXY + CREATE_API
        create_request = request.Request(create_request_url, method="PUT")
        create_response = request.urlopen(create_request)
        self.assertEqual(create_response.status, 200)

    def _get_movies(self):
        movies_request_url = EXTERNAL_PROXY + MOVIES_API
        movies_request = request.Request(movies_request_url, method="GET")
        movies_response = request.urlopen(movies_request)
        self.assertEqual(movies_response.status, 200)

    def _get_match(self, test_user_input):
        match_request_url = EXTERNAL_PROXY + MATCH_API
        data = json.dumps(test_user_input).encode("utf-8")
        match_request = request.Request(
            match_request_url, data=data, method="POST")
        match_request.add_header("Content-Type", "application/json")
        match_response = request.urlopen(match_request)
        self.assertEqual(match_response.status, 200)
        match_data = json.loads(match_response.read())
        self.assertIn("data", match_data)
        self.assertIn("author", match_data["data"])
        self.assertIn("reviews", match_data["data"])
        return (match_data["data"]["author"], match_data["data"]["reviews"])

    def test_pipeline(self):
        review = Review("steven", "bladerunner", 0.8)
        self._do_ingestion_batch(TEST_DATA_FILE)
        self._do_ingestion_single_review(review)

        self._do_projection()

        self._get_movies()
        test_user_input = {'bladerunner': 0.4}
        match = self._get_match(test_user_input)
        self.assertEqual(match[0], "steven")

        test_user_input = {'bladerunner': 1.0}
        match = self._get_match(test_user_input)
        self.assertNotEqual(match[0], "steven")

        test_user_input = {'bladerunner': -1.0}
        match = self._get_match(test_user_input)
        self.assertNotEqual(match[0], "steven")
