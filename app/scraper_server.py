import logging
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api

from app.scraper.data_submission_client import DataSubmissionClient
from app.scraper.scraper_driver import ScraperDriver
from app.metrics.scraper_metrics_helper import ScraperMetricsHelper
from app.scraper.web_scraper_engine import WebScraperEngine

app = Flask(__name__)
CORS(app)
api = Api(app)

data_submission_client = DataSubmissionClient()
web_scraper_engine = WebScraperEngine()
metrics_helper = ScraperMetricsHelper()

scraper_driver = ScraperDriver(
    data_submission_client, web_scraper_engine, metrics_helper)


class Scrape(Resource):
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
        scraper_driver.run(count)
        logging.info("Done scraping.")

        return jsonify({"message": "",
                        "category": "success",
                        "status": 200})


api.add_resource(Scrape, '/scrape')

if __name__ == '__main__':
    app.run(debug=True)
