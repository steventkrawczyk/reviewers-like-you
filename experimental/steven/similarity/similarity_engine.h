#include <vector>

#include "similarity_shard.h"

class SimilarityEngine {
  public:
    SimilarityEngine(std::unique_ptr<std::vector<SimilarityShard>>&& shards);

    std::vector<float> findAverageVector();

    std::string getClosestNeighbor(std::vector<float> input_vector);
  private:
    std::unique_ptr<std::vector<SimilarityShard>> shards;
};