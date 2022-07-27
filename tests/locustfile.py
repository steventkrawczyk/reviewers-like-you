import json
import logging
import urllib
from locust import HttpUser, constant, events, task, tag

from tools.infra.database_manager import DatabaseManager
from tools.infra.container_orchestrator import ContainerOrchestrator
from app.model.review import Review

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

orchestrator = ContainerOrchestrator()
database_manager = DatabaseManager()
review = Review("steven", "bladerunner", 0.8).to_dict()


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    logging.info("Starting new load test...")
    orchestrator = ContainerOrchestrator()
    orchestrator.start_containers()
    database_manager.create_reviews_table(TABLE_NAME)


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    logging.info("Finished load test, cleaning up...")
    database_manager.delete_table(TABLE_NAME)
    orchestrator.stop_containers()


class ReviewersLikeYouUser(HttpUser):
    wait_time = constant(1)

    def on_start(self):
        # Add some data at the start so that we can start tasks without error
        self.batch()
        self.create()

    @tag('ingestion', 'upload')
    @task
    def upload(self):
        query_parameters = urllib.parse.urlencode(review)
        request = URL_BASE + INGESTION_PORT + UPLOAD_API + query_parameters
        self.client.put(request, name=UPLOAD_API)

    @tag('ingestion', 'batch')
    @task
    def batch(self):
        query_parameters = urllib.parse.urlencode(
            {"filepath": TEST_DATA_FILE})
        request = URL_BASE + INGESTION_PORT + BATCH_API + query_parameters
        self.client.put(request, name=BATCH_API)

    @tag('projection', 'create')
    @task
    def create(self):
        request = URL_BASE + PROJECTION_PORT + CREATE_API
        self.client.put(request, name=CREATE_API)

    @tag('recommendation', 'movies')
    @task
    def movies(self):
        request = URL_BASE + RECOMMENDATION_PORT + MOVIES_API
        self.client.get(request, name=MOVIES_API)

    @tag('recommendation', 'match')
    @task
    def match(self):
        test_user_input = {'bladerunner': 0.4}
        data = json.dumps(test_user_input).encode("utf-8")
        request = URL_BASE + RECOMMENDATION_PORT + MATCH_API
        self.client.post(request, data=data, headers={
                         "Content-Type": "application/json"}, name=MATCH_API)
