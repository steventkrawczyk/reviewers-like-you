#include "similarity_shard_factory.h"

#include <vector>

SimilarityShardFactory::SimilarityShardFactory(std::unique_ptr<ProjectionDatastoreShard>&& data_shard) {
    this->data_shard = std::move(data_shard);
}


SimilarityShard SimilarityShardFactory::build() {
    std::vector<std::vector<float>> vectors;
    std::map<int, std::string> author_index;
    std::optional<std::vector<float>> average_vector = std::nullopt;
    std::map<std::string, std::vector<float>> projection = data_shard->getAll();

    int index = 0;
    for (auto projection_iterator = projection.begin(); 
         projection_iterator != projection.end(); projection_iterator++) {
        projection_iterator->first;
        projection_iterator->second;

        if (projection_iterator->first.compare(average_vector_name)) {
            average_vector = projection_iterator->second;
        } else {
            author_index[index++] = projection_iterator->first;
            vectors.push_back(projection_iterator->second);
        }
    }

    return SimilarityShard(vectors, author_index, average_vector);
}