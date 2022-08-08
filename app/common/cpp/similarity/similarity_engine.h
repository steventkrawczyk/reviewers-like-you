#include <vector>

#include "app/common/cpp/clients/projection_datastore_client.h"
#include "app/common/cpp/similarity/similarity_shard.h"

class SimilarityEngine {
 public:
  static SimilarityEngine create(
      std::shared_ptr<ProjectionDatastoreClient> datastore);

  std::vector<float> findAverageVector();

  std::string getClosestNeighbor(std::vector<float> input_vector);

 private:
  std::vector<SimilarityShard> shards;

  SimilarityEngine(std::vector<SimilarityShard>&& shards);
};
