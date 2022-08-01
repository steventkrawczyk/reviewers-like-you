'''
This flask app exposes an API for the movie list. It offers one APIs:

movies:
    no query parameters
'''
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask_restful import Resource, Api

from app.config.config_loader import ConfigLoader
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory


class Movies(Resource):
    def __init__(self, movies, reload_for_testing, projection_datastore):
        self.movies = movies
        self.reload_for_testing = reload_for_testing
        self.projection_datastore = projection_datastore

    # NOTE This is required for testing, since otherwise we init
    # an empty projection when we run `docker compose up`.
    def _reload_movie_list(self):
        self.movies = list(
            self.projection_datastore.get_movie_indices().keys())

    def get(self):
        if self.reload_for_testing:
            self._reload_movie_list()
        return jsonify({"message": "",
                        "category": "success",
                        "data": self.movies,
                        "status": 200})


config_filepath = "app/config.yml"
config = ConfigLoader.load(config_filepath)
projection_datastore = ProjectionDatastoreFactory(endpoint_url=config['minio_endpoint_url'],
                                                  bucket_name=config['bucket_name'],
                                                  projection_filepath_root=config['projection_filepath_root'],
                                                  movie_indices_filepath=config['movie_indices_filepath'],
                                                  in_memory=config['in_memory']).build()
movies = list(projection_datastore.get_movie_indices().keys())

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Movies, '/movies',
                 resource_class_kwargs={'movies': movies,
                                        'reload_for_testing': config['reload_for_testing'],
                                        'projection_datastore': projection_datastore})

if __name__ == '__main__':
    app.run(debug=True)
