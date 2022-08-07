from app.common.python.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.common.python.projection.datastore.projection_datastore_proxy import ProjectionDatastoreProxy
from app.common.python.recommendation.movies_client import MoviesClient
from app.common.python.recommendation.similarity_client import SimilarityClient
from app.common.python.recommendation.similarity.similarity_engine_factory import SimilarityEngineFactory
from app.common.python.recommendation.similarity.in_memory_similarity_client import InMemorySimilarityClient
from app.common.python.recommendation.match_generator import MatchGenerator


class MatchGeneratorFactory:
    '''
    Factory class for MatchGenerator.
    '''

    def __init__(self, main_datastore: MainDatastoreProxy, projection_datastore: ProjectionDatastoreProxy = None, in_memory: bool = False):
        self.main_datastore = main_datastore
        self.projection_datastore = projection_datastore
        self.in_memory = in_memory

    def build(self):
        if self.in_memory:
            similarity_engine = SimilarityEngineFactory(
                self.projection_datastore).build()
            in_memory_similarity_client = InMemorySimilarityClient(
                similarity_engine)
            average_vec = similarity_engine.find_average_vector()
            return MatchGenerator(self.main_datastore, in_memory_similarity_client,
                                  self.projection_datastore.get_movie_indices(), average_vec)
        else:
            similarity_client = SimilarityClient()
            movies_client = MoviesClient()
            average_vec = similarity_client.find_average_vector()
            return MatchGenerator(self.main_datastore, similarity_client,
                                  movies_client.get_movie_indices(), average_vec)
