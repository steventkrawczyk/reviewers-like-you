from app.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.projection.projection_datastore_proxy import ProjectionDatastoreProxy
from app.recommendation.match_generator import MatchGenerator
from app.recommendation.similarity_engine import SimilarityEngine


class MatchGeneratorFactory:
    '''
    Factory class for MatchGenerator.
    '''

    def __init__(self, main_datastore: MainDatastoreProxy, projection_datastore: ProjectionDatastoreProxy):
        self.main_datastore = main_datastore
        self.projection_datastore = projection_datastore

    def build(self) -> MatchGenerator:
        vectors = []
        author_by_index = dict()
        index = 0
        average_vec = []
        for author, vector in self.projection_datastore.get().items():
            if author == "_average":
                average_vec = vector
            else:
                author_by_index[index] = author
                index += 1
                vectors.append(vector)
        similarity_engine = SimilarityEngine(vectors)
        return MatchGenerator(self.main_datastore, similarity_engine,
                              self.projection_datastore.get_movie_indices(),
                              author_by_index, average_vec)
