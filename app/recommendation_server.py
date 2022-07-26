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


database = MainDatastoreFactory().build()
projection_databse = ProjectionDatastoreFactory().build()
movies_to_rate = list(projection_databse.get_movie_indices().keys())
match_generator = MatchGeneratorFactory(database, projection_databse).build()

app = Flask(__name__)
CORS(app)
api = Api(app)


class Movies(Resource):
    def get(self):
        return jsonify({"message": "",
                        "category": "success",
                        "data": movies_to_rate,
                        "status": 200})


class Match(Resource):
    def get(self):
        match_data = ("", [])
        user_input = {}

        # TODO cleanse user input
        for movie, rating in request.args.items():
            user_input[movie] = float(rating)


        print("Matching for " + str(user_input))
        match_data = match_generator.get_match(user_input)
        print("match_data " + str(match_data))

        logging.debug("User got matched with reviewer: " + str(match_data[0]))

        # TODO Revise data schema so that we can support serde more easily
        responseData = {"author": match_data[0], "reviews": []}
        # for review in match_data[1]:
        #     reviewJson = {"movie": review.movie, "rating": review.rating}
        #     responseData["reviews"].append(reviewJson)

        return jsonify({"message": "",
                        "category": "success",
                        "data": responseData,
                        "status": 200})


api.add_resource(Movies, '/movies')
api.add_resource(Match, '/match')

if __name__ == '__main__':
    app.run(debug=True)
