from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api
from healthcheck import HealthCheck
import logging

from app.config.config_loader import ConfigLoader
from app.ingestion.datastore.upload_client import UploadClient
from app.ingestion.upload_client_factory import UploadClientFactory


UPLOAD_FOLDER = '/reviewers-like-you/tmp'
ALLOWED_EXTENSIONS = {'csv', 'txt'}


class File(Resource):
    def __init__(self, client: UploadClient):
        self.client = client

    def allowed_file(self, filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    # def post(self):

    def post(self):
        file = None
        if 'file' not in request.files:
            logging.warning("No files")
        file = request.files['file']
        if file.filename == '':
            logging.warning("Got empty filename")
        if file and self.allowed_file(file.filename):
            data_string = file.read()
            file_uuid = self.client.upload_file(data_string)
            return jsonify({"message": "",
                            "category": "success",
                            "data": file_uuid,
                            "status": 200})
        return jsonify({"message": "Server error.",
                        "status": 500})


config_filepath = "app/config.yml"
config = ConfigLoader.load(config_filepath)
client = UploadClientFactory(endpoint_url=config["minio_endpoint_url"],
                             bucket_name=config["upload_bucket_name"]).build()

app = Flask(__name__)
health = HealthCheck()
app.add_url_rule("/uploadhealth", "healthcheck",
                 view_func=lambda: health.check())
CORS(app)
api = Api(app)

api.add_resource(File, '/file',
                 resource_class_kwargs={'client': client})

if __name__ == '__main__':
    app.run(debug=True)
