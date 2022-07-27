from typing import Dict, List, Set, Tuple

from app.ingestion.main_datastore_proxy import MainDatastoreProxy


class ProjectionBuilder:
    '''
    This class encapsulates the logic to build our vector projection space
    given a list of authors, movies for rows, and a main data store to grab
    movie reviews from.
    '''

    def __init__(self, main_datastore_proxy: MainDatastoreProxy):
        self.main_datastore_proxy = main_datastore_proxy

    def _build_average_vector(self, author_vectors: Dict[str, float], dim: int):
        average_vector = []
        author_count = len(author_vectors.keys())
        for index in range(dim):
            rating_sum = sum([author_vector[index]
                             for _, author_vector in author_vectors.items()])
            rating_average = rating_sum / author_count
            average_vector.append(rating_average)
        return average_vector

    def _build_vector_for_author(self, author: str, movie_indices: Dict[str, int], dim: int):
        author_vector = [0.0] * dim
        reviews_by_author = self.main_datastore_proxy.get(author)
        for review in reviews_by_author:
            if review.movie in movie_indices:
                author_vector[movie_indices[review.movie]] = review.rating
        return author_vector
    
    def _build_vectors(self, authors: List[str], movie_indices: Dict[str, int], dim: int):
        author_vectors = dict()
        for author in authors:
            author_vector = self._build_vector_for_author(author, movie_indices, dim)
            author_vectors[author] = author_vector
        return author_vectors

    def build_vectors(self, popular_movies: Set[str], authors: List[str]) -> Tuple[Dict[str, List[float]], Dict[str, int]]:
        movie_indices = dict()
        for index, movie in enumerate(popular_movies):
            movie_indices[movie] = index

        dim = len(popular_movies)
        author_vectors = self._build_vectors(authors, movie_indices, dim)
        author_vectors["_average"] = self._build_average_vector(
            author_vectors, dim)

        return (author_vectors, movie_indices)
