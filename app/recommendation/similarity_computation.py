

from typing import List
import numpy as np


class SimilarityComputation:
    @staticmethod
    def shard_computation(input_vector: List[float], possible_neighbors: List[List[float]]):
        print("shard")
        return SimilarityComputation._get_closest_neighbor(input_vector, possible_neighbors)

    @staticmethod
    def merge_computation(input_vector: List[float], possible_neighbors: List[List[float]]):
        print("merge")
        return SimilarityComputation._get_closest_neighbor(input_vector, possible_neighbors)

    @staticmethod
    def _get_closest_neighbor(input_vector: List[float], possible_neighbors: List[List[float]]) -> int:
        input_vector = np.array(input_vector)
        current_min_dist = float("inf")
        nn_index = -1
        print("possible_neighbors: " + str(possible_neighbors))
        for index, vector in enumerate(possible_neighbors):
            vector = np.array(vector)
            dist = np.linalg.norm(input_vector-vector)
            if dist < current_min_dist:
                current_min_dist = dist
                nn_index = index
        return nn_index