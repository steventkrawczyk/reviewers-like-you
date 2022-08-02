import json
import urllib
from locust import HttpUser, constant, task, tag
import requests

from tools.infra.database_manager import DatabaseManager
from app.model.review import Review

TEST_DATA_FILE = "tests/test_data.csv"
TABLE_NAME = 'movie_reviews'

BACKEND_PROXY = "http://backendproxy:5000"
INTERNAL_PROXY = "http://internalproxy:5000"

UPLOAD_API = "/upload?"
BATCH_API = "/batch?"
CREATE_API = "/create"
MOVIES_API = "/movies"
MATCH_API = "/match?"
FILE_API = "/file"

database_manager = DatabaseManager("http://dynamodb-local:8000")
review = Review("steven", "bladerunner", 0.8).to_dict()


class ReviewersLikeYouUser(HttpUser):
    wait_time = constant(1)

    @tag('ingestion', 'upload')
    @task
    def upload(self):
        query_parameters = urllib.parse.urlencode(review)
        request = INTERNAL_PROXY + UPLOAD_API + query_parameters
        self.client.put(request, name=UPLOAD_API)

    @tag('ingestion', 'batch')
    @task
    def batch(self):
        filepath = ""
        with open(TEST_DATA_FILE, 'rb') as f:
            file_response = self.client.post(INTERNAL_PROXY + FILE_API, files={"file": f}, name=FILE_API)
            file_data = file_response.json()
            filepath = file_data["data"]
        ingestion_query_parameters = urllib.parse.urlencode({"filepath": filepath})
        ingestion_request_url = INTERNAL_PROXY + \
            BATCH_API + ingestion_query_parameters
        self.client.put(ingestion_request_url, name=BATCH_API)

    @tag('projection', 'create')
    @task
    def create(self):
        request = INTERNAL_PROXY + CREATE_API
        self.client.put(request, name=CREATE_API)

    @tag('recommendation', 'movies')
    @task
    def movies(self):
        request = BACKEND_PROXY + MOVIES_API
        self.client.get(request, name=MOVIES_API)

    @tag('recommendation', 'match')
    @task
    def match(self):
        test_user_input = {'bladerunner': 0.4}
        data = json.dumps(test_user_input).encode("utf-8")
        request = BACKEND_PROXY + MATCH_API
        self.client.post(request, data=data, headers={
                         "Content-Type": "application/json"}, name=MATCH_API)
