'''
This flask app exposes APIs for data ingestion. It offers two APIs:

upload:
    * author
    * movie
    * rating

batch:
    * filepath
'''
import logging
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api
import pandas as pd

from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.ingestion.dataframe_ingestion_client import DataframeIngestionClient
from app.model.review import Review


database = MainDatastoreFactory().build()
client = DataframeIngestionClient(database)

app = Flask(__name__)
CORS(app)
api = Api(app)


class Upload(Resource):
    def put(self):
        author, movie, rating = "", "", ""
        for key, arg in request.args.items():
            if key == "author":
                author = arg
            elif key == "movie":
                movie = arg
            elif key == "rating":
                rating = arg
        review = Review.build(author, movie, rating)
        logging.debug("Uploading review " + str(review))
        database.upload(review)
        return jsonify({"message": "",
                        "category": "success",
                        "status": 200})


class Batch(Resource):
    def _extract_and_upload(self, filepath: str):
        data = pd.read_csv(filepath, header=0)
        client.upload(data)

    def put(self):
        filepath = ""
        async_execution = False

        for key, arg in request.args.items():
            if key == "filepath":
                filepath = arg
            if key == "async":
                async_execution = bool(arg)

        logging.debug("Uploading file from " + filepath)
        self._extract_and_upload(filepath)
        return jsonify({"message": "",
                        "category": "success",
                        "status": 200})


api.add_resource(Upload, '/upload')
api.add_resource(Batch, '/batch')

if __name__ == '__main__':
    app.run(debug=True)
