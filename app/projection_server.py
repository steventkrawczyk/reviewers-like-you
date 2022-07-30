import logging
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from flask_restful import Resource, Api

from app.config.config_loader import ConfigLoader
from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.projection.engine.projection_engine import ProjectionEngine
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.projection.projection_engine_factory import ProjectionEngineFactory


class Create(Resource):
    def __init__(self, projection_engine: ProjectionEngine):
        self.projection_engine = projection_engine

    def put(self):
        async_execution = False

        for key, arg in request.args.items():
            if key == "async":
                async_execution = bool(arg)

        logging.info("Creating projection...")
        self.projection_engine.create_projection()
        logging.info("Done!")

        return jsonify({"message": "",
                        "category": "success",
                        "status": 200})


config_filepath = "app/config.yml"
config = ConfigLoader.load(config_filepath)
main_datastore = MainDatastoreFactory(endpoint_url=config['dynamo_endpoint_url'],
                                      table_name=config['table_name'],
                                      in_memory=config['in_memory']).build()
projection_datastore = ProjectionDatastoreFactory(endpoint_url=config['minio_endpoint_url'],
                                                  bucket_name=config['bucket_name'],
                                                  projection_filepath_root=config['projection_filepath_root'],
                                                  movie_indices_filepath=config['movie_indices_filepath'],
                                                  in_memory=config['in_memory']).build()
projection_engine = ProjectionEngineFactory(
    main_datastore, projection_datastore).build()

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Create, '/create',
                 resource_class_kwargs={'projection_engine': projection_engine})

if __name__ == '__main__':
    app.run(debug=True)
