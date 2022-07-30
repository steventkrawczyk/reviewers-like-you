import logging
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api

from app.config.config_loader import ConfigLoader
from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.scraper.data_submission_client import DataSubmissionClient
from app.scraper.scraper_driver import ScraperDriver
from app.metrics.scraper_metrics_helper import ScraperMetricsHelper
from app.scraper.web_scraper_engine import WebScraperEngine


class Scrape(Resource):
    def __init__(self, scraper_driver: ScraperDriver):
        self.scraper_driver = scraper_driver

    def put(self):
        count = 0
        async_execution = False

        for key, arg in request.args.items():
            if key == "count":
                count = arg
            if key == "async":
                async_execution = bool(arg)

        logging.info("Attempting to scrape " +
                     str(count) + " entries overall.")
        self.scraper_driver.run(count)
        logging.info("Done scraping.")

        return jsonify({"message": "",
                        "category": "success",
                        "status": 200})


# TODO some props need to migrated to config (e.g. metrics)
config_filepath = "app/config.yml"
config = ConfigLoader.load(config_filepath)
main_datastore = MainDatastoreFactory(endpoint_url=config['dynamo_endpoint_url'],
                                      table_name=config['table_name'],
                                      in_memory=config['in_memory']).build()
data_submission_client = DataSubmissionClient(main_datastore)
web_scraper_engine = WebScraperEngine()
metrics_helper = ScraperMetricsHelper()
scraper_driver = ScraperDriver(
    data_submission_client, web_scraper_engine, metrics_helper)

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Scrape, '/scrape',
                resource_class_kwargs={'scraper_driver': scraper_driver})

if __name__ == '__main__':
    app.run(debug=True)
