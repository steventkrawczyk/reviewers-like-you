import logging
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.projection.projection_engine_factory import ProjectionEngineFactory


app = Flask(__name__)
CORS(app)
api = Api(app)

main_datastore_proxy = MainDatastoreFactory().build()
projection_datastore_proxy = ProjectionDatastoreFactory().build()
projection_engine = ProjectionEngineFactory(
    main_datastore_proxy, projection_datastore_proxy).build()


class Create(Resource):
    def put(self):
        async_execution = False

        for key, arg in request.args.items():
            if key == "async":
                async_execution = bool(arg)

        logging.info("Creating projection...")
        projection_engine.create_projection()
        logging.info("Done!")

        return jsonify({"message": "",
                        "category": "success",
                        "status": 200})


api.add_resource(Create, '/create')

if __name__ == '__main__':
    app.run(debug=True)
