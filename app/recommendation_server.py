from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api

from app.main_datastore.main_datastore_proxy import MainDatastoreProxy
from app.projection.projection_datastore_proxy import ProjectionDatastoreProxy
from app.projection.projection_engine import ProjectionEngine
from app.recommendation.match_generator import MatchGenerator

# NOTE: This approach is only for testing while we don't have a
# persistent projection DB.
database = MainDatastoreProxy()
authors = list(database.get_keys())
projection_databse = ProjectionDatastoreProxy()
projection_engine = ProjectionEngine(database, projection_databse)
projection_engine.create_projection()
# End test setup

movies_to_rate = list(projection_databse.get_movie_indices().keys())
match_generator = MatchGenerator(database, projection_databse)

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

        match_data = match_generator.get_match(user_input)

        # TODO Revise data schema so that we can support serde more easily
        responseData = {"author": match_data[0], "reviews": []}
        for review_tuple in match_data[1]:
            reviewJson = {"movie": review_tuple[0], "rating": review_tuple[1]}
            responseData["reviews"].append(reviewJson)

        return jsonify({"message": "",
                        "category": "success",
                        "data": responseData,
                        "status": 200})


api.add_resource(Movies, '/movies')
api.add_resource(Match, '/match')

if __name__ == '__main__':
    app.run(debug=True)
