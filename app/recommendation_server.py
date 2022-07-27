'''
This flask app exposes APIs for recommendation. It offers two APIs:

movies:
    no query parameters

match:
    query parameters are of the form "MOVIE=RATING"
'''
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api
import logging

from app.ingestion.main_datastore_factory import MainDatastoreFactory
from app.projection.projection_datastore_factory import ProjectionDatastoreFactory
from app.recommendation.match_generator_factory import MatchGeneratorFactory


app = Flask(__name__)
CORS(app)
api = Api(app)


class Movies(Resource):
    def __init__(self, projection_datastore):
        self.projection_datastore = projection_datastore

    def get(self):
        movies = list(self.projection_datastore.get_movie_indices().keys())
        return jsonify({"message": "",
                        "category": "success",
                        "data": movies,
                        "status": 200})


class Match(Resource):
    def __init__(self, main_datastore, projection_datastore):
        self.main_datastore = main_datastore
        self.projection_datastore = projection_datastore

    # NOTE This is required for testing, since otherwise we init
    # an empty projection when we run `docker compose up`.
    def _load_match_generator(self):
        self.movies = list(
            self.projection_datastore.get_movie_indices().keys())
        self.match_generator = MatchGeneratorFactory(
            self.main_datastore, self.projection_datastore).build()

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
        self._load_match_generator()
        user_ratings = self._process_request(request)
        match_data = self._get_match(user_ratings)
        logging.debug("User got matched with reviewer: " + str(match_data[0]))
        response_data = self._build_response(match_data)
        return jsonify({"message": "",
                        "category": "success",
                        "data": response_data,
                        "status": 200})


main_datastore = MainDatastoreFactory().build()
projection_datastore = ProjectionDatastoreFactory().build()

api.add_resource(Movies, '/movies',
                 resource_class_kwargs={'projection_datastore': projection_datastore})
api.add_resource(Match, '/match',
                 resource_class_kwargs={'main_datastore': main_datastore, 'projection_datastore': projection_datastore})

if __name__ == '__main__':
    app.run(debug=True)
