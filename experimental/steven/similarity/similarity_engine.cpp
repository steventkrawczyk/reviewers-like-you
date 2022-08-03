#include "similarity_engine.h"



SimilarityEngine::SimilarityEngine(std::unique_ptr<std::vector<SimilarityShard>>&& shards) {
    this->shards = std::move(shards);
}

std::vector<float> SimilarityEngine::findAverageVector() {
    for (auto& shard : *(this->shards)) {
        std::optional<std::vector<float>> response = shard.findAverageVector();
        if (response.has_value()) {
            return response.value();
        }
    }
    throw std::runtime_error("No average vector found");
    return std::vector<float>();
}

std::string SimilarityEngine::getClosestNeighbor(std::vector<float> input_vector) {

}

//     def get_closest_neighbor(self, input_vector: List[float]) -> str:
//         distances_from_shards = []
//         author_index = dict()
//         for shard_index, shard in enumerate(self.shards):
//             nn_index_from_shard, distance_from_shard = shard.get_closest_neighbor(input_vector)
//             distances_from_shards.append(distance_from_shard)
//             author_index[shard_index] = shard.decode_match(nn_index_from_shard)
//         nn_index = SimilarityComputation.driver_computation(distances_from_shards)
//         return author_index[nn_index]


