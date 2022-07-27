from app.projection.datastore.projection_datastore_proxy import ProjectionDatastoreProxy


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
        datastore = ProjectionDatastoreProxy(
            self.projection_filepath_root, self.movie_indices_filepath, self.in_memory)
        datastore.load_data()
        return datastore
