from app.ingestion.main_datastore_proxy import MainDatastoreProxy
from app.projection.engine.popularity_analyzer import PopularityAnalyzer
from app.projection.engine.projection_builder import ProjectionBuilder
from app.projection.datastore.projection_datastore_proxy import ProjectionDatastoreProxy
from app.projection.engine.projection_engine import ProjectionEngine


class ProjectionEngineFactory:
    '''
    A factory class for ProjectionEngine.
    '''
    def __init__(self, main_datastore_proxy: MainDatastoreProxy,
                 projection_datastore_proxy: ProjectionDatastoreProxy):
        self.main_datastore_proxy = main_datastore_proxy
        self.projection_datastore_proxy = projection_datastore_proxy

    def build(self):
        popularity_analyzer = PopularityAnalyzer(self.main_datastore_proxy)
        projection_builder = ProjectionBuilder(self.main_datastore_proxy)
        return ProjectionEngine(self.main_datastore_proxy,
                                self.projection_datastore_proxy,
                                popularity_analyzer, projection_builder)
