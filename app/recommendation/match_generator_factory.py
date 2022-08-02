from app.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.recommendation.match_generator import MatchGenerator
from app.recommendation.movies_client import MoviesClient
from app.recommendation.similarity.similarity_client import SimilarityClient


class MatchGeneratorFactory:
    '''
    Factory class for MatchGenerator.
    '''

    def __init__(self, main_datastore: MainDatastoreProxy):
        self.main_datastore = main_datastore
        self.similarity_client = SimilarityClient()
        self.movies_client = MoviesClient()

    def build(self) -> MatchGenerator:
        average_vec = self.similarity_client.find_average_vector()
        return MatchGenerator(self.main_datastore, self.similarity_client,
                              self.movies_client.get_movie_indices(), average_vec)
