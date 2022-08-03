#include "projection_datastore_shard.h"

void ProjectionDatastoreShard::upload(std::map<std::string, std::vector<float>> projection) {
    if (!this->in_memory) {
        saveData(projection);
    }
    cacheData(projection);
}

void loadData();

std::map<std::string, std::vector<float>> ProjectionDatastoreShard::getAll() {
    return projection;
}

std::vector<float> ProjectionDatastoreShard::get(std::string author_name) {
    return this->projection[author_name];
}

void ProjectionDatastoreShard::cacheData(std::map<std::string, std::vector<float>> projection) {
    this->projection = projection;
}

