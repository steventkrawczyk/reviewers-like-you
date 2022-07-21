import numpy as np

class SimilarityEngine:
    def __init__(self, vectors):
        self.vectors = vectors

    def get_closest_neighbor(self, input_vector) -> int:
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
