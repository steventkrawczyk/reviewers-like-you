'''
This flask app exposes APIs for recommendation. It offers one APIs:

match:
    query parameters are of the form "MOVIE=RATING"
'''
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api
import logging

from app.config.config_loader import ConfigLoader
from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.recommendation.generatory_factory_facade import GeneratorFactoryFacade
from app.recommendation.movies_client import MoviesClient


class Match(Resource):
    def __init__(self, match_generator, movies, reload_for_testing, main_datastore):
        self.match_generator = match_generator
        self.movies = movies
        self.reload_for_testing = reload_for_testing
        self.main_datastore = main_datastore

    # NOTE This is required for testing, since otherwise we init
    # an empty projection when we run `docker compose up`.
    def _reload_match_generator(self):
        self.movies = MoviesClient().get_movie_indices(include_indices=False)
        self.match_generator = GeneratorFactoryFacade(
            self.main_datastore).build()

    def _process_request(self, request):
        user_ratings = {}
        for movie, rating in request.get_json().items():
            if movie in self.movies:
                user_ratings[movie] = float(rating)
            else:
                logging.warning(
                    "Parameter in request data but not in our index of movies: " + movie)
        return user_ratings

    def _get_match(self, user_input):
        return self.match_generator.get_match(user_input)

    def _build_response(self, match_data):
        response_data = {"author": match_data[0], "reviews": []}
        for review in match_data[1]:
            review_json = {"movie": review.movie, "rating": review.rating}
            response_data["reviews"].append(review_json)
        return response_data

    def post(self):
        if self.reload_for_testing:
            self._reload_match_generator()
        user_ratings = self._process_request(request)
        match_data = self._get_match(user_ratings)
        logging.debug("User got matched with reviewer: " + str(match_data[0]))
        response_data = self._build_response(match_data)
        return jsonify({"message": "",
                        "category": "success",
                        "data": response_data,
                        "status": 200})


config_filepath = "app/config.yml"
config = ConfigLoader.load(config_filepath)
main_datastore = MainDatastoreFactory(endpoint_url=config['dynamo_endpoint_url'],
                                      table_name=config['table_name'],
                                      in_memory=config['in_memory']).build()
movies = MoviesClient().get_movie_indices(include_indices=False)
match_generator = None
if config['in_memory']:
    projection_datastore = ProjectionDatastoreFactory(endpoint_url=config['minio_endpoint_url'],
                                                      bucket_name=config['bucket_name'],
                                                      projection_filepath_root=config['projection_filepath_root'],
                                                      movie_indices_filepath=config['movie_indices_filepath'],
                                                      in_memory=config['in_memory']).build()
    match_generator = GeneratorFactoryFacade(
        main_datastore, projection_datastore, True).build()
else:
    match_generator = GeneratorFactoryFacade(main_datastore).build()

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Match, '/match',
                 resource_class_kwargs={'match_generator': match_generator,
                                        'movies': movies,
                                        'reload_for_testing': config['reload_for_testing'],
                                        'main_datastore': main_datastore})

if __name__ == '__main__':
    app.run(debug=True)
