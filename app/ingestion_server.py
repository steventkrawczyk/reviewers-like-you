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
from flask_restful import Resource, Api
import pandas as pd

from app.config.config_loader import ConfigLoader
from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.ingestion.dataframe_ingestion_client import DataframeIngestionClient
from app.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.model.review import Review


class Upload(Resource):
    def __init__(self, database: MainDatastoreProxy):
        self.database = database

    def put(self):
        review = Review.from_dict(request.args)
        logging.debug("Uploading review " + str(review))
        self.database.upload(review)
        return jsonify({"message": "",
                        "category": "success",
                        "status": 200})


class Batch(Resource):
    def __init__(self, client: DataframeIngestionClient):
        self.client = client

    def _extract_and_upload(self, filepath: str):
        data = pd.read_csv(filepath, header=0)
        self.client.upload(data)

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


config_filepath = "app/config.yml"
config = ConfigLoader.load(config_filepath)
main_datastore = MainDatastoreFactory(endpoint_url=config['dynamo_endpoint_url'],
                                      table_name=config['table_name'],
                                      in_memory=config['in_memory']).build()
client = DataframeIngestionClient(main_datastore)

app = Flask(__name__)
api = Api(app)

api.add_resource(Upload, '/upload',
                 resource_class_kwargs={'database': main_datastore})
api.add_resource(Batch, '/batch', resource_class_kwargs={'client': client})

if __name__ == '__main__':
    app.run(debug=True)
