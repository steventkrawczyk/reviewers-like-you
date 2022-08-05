#include <map>
#include <string>
#include <vector>

#include "projection_datastore_shard.h"

struct SimilarityShardRepsonse {
  int index;
  float distance;
};

#define AVERAGE_VECTOR_NAME "_average"

class SimilarityShard {
 public:
  static SimilarityShard create(ProjectionDatastoreShard& data_shard);

  SimilarityShardRepsonse getClosestNeighbor(std::vector<float> input_vector);

  std::optional<std::string> decodeMatch(int index_of_match);

  std::optional<std::vector<float>> findAverageVector();

  std::vector<float> getVector(int index);

 private:
  std::vector<std::vector<float>> vectors;
  std::map<int, std::string> author_index;
  std::optional<std::vector<float>> average_vector = std::nullopt;

  SimilarityShard(std::vector<std::vector<float>>&& vectors,
                  std::map<int, std::string>&& author_index,
                  std::optional<std::vector<float>>&& average_vector);

  inline float computeDistance(std::vector<float> v, std::vector<float> w);
};