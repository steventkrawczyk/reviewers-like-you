#include "app/services/similarity/similarity/similarity_shard.h"

#include <math.h>

#include <limits>
#include <vector>

SimilarityShard SimilarityShard::create(
    std::map<std::string, std::vector<float>> projection) {
  std::vector<std::vector<float>> vectors;
  std::map<int, std::string> author_index;
  std::optional<std::vector<float>> average_vector = std::nullopt;

  int index = 0;
  for (auto projection_iterator = projection.begin();
       projection_iterator != projection.end(); projection_iterator++) {
    projection_iterator->first;
    projection_iterator->second;

    if (projection_iterator->first.compare(AVERAGE_VECTOR_NAME) == 0) {
      average_vector = projection_iterator->second;
    } else {
      author_index[index++] = projection_iterator->first;
      vectors.push_back(projection_iterator->second);
    }
  }

  return SimilarityShard(std::move(vectors), std::move(author_index),
                         std::move(average_vector));
}

SimilarityShardRepsonse SimilarityShard::getClosestNeighbor(
    std::vector<float> input_vector) {
  float current_min = std::numeric_limits<float>::max();
  float distance = 0;
  int index = 0;
  int nn_index = -1;
  size_t length = input_vector.size();

  for (auto& vec : this->vectors) {
    distance = this->computeDistance(input_vector, vec, length);
    if (distance < current_min) {
      nn_index = index;
      current_min = distance;
    }
    index++;
  }

  auto response = SimilarityShardRepsonse();
  response.distance = current_min;
  response.index = nn_index;
  return response;
}

std::optional<std::string> SimilarityShard::decodeMatch(int index_of_match) {
  if (!this->author_index.contains(index_of_match)) {
    return std::nullopt;
  }
  return this->author_index[index_of_match];
}

std::optional<std::vector<float>> SimilarityShard::findAverageVector() {
  return this->average_vector;
}

std::vector<float> SimilarityShard::getVector(int index) {
  return this->vectors[index];
}

SimilarityShard::SimilarityShard(
    std::vector<std::vector<float>>&& vectors,
    std::map<int, std::string>&& author_index,
    std::optional<std::vector<float>>&& average_vector)
    : vectors(std::move(vectors)),
      author_index(std::move(author_index)),
      average_vector(std::move(average_vector)) {}

inline float SimilarityShard::computeDistance(std::vector<float> v,
                                              std::vector<float> w,
                                              size_t length) {
  float sum = 0;
  for (int i = 0; i < length; i++) {
    sum += powf(v[i] - w[i], 2);
  }
  return sqrtf(sum);
}
