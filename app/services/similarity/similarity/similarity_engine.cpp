#include "app/services/similarity/similarity/similarity_engine.h"

std::unique_ptr<SimilarityEngine> SimilarityEngine::create(
    std::shared_ptr<ProjectionDatastoreClient> datastore) {
  std::vector<SimilarityShard> compute_shards;

  int shard_count = datastore->getShardCount();

  // TODO we can do this in parallel
  for (int i = 0; i < shard_count; i++) {
    auto projection = datastore->getShardProjection(i);
    auto compute_shard = SimilarityShard::create(projection);
    compute_shards.push_back(compute_shard);
  }

  return std::make_unique<SimilarityEngine>(std::move(compute_shards));
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

  // TODO parallelize this loop
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