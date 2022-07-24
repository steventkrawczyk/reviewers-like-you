'''
Factory class for ProjectionDatastoreProxy.
'''
import json
import os.path
from typing import Dict, List

from app.projection.projection_datastore_proxy import ProjectionDatastoreProxy


class ProjectionDatastoreFactory:
    def __init__(self, projection_filepath: str = f'data/projection.json', 
                 movie_indices_filepath: str = f'data/movie_indices.json'):
        self.projection_filepath = projection_filepath
        self.movie_indices_filepath = movie_indices_filepath

    def build(self) -> ProjectionDatastoreProxy:
        datastore = ProjectionDatastoreProxy(self.projection_filepath, self.movie_indices_filepath)
        datastore.load_data()
        return datastore