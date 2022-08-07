import json
from typing import List
from urllib import request


class MoviesClient:
    def __init__(self):
        self.request_url = "http://backendproxy:5000/movies?indices="

    def get_movie_indices(self, include_indices: bool = True) -> List[float]:
        movies_request = request.Request(
            self.request_url + str(include_indices), method="POST")
        movies_response = request.urlopen(movies_request)
        response_data = json.loads(movies_response.read())
        return response_data["data"]
