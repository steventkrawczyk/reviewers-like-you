from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_restful import Resource, Api

from app.main_datastore.main_datastore_proxy import MainDatastoreProxy


database = MainDatastoreProxy()

app = Flask(__name__)
CORS(app)
api = Api(app)


class Upload(Resource):
    def post(self):
        author, movie, rating = "", "", ""
        for key, arg in request.args.items():
            if key == "author":
                author = arg
            elif key == "movie":
                movie = arg
            elif key == "rating":
                rating = arg
        database.upload(author, movie, rating)
        return jsonify({"message": "",
                        "category": "success",
                        "status": 200})


api.add_resource(Upload, '/upload')

if __name__ == '__main__':
    app.run(debug=True)
