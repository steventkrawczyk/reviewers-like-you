import json
from typing import List
from urllib import request


class SimilarityClient:
    def __init__(self):
        self.average_request_url = "http://backendproxy:5000/average"
        self.closest_request_url = "http://backendproxy:5000/closest"

    def find_average_vector(self) -> List[float]:
        average_request = request.Request(
            self.average_request_url, method="GET")
        average_response = request.urlopen(average_request)
        response_data = json.loads(average_response.read())
        return response_data["data"]

    def get_closest_neighbor(self, input_vector: List[float]) -> str:
        data = json.dumps({"vector": input_vector}).encode("utf-8")
        closest_requset = request.Request(
            self.closest_request_url, data=data, method="POST")
        closest_requset.add_header("Content-Type", "application/json")
        closest_response = request.urlopen(closest_requset)
        response_data = json.loads(closest_response.read())
        return response_data["data"]
