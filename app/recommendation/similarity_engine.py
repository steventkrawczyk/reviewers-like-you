from typing import List
import numpy as np


class SimilarityEngine:
    '''
    This class encapsulates the algorithm for finding a reviewer match for
    our user. For now, we are using a simple closest neighbor algorithm
    using distance formula.
    '''

    def __init__(self, vectors):
        self.vectors = vectors

    def get_closest_neighbor(self, input_vector: List[float]) -> int:
        input_vector = np.array(input_vector)
        current_min_dist = float("inf")
        nn_index = -1
        for index, vector in enumerate(self.vectors):
            vector = np.array(vector)
            dist = np.linalg.norm(input_vector-vector)
            if dist < current_min_dist:
                current_min_dist = dist
                nn_index = index
        return nn_index
