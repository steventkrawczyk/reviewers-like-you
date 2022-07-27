from app.ingestion.datastore.main_datastore_proxy import MainDatastoreProxy
from app.projection.datastore.projection_datastore_proxy import ProjectionDatastoreProxy
from app.recommendation.match_generator import MatchGenerator
from app.recommendation.similarity.similarity_engine_factory import SimilarityEngineFactory


class MatchGeneratorFactory:
    '''
    Factory class for MatchGenerator.
    '''

    def __init__(self, main_datastore: MainDatastoreProxy, projection_datastore: ProjectionDatastoreProxy):
        self.main_datastore = main_datastore
        self.projection_datastore = projection_datastore

    def build(self) -> MatchGenerator:
        similarity_engine = SimilarityEngineFactory(
            self.projection_datastore).build()
        average_vec = similarity_engine.find_average_vector()
        return MatchGenerator(self.main_datastore, similarity_engine,
                              self.projection_datastore.get_movie_indices(), average_vec)
