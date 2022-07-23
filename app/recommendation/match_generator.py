from typing import Dict, List, Tuple

from app.main_datastore.main_datastore_proxy import MainDatastoreProxy
from app.projection.projection_datastore_proxy import ProjectionDatastoreProxy
from app.recommendation.similarity_engine import SimilarityEngine


class MatchGenerator:
    # TODO create a factory for this
    def __init__(self, main_datastore: MainDatastoreProxy, projection_datastore: ProjectionDatastoreProxy):
        self.main_datastore = main_datastore
        self.projection_datastore = projection_datastore

        # We cache these because the calls to DB might be expensive
        # TODO Once a real DB is implemented, evaluate the tradeoff
        self.projection = self.projection_datastore.get()
        self.movie_indices = self.projection_datastore.get_movie_indices()

        self.dim = len(self.movie_indices)
        self._build_similarity_engine()

    def _build_similarity_engine(self) -> None:
        vectors = []
        self.author_by_index = dict()
        index = 0
        for author, vector in self.projection.items():
            if author == "_average":
                self.average_vec = vector
            else:
                self.author_by_index[index] = author
                index += 1
                vectors.append(vector)
        self.similarity_engine = SimilarityEngine(vectors)

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
