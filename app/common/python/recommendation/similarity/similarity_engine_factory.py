from app.common.python.projection.datastore.projection_datastore_proxy import ProjectionDatastoreProxy
from app.common.python.recommendation.similarity.similarity_engine import SimilarityEngine
from app.common.python.recommendation.similarity.similarity_shard_factory import SimilarityShardFactory


class SimilarityEngineFactory:
    '''
    Factory class for SimilarityEngine. 
    '''

    def __init__(self, projection_datastore: ProjectionDatastoreProxy):
        self.projection_datastore = projection_datastore
        self.average_vec = []

    def build(self):
        compute_shards = []
        data_shards = self.projection_datastore.get_shards()
        for data_shard in data_shards:
            compute_shard = SimilarityShardFactory(data_shard).build()
            compute_shards.append(compute_shard)
        return SimilarityEngine(compute_shards)
