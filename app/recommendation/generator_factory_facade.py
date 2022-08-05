from app.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.projection.datastore.projection_datastore_proxy import ProjectionDatastoreProxy
from app.recommendation.in_memory_match_generator_factory import InMemoryMatchGeneratorFactory
from app.recommendation.match_generator_factory import MatchGeneratorFactory


class GeneratorFactoryFacade:
    '''
    Factory class for MatchGenerator.
    '''

    def __init__(self, main_datastore: MainDatastoreProxy, projection_datastore: ProjectionDatastoreProxy = None, in_memory: bool = False):
        self.main_datastore = main_datastore
        self.projection_datastore = projection_datastore
        self.in_memory = in_memory

    def build(self):
        if self.in_memory:
            return InMemoryMatchGeneratorFactory(self.main_datastore, self.projection_datastore).build()
        else:
            return MatchGeneratorFactory(self.main_datastore).build()