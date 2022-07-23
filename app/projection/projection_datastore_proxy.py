'''
This class is used as a proxy to the database that stores our
projection.
'''
from typing import Dict, List


class ProjectionDatastoreProxy:
    def __init__(self):
        self.movie_indices = dict()
        self.projection = dict()

    def upload(self, projection: Dict[str, List[float]], movie_indices: Dict[str, int]) -> None:
        self.projection = projection
        self.movie_indices = movie_indices

    def get(self) -> Dict[str, List[float]]:
        return self.projection

    def get_movie_indices(self) -> Dict[str, int]:
        return self.movie_indices
