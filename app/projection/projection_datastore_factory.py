from app.projection.datastore.projection_datastore_proxy import ProjectionDatastoreProxy
from app.projection.datastore.projection_file_store import ProjectionFileStore


class ProjectionDatastoreFactory:
    '''
    Factory class for ProjectionDatastoreProxy.
    '''

    def __init__(self, projection_filepath_root: str = f'data/projection_',
                 movie_indices_filepath: str = f'data/movie_indices.json',
                 in_memory: bool = False):
        self.projection_filepath_root = projection_filepath_root
        self.movie_indices_filepath = movie_indices_filepath
        self.in_memory = in_memory

    def build(self) -> ProjectionDatastoreProxy:
        file_store = None
        if not self.in_memory:
            file_store = ProjectionFileStore()
            file_store.make_projections_bucket()

        datastore = ProjectionDatastoreProxy(file_store,
            self.projection_filepath_root, self.movie_indices_filepath, self.in_memory)
        datastore.load_data()
        return datastore
