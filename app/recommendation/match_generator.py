'''
This class powers the recommendation backend by finding an author match
for the user, and enriching the response with data from the main data
store.
'''
from typing import Dict, List, Tuple

from app.main_datastore.main_datastore_proxy import MainDatastoreProxy
from app.recommendation.similarity_engine import SimilarityEngine


class MatchGenerator:
    def __init__(self, main_datastore: MainDatastoreProxy,
                 similarity_engine: SimilarityEngine,
                 movie_indices: Dict[str, int],
                 author_by_index: Dict[int, str],
                 average_vec: List[float]):
        self.main_datastore = main_datastore
        self.author_by_index = author_by_index
        self.similarity_engine = similarity_engine
        self.movie_indices = movie_indices
        self.average_vec = average_vec
        self.dim = len(self.movie_indices)

    def _compute_preferences_vector(self, user_input: Dict[str, float]) -> List[float]:
        vector = [0.0] * self.dim
        for movie, rating in user_input.items():
            index = self.movie_indices[movie]
            if rating == -1:
                vector[index] = self.average_vec[index]
            else:
                vector[index] = rating
        return vector

    def get_match(self, user_input: Dict[str, float]) -> Tuple[str, List[Tuple[str, str]]]:
        vector = self._compute_preferences_vector(user_input)
        index_of_match = self.similarity_engine.get_closest_neighbor(vector)
        author_match = self.author_by_index[index_of_match]
        author_reviews = self.main_datastore.get(author_match)
        return (author_match, author_reviews)
