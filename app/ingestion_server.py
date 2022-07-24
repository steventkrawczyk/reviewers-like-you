'''
This flask app exposes APIs for data ingestion. It offers two APIs:

upload:
    * author
    * movie
    * rating

batch:
    * filepath
'''
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api
import pandas as pd

from app.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.ingestion.dataframe_ingestion_client import DataframeIngestionClient


database = MainDatastoreProxy()
client = DataframeIngestionClient(database)

app = Flask(__name__)
CORS(app)
api = Api(app)


class Upload(Resource):
    def post(self):
        author, movie, rating = "", "", ""
        for key, arg in request.args.items():
            if key == "author":
                author = arg
            elif key == "movie":
                movie = arg
            elif key == "rating":
                rating = arg
        database.upload(author, movie, rating)
        return jsonify({"message": "",
                        "category": "success",
                        "status": 200})


class Batch(Resource):
    def post(self):
        filepath = ""
        for key, arg in request.args.items():
            if key == "filepath":
                filepath = arg
        data = pd.read_csv(filepath, header=0)
        client.upload(data)
        return jsonify({"message": "",
                        "category": "success",
                        "status": 200})


api.add_resource(Upload, '/upload')
api.add_resource(Batch, '/batch')

if __name__ == '__main__':
    app.run(debug=True)
