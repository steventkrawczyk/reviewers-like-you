#include "app/services/projection_datastore/projection/datastore/projection_datastore_shard.h"

ProjectionDatastoreShard::ProjectionDatastoreShard(
    std::shared_ptr<ProjectionBackend> backend, std::string projection_filepath)
    : backend(backend), projection_filepath(projection_filepath) {}

void ProjectionDatastoreShard::upload(
    std::map<std::string, std::vector<float>> projection) {
  cacheData(projection);
  saveData();
}

void ProjectionDatastoreShard::append(
    std::map<std::string, std::vector<float>> projection) {
  appendData(projection);
  saveData();
}

void ProjectionDatastoreShard::loadData() { this->loadProjection(); }

std::map<std::string, std::vector<float>> ProjectionDatastoreShard::getAll() {
  return projection;
}

std::vector<float> ProjectionDatastoreShard::get(std::string author_name) {
  return this->projection[author_name];
}

int ProjectionDatastoreShard::size() { return this->projection.size(); }

void ProjectionDatastoreShard::cacheData(
    std::map<std::string, std::vector<float>> projection) {
  this->projection = projection;
}

void ProjectionDatastoreShard::appendData(
    std::map<std::string, std::vector<float>> projection) {
  this->projection.insert(projection.begin(), projection.end());
}

void ProjectionDatastoreShard::saveData() {
  auto wrapped_object = ShardProjectionObject(this->projection);
  this->backend->putObject(this->projection_filepath, wrapped_object);
}

void ProjectionDatastoreShard::loadProjection() {
  auto wrapped_object = this->backend->getObject(this->projection_filepath);
  auto unwrapped_object =
      static_cast<ShardProjectionObject&>(wrapped_object).get();
  if (unwrapped_object.size() > 0) {
    this->projection = unwrapped_object;
  }
}
