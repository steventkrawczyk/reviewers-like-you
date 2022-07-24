'''
This class is used to download data from the main datastore and create
a projection of popular movies to use for similarity computations.
'''
from typing import Dict, List

from app.main_datastore.main_datastore_proxy import MainDatastoreProxy
from app.projection.popularity_analyzer import PopularityAnalyzer
from app.projection.projection_builder import ProjectionBuilder
from app.projection.projection_datastore_proxy import ProjectionDatastoreProxy


class ProjectionEngine:
    def __init__(self, main_datastore_proxy: MainDatastoreProxy,
                 projection_datastore_proxy: ProjectionDatastoreProxy):
        self.main_datastore_proxy = main_datastore_proxy
        self.projection_datastore_proxy = projection_datastore_proxy
        self.popularity_analyzer = PopularityAnalyzer(self.main_datastore_proxy)
        self.projection_builder = ProjectionBuilder(self.main_datastore_proxy)

    def _store_projection(self, author_vectors: Dict[str, List[float]], movie_indices: Dict[str, int]) -> None:
        self.projection_datastore_proxy.upload(author_vectors, movie_indices)

    def create_projection(self) -> None:
        self.authors = list(self.main_datastore_proxy.get_keys())
        popular_movies = self.popularity_analyzer.compute_popular_movies(self.authors)
        author_vectors, movie_indices = self.projection_builder.build_vectors(popular_movies, self.authors)
        self._store_projection(author_vectors, movie_indices)
