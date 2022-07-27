from typing import Dict, List
from app.recommendation.similarity.similarity_computation import SimilarityComputation


class SimilarityShard:
    '''
    A single compute shard for SimilarityEngine.
    '''

    def __init__(self, vectors: List[List[float]], author_index: Dict[int, str], average_vector: List[float] = None):
        self.vectors = vectors
        self.author_index = author_index
        self.average_vector = average_vector

    def get_closest_neighbor(self, input_vector: List[float]) -> int:
        return SimilarityComputation.shard_computation(input_vector, self.vectors)

    def decode_match(self, index_of_match: int):
        if index_of_match not in self.author_index:
            return None
        return self.author_index[index_of_match]

    def find_average_vector(self):
        return self.average_vector

    def get_vector(self, index):
        return self.vectors[index]
