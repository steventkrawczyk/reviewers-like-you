import os.path
from typing import Dict, List

from app.projection.datastore.projection_datastore_shard import ProjectionDatastoreShard
from app.projection.datastore.projection_file_store import ProjectionFileStore


class ProjectionDatastoreProxy:
    '''
    This class is used as a proxy to the database that stores our
    projection.
    '''

    def __init__(self, file_store: ProjectionFileStore,
                 projection_filepath_root: str,
                 movie_indices_filepath: str,
                 in_memory: bool,
                 shard_size: int = 25):
        self.shards = []
        self.movie_indices = dict()
        self.file_store = file_store
        self.projection_filepath_root = projection_filepath_root
        self.movie_indices_filepath = movie_indices_filepath
        self.in_memory = in_memory
        self.shard_size = shard_size
        self.shard_count = len(self.shards)

    def _get_shard_filepath(self, shard_index: str) -> str:
        return self.projection_filepath_root + str(shard_index) + ".json"

    # TODO Use new API
    def _initialize_shards(self):
        shard_index = 0
        while True:
            if os.path.isfile(self._get_shard_filepath(shard_index)):
                self._create_new_shard()
                shard_index += 1
            else:
                return

    def _create_new_shard(self):
        new_shard = ProjectionDatastoreShard(self.file_store,
            self._get_shard_filepath(self.shard_count), self.in_memory)
        self.shards.append(new_shard)
        self.shard_count += 1

    def _load_movie_indices(self) -> None:
        if self.file_store.check_if_object_exists(self.movie_indices_filepath):
            self.movie_indices = self.file_store.get_object(self.movie_indices_filepath)

    def _save_data(self, movie_indices: Dict[str, int]) -> None:
        self.file_store.put_object(self.movie_indices_filepath, movie_indices)

    def _cache_data(self, movie_indices: Dict[str, int]) -> None:
        self.movie_indices = movie_indices

    def load_data(self):
        if not self.in_memory:
            self._load_movie_indices()
        if self.shard_count == 0:
            self._initialize_shards()
        for shard in self.shards:
            shard.load_data()

    def _upload_to_shards(self, projection: Dict[str, List[float]]) -> None:
        ordered_projection = list(projection.items())
        projection_size = len(projection)
        offset = 0
        shard_index = 0
        while offset < projection_size:
            # Create a new shard if we need one
            if shard_index is self.shard_count:
                self._create_new_shard()

            projection_for_shard = dict()
            batch_size = min(self.shard_size, projection_size - offset)
            for batch_index in range(batch_size):
                author, vector = ordered_projection[offset + batch_index]
                projection_for_shard[author] = vector
            self.shards[shard_index].upload(projection_for_shard)
            shard_index += 1
            offset += batch_size

    def upload(self, projection: Dict[str, List[float]], movie_indices: Dict[str, int]) -> None:
        if not self.in_memory:
            self._save_data(movie_indices)
        self._cache_data(movie_indices)
        self._upload_to_shards(projection)

    def get_movie_indices(self) -> Dict[str, int]:
        return self.movie_indices

    def get_shards(self) -> List[ProjectionDatastoreShard]:
        return self.shards
