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
from healthcheck import HealthCheck

from app.config.config_loader import ConfigLoader
from app.ingestion.datastore.upload_client import UploadClient
from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.ingestion.dataframe_ingestion_client import DataframeIngestionClient
from app.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.ingestion.upload_client_factory import UploadClientFactory
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
    def __init__(self, dataframe_client: DataframeIngestionClient, file_client: UploadClient):
        self.dataframe_client = dataframe_client
        self.file_client = file_client

    def _extract_and_upload(self, filepath: str):
        data = self.file_client.download_dataframe(filepath)
        self.dataframe_client.upload(data)

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
dataframe_client = DataframeIngestionClient(main_datastore)
file_client = UploadClientFactory(endpoint_url=config["minio_endpoint_url"],
                                  bucket_name=config["upload_bucket_name"]).build()

app = Flask(__name__)
health = HealthCheck()
app.add_url_rule("/ingestionhealth", "healthcheck",
                 view_func=lambda: health.check())
CORS(app)
api = Api(app)

api.add_resource(Upload, '/upload',
                 resource_class_kwargs={'database': main_datastore})
api.add_resource(
    Batch, '/batch', resource_class_kwargs={'dataframe_client': dataframe_client,
                                            'file_client': file_client})

if __name__ == '__main__':
    app.run(debug=True)
