#include "projection_datastore_shard.h"

ProjectionDatastoreShard::ProjectionDatastoreShard(
    ProjectionFileStore& file_store, std::string projection_filepath)
    : file_store(file_store), projection_filepath(projection_filepath) {}

void ProjectionDatastoreShard::upload(
    std::map<std::string, std::vector<float>> projection) {
  saveData(projection);
  cacheData(projection);
}

void ProjectionDatastoreShard::loadData() { this->loadProjection(); }

std::map<std::string, std::vector<float>> ProjectionDatastoreShard::getAll() {
  return projection;
}

std::vector<float> ProjectionDatastoreShard::get(std::string author_name) {
  return this->projection[author_name];
}

void ProjectionDatastoreShard::cacheData(
    std::map<std::string, std::vector<float>> projection) {
  this->projection = projection;
}

void ProjectionDatastoreShard::cacheData(
    std::map<std::string, std::vector<float>> projection) {
  this->projection = projection;
}

void ProjectionDatastoreShard::saveData(
    std::map<std::string, std::vector<float>> projection) {
  this->file_store.putProjection(this->projection_filepath, projection);
}

void ProjectionDatastoreShard::loadProjection() {
  if (this->file_store.objectExists(this->projection_filepath)) {
    this->projection =
        this->file_store.getProjection(this->projection_filepath);
  }
}
