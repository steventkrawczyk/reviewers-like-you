from typing import List

from app.recommendation.similarity_computation import SimilarityComputation
from app.recommendation.similarity_shard import SimilarityShard


class SimilarityEngine:
    '''
    This class encapsulates the algorithm for finding a reviewer match for
    our user. For now, we are using a simple closest neighbor algorithm
    using distance formula.
    '''

    def __init__(self, shards: List[SimilarityShard]):
        self.shards = shards

    def find_average_vector(self) ->  List[float]:
        average_vector = None
        for shard in self.shards:
            shard_average_vector = shard.find_average_vector()
            if shard_average_vector is not None:
                average_vector = shard_average_vector
        return average_vector

    def get_closest_neighbor(self, input_vector: List[float]) -> str:
        vectors_from_shards = []
        author_index = dict()
        for shard_index, shard in enumerate(self.shards):
            nn_index_from_shard = shard.get_closest_neighbor(input_vector)
            vector_from_shard = shard.get_vector(nn_index_from_shard)
            author_index[shard_index] = shard.decode_match(nn_index_from_shard)
            vectors_from_shards.append(vector_from_shard)
        nn_index = SimilarityComputation.driver_computation(input_vector, vectors_from_shards)
        return author_index[nn_index]


