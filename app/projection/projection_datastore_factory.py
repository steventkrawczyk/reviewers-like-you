'''
Factory class for ProjectionDatastoreProxy.
'''
from app.projection.projection_datastore_proxy import ProjectionDatastoreProxy


class ProjectionDatastoreFactory:
    def __init__(self, projection_filepath: str = f'data/projection.json',
                 movie_indices_filepath: str = f'data/movie_indices.json',
                 in_memory: bool = False):
        self.projection_filepath = projection_filepath
        self.movie_indices_filepath = movie_indices_filepath
        self.in_memory = in_memory

    def build(self) -> ProjectionDatastoreProxy:
        datastore = ProjectionDatastoreProxy(
            self.projection_filepath, self.movie_indices_filepath, self.in_memory)
        datastore.load_data()
        return datastore
