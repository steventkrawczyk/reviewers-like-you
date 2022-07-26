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
    def __init__(self, movies):
        self.movies = movies

    def get(self):
        return jsonify({"message": "",
                        "category": "success",
                        "data": self.movies,
                        "status": 200})


class Match(Resource):
    def __init__(self, match_generator, movies):
        self.match_generator = match_generator
        self.movies = movies

    def _process_request(self, request_data):
        user_ratings = {}
        for movie, rating in request_data:
            if movie in self.movies:
                user_ratings[movie] = float(rating)
            else:
                logging.warning("Parameter in request but not in our index of movies: " + movie)
        return user_ratings

    def _get_match(self, user_input):
        return self.match_generator.get_match(user_input)

    def _build_response(self, match_data):
        response_data = {"author": match_data[0], "reviews": []}
        for review in match_data[1]:
            review_json = {"movie": review.movie, "rating": review.rating}
            response_data["reviews"].append(review_json)
        return response_data

    def get(self):
        user_ratings = self._process_request(request.args.items())
        match_data = self._get_match(user_ratings)
        logging.debug("User got matched with reviewer: " + str(match_data[0]))
        response_data = self._build_response(match_data)
        return jsonify({"message": "",
                        "category": "success",
                        "data": response_data,
                        "status": 200})


database = MainDatastoreFactory().build()
projection_databse = ProjectionDatastoreFactory().build()
movies_to_rate = list(projection_databse.get_movie_indices().keys())
match_generator = MatchGeneratorFactory(database, projection_databse).build()

api.add_resource(Movies, '/movies',
                 resource_class_kwargs={'movies': movies_to_rate})
api.add_resource(Match, '/match', resource_class_kwargs={
                 'match_generator': match_generator, 'movies': movies_to_rate})

if __name__ == '__main__':
    app.run(debug=True)
