import logging
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
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


main_datastore_proxy = MainDatastoreFactory().build()
projection_datastore_proxy = ProjectionDatastoreFactory().build()
projection_engine = ProjectionEngineFactory(
    main_datastore_proxy, projection_datastore_proxy).build()

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Create, '/create',
                 resource_class_kwargs={'projection_engine': projection_engine})

if __name__ == '__main__':
    app.run(debug=True)
