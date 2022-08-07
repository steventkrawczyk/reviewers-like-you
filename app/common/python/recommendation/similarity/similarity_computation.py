from typing import List, Tuple
import numpy as np


class SimilarityComputation:
    '''
    This class is used to define the computations for the shards and
    the driver (SimilarityEngine) that are used complete the distributed
    similarity computation.
    '''
    @staticmethod
    def shard_computation(input_vector: List[float], possible_neighbors: List[List[float]]) -> Tuple[int, float]:
        '''
        The shard method returns a tuple of (nn_index, distance), so that the driver can merge the results
        '''
        return SimilarityComputation._get_closest_neighbor(input_vector, possible_neighbors)

    @staticmethod
    def driver_computation(distances: List[float]) -> int:
        '''
        Merges results by finding the index of the min distance.
        '''
        return distances.index(min(distances))
    
    @staticmethod
    def _get_closest_neighbor(input_vector: List[float], possible_neighbors: List[List[float]]) -> Tuple[int, float]:
        input_vector = np.array(input_vector)
        current_min_dist = float("inf")
        nn_index = -1
        for index, vector in enumerate(possible_neighbors):
            vector = np.array(vector)
            dist = np.linalg.norm(input_vector-vector)
            if dist < current_min_dist:
                current_min_dist = dist
                nn_index = index
        return nn_index, current_min_dist
