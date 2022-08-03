#include "similarity_shard.h" 
#include <limits>
#include <vector>

 
SimilarityShard::SimilarityShard(std::vector<std::vector<float>> vectors, 
                                 std::map<int, std::string> author_index, 
                                 std::optional<std::vector<float>> average_vector) {
    this->vectors = vectors;
    this->author_index = author_index;
    this->average_vector = average_vector;
}

SimilarityShardRepsonse SimilarityShard::getClosestNeighbor(std::vector<float> input_vector) {
    float current_min = std::numeric_limits<float>::max();
    float distance = 0;
    int index = 0;
    int nn_index = -1;

    for(auto& vec : this->vectors) {
        distance = this->computeDistance(input_vector, vec);
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

template <class T>
inline T SimilarityShard::computeDistance(std::vector<T> v, std::vector<T> w) {
    size_t length = v.size();
    T sum = 0;
    for (int i = 0; i < length; i++) {
        sum += pow(v[i] - w[i], 2)
    }
    return sqrt(sum)
}
