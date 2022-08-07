#include <vector>

#include "projection_datastore_head.h"
#include "similarity_shard.h"

class SimilarityEngine {
 public:
  static SimilarityEngine create(ProjectionDatastoreHead& datastore);

  std::vector<float> findAverageVector();

  std::string getClosestNeighbor(std::vector<float> input_vector);

 private:
  std::vector<SimilarityShard> shards;

  SimilarityEngine(std::vector<SimilarityShard>&& shards);
};
