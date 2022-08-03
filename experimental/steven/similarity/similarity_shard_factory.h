#include <memory>

#include "projection_datastore_shard.h"
#include "similarity_shard.h"

class SimilarityShardFactory {
  public:
    SimilarityShardFactory(std::unique_ptr<ProjectionDatastoreShard>&& data_shard);
    SimilarityShard build();

  private:
    std::unique_ptr<ProjectionDatastoreShard> data_shard;
    const std::string average_vector_name = "_average";
};