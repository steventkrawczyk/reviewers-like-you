from typing import List

from app.common.python.recommendation.similarity.similarity_engine import SimilarityEngine


class InMemorySimilarityClient:
    def __init__(self, similarity_engine: SimilarityEngine):
        self.similarity_engine = similarity_engine

    def find_average_vector(self) -> List[float]:
        return self.similarity_engine.find_average_vector()

    def get_closest_neighbor(self, input_vector: List[float]) -> str:
        return self.similarity_engine.get_closest_neighbor(input_vector)
