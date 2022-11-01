#include <memory>
#include <vector>

#include "app/common/cpp/clients/projection_datastore_client.h"
#include "app/services/similarity/similarity/similarity_shard.h"

class SimilarityEngine {
 public:
  static std::unique_ptr<SimilarityEngine> create(
      std::shared_ptr<ProjectionDatastoreClient> datastore);

  std::vector<float> findAverageVector();

  std::string getClosestNeighbor(std::vector<float> input_vector);

 private:
  std::vector<SimilarityShard> shards;

  SimilarityEngine(std::vector<SimilarityShard>&& shards);
};
