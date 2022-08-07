from typing import Dict, List

from app.common.python.projection.datastore.projection_datastore_shard import ProjectionDatastoreShard

MAX_SHARD_COUNT = 100


class ProjectionDatastoreProxy:
    '''
    This class is used as a proxy to the database that stores our
    projection.
    '''

    def __init__(self, shard_size: int = 25):
        self.shards = []
        self.movie_indices = dict()
        self.shard_size = shard_size
        self.shard_count = len(self.shards)

    def _create_new_shard(self):
        new_shard = ProjectionDatastoreShard()
        self.shards.append(new_shard)
        self.shard_count += 1

    def _cache_data(self, movie_indices: Dict[str, int]) -> None:
        self.movie_indices = movie_indices

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
        self._cache_data(movie_indices)
        self._upload_to_shards(projection)

    def get_movie_indices(self) -> Dict[str, int]:
        return self.movie_indices

    def get_shards(self) -> List[ProjectionDatastoreShard]:
        return self.shards
