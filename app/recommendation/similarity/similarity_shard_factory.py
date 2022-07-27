from app.projection.datastore.projection_datastore_shard import ProjectionDatastoreShard
from app.recommendation.similarity.similarity_shard import SimilarityShard


class SimilarityShardFactory:
    '''
    Factory for SimilarityShard. Responsible for building vector space
    and author index, and finding the average vector.
    '''

    def __init__(self, data_shard: ProjectionDatastoreShard):
        self.data_shard = data_shard

    def build(self):
        vectors = []
        author_by_index = dict()
        index = 0
        average_vec = None
        for author, vector in self.data_shard.get_all().items():
            if author == "_average":
                average_vec = vector
            else:
                author_by_index[index] = author
                index += 1
                vectors.append(vector)

        return SimilarityShard(vectors, author_by_index, average_vec)
