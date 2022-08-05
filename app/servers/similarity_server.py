from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api
from healthcheck import HealthCheck

from app.config.config_loader import ConfigLoader
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.recommendation.similarity.similarity_engine import SimilarityEngine
from app.recommendation.similarity.similarity_engine_factory import SimilarityEngineFactory


class Average(Resource):
    def __init__(self, similarity_engine: SimilarityEngine):
        self.similarity_engine = similarity_engine

    def get(self):
        response = similarity_engine.find_average_vector()
        return jsonify({"message": "",
                        "category": "success",
                        "data": response,
                        "status": 200})


class Closest(Resource):
    def __init__(self, similarity_engine: SimilarityEngine):
        self.similarity_engine = similarity_engine

    def post(self):
        input_vector = request.get_json()["vector"]
        response = similarity_engine.get_closest_neighbor(input_vector)
        return jsonify({"message": "",
                        "category": "success",
                        "data": response,
                        "status": 200})


config_filepath = "app/config.yml"
config = ConfigLoader.load(config_filepath)
projection_datastore = ProjectionDatastoreFactory(endpoint_url=config['minio_endpoint_url'],
                                                  bucket_name=config['projection_bucket_name'],
                                                  projection_filepath_root=config['projection_filepath_root'],
                                                  movie_indices_filepath=config['movie_indices_filepath'],
                                                  in_memory=config['in_memory']).build()
similarity_engine = SimilarityEngineFactory(projection_datastore).build()

app = Flask(__name__)
health = HealthCheck()
app.add_url_rule("/similarityhealth", "healthcheck",
                 view_func=lambda: health.check())
CORS(app)
api = Api(app)

api.add_resource(Average, '/average',
                 resource_class_kwargs={'similarity_engine': similarity_engine})


api.add_resource(Closest, '/closest',
                 resource_class_kwargs={'similarity_engine': similarity_engine})

if __name__ == '__main__':
    app.run(debug=True)
