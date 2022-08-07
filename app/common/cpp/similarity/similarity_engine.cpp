#include "similarity_engine.h"

SimilarityEngine SimilarityEngine::create(ProjectionDatastoreHead& datastore) {
  std::vector<SimilarityShard> compute_shards;
  std::vector<ProjectionDatastoreShard> data_shards = datastore.getShards();

  for (auto& data_shard : data_shards) {
    auto compute_shard = SimilarityShard::create(data_shard);
    compute_shards.push_back(compute_shard);
  }

  return SimilarityEngine(std::move(compute_shards));
}

std::vector<float> SimilarityEngine::findAverageVector() {
  for (auto& shard : this->shards) {
    std::optional<std::vector<float>> response = shard.findAverageVector();
    if (response.has_value()) {
      return response.value();
    }
  }
  throw std::runtime_error("No average vector found");
  return std::vector<float>();
}

std::string SimilarityEngine::getClosestNeighbor(
    std::vector<float> input_vector) {
  std::vector<std::string> authors;
  std::vector<float> distances_from_shards;

  for (int i = 0; i < this->shards.size(); i++) {
    auto response = this->shards.at(i).getClosestNeighbor(input_vector);
    distances_from_shards.push_back(response.distance);
    authors.push_back(this->shards.at(i).decodeMatch(response.index).value());
  }

  auto min_distance_iterator = std::min_element(distances_from_shards.begin(),
                                                distances_from_shards.end());
  return authors[std::distance(distances_from_shards.begin(),
                               min_distance_iterator)];
}

SimilarityEngine::SimilarityEngine(std::vector<SimilarityShard>&& shards)
    : shards(std::move(shards)) {}