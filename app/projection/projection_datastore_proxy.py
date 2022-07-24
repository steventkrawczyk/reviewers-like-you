'''
This class is used as a proxy to the database that stores our
projection.
'''
import json
import os.path
from typing import Dict, List


class ProjectionDatastoreProxy:
    def __init__(self, projection_filepath: str,
                 movie_indices_filepath: str):
        self.projection = dict()
        self.movie_indices = dict()
        self.projection_filepath = projection_filepath
        self.movie_indices_filepath = movie_indices_filepath

    def _load_projection(self) -> None:
        if os.path.isfile(self.projection_filepath):
            with open(self.projection_filepath) as f:
                self.projection = json.load(f)

    def _load_movie_indices(self) -> None:
        if os.path.isfile(self.movie_indices_filepath):
            with open(self.movie_indices_filepath) as f:
                self.movie_indices = json.load(f)
    
    def _save_data(self, projection: Dict[str, List[float]], movie_indices: Dict[str, int]) -> None:
        with open(self.projection_filepath, 'w+', encoding='utf-8') as f:
            json.dump(projection, f, ensure_ascii=False, indent=4)
        with open(self.movie_indices_filepath, 'w+', encoding='utf-8') as f:
            json.dump(movie_indices, f, ensure_ascii=False, indent=4)

    def _cache_data(self, projection: Dict[str, List[float]], movie_indices: Dict[str, int]) -> None:
        self.projection = projection
        self.movie_indices = movie_indices

    def load_data(self):
        self._load_projection()
        self._load_movie_indices()
    
    def upload(self, projection: Dict[str, List[float]], movie_indices: Dict[str, int]) -> None:
        self._save_data(projection, movie_indices)
        self._cache_data(projection, movie_indices)

    def get(self) -> Dict[str, List[float]]:
        return self.projection

    def get_movie_indices(self) -> Dict[str, int]:
        return self.movie_indices
