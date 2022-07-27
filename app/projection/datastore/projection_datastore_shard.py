from typing import Dict, List

from app.projection.datastore.projection_file_store import ProjectionFileStore


class ProjectionDatastoreShard:
    '''
    A single shard for projection data storage. Corresponds to one file
    storing projection vectors.
    '''

    def __init__(self, file_store: ProjectionFileStore, projection_filepath: str, in_memory: bool):
        self.projection = dict()
        self.file_store = file_store
        self.projection_filepath = projection_filepath
        self.in_memory = in_memory

    def _load_projection(self) -> None:
        if self.file_store.check_if_object_exists(self.projection_filepath):
            self.projection = self.file_store.get_object(self.projection_filepath)

    def _save_data(self, projection: Dict[str, List[float]]) -> None:
        self.file_store.put_object(self.projection_filepath, projection)

    def _cache_data(self, projection: Dict[str, List[float]]) -> None:
        self.projection = projection

    def load_data(self):
        if not self.in_memory:
            self._load_projection()

    def upload(self, projection: Dict[str, List[float]]) -> None:
        if not self.in_memory:
            self._save_data(projection)
        self._cache_data(projection)

    def get_all(self) -> Dict[str, List[float]]:
        return self.projection

    def get(self, author: str):
        return self.projection[author]
