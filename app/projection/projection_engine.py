'''
This class is used to download data from the main datastore and create
a projection of popular movies to use for similarity computations.
'''
import math
from typing import Dict, List, Set, Tuple

from app.main_datastore.main_datastore_proxy import MainDatastoreProxy
from app.projection.projection_datastore_proxy import ProjectionDatastoreProxy


class ProjectionEngine:
    def __init__(self, main_datastore_proxy: MainDatastoreProxy, projection_datastore_proxy: ProjectionDatastoreProxy):
        self.main_datastore_proxy = main_datastore_proxy
        self.authors = list(self.main_datastore_proxy.get_keys())
        self.projection_datastore_proxy = projection_datastore_proxy

    def create_projection(self) -> None:
        popular_movies = self.compute_popular_movies()
        author_vectors, movie_indices = self.build_vectors(popular_movies)
        self.store_projection(author_vectors, movie_indices)

    def compute_popular_movies(self) -> Set[str]:
        popular_movies = set()

        # Idea: popular movies are ones that every reviewer has
        # reviewed.
        for author in self.authors:
            # TODO optimize main data store calls
            reviews_by_author = self.main_datastore_proxy.get(author)
            movies_by_author = set()
            for movie, rating in reviews_by_author:
                if not math.isnan(float(rating)):
                    movies_by_author.add(movie)
            if not popular_movies:
                popular_movies = movies_by_author
            popular_movies = popular_movies.intersection(movies_by_author)

        return popular_movies

    def build_vectors(self, popular_movies: Set[str]) -> Tuple[Dict[str, List[float]], Dict[str, int]]:
        movie_indices = dict()
        for index, movie in enumerate(popular_movies):
            movie_indices[movie] = index

        author_vectors = dict()
        dim = len(popular_movies)

        for author in self.authors:
            author_vector = [0.0] * dim
            # TODO optimize main data store calls
            reviews_by_author = self.main_datastore_proxy.get(author)
            for movie, rating in reviews_by_author:
                if movie in movie_indices:
                    author_vector[movie_indices[movie]] = float(rating)
            author_vectors[author] = author_vector

        return (author_vectors, movie_indices)

    def store_projection(self, author_vectors: Dict[str, List[float]], movie_indices: Dict[str, int]) -> None:
        self.projection_datastore_proxy.upload(author_vectors, movie_indices)
