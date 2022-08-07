#include "projection_datastore_proxy.h"

std::unique_ptr<ProjectionDatastoreProxy> ProjectionDatastoreProxy::create(
    ProjectionFileStore file_store, std::string projection_filepath_root,
    std::string movie_indices_filepath) {
  auto datastore = ProjectionDatastoreProxy(
      file_store, projection_filepath_root, movie_indices_filepath, SHARD_SIZE);
  datastore.loadData();
  return std::make_unique<ProjectionDatastoreProxy>(datastore);
}

ProjectionDatastoreProxy::ProjectionDatastoreProxy(
    ProjectionFileStore file_store, std::string projection_filepath_root,
    std::string movie_indices_filepath, int shard_size)
    : file_store(file_store),
      projection_filepath_root(projection_filepath_root),
      movie_indices_filepath(movie_indices_filepath),
      shard_size(shard_size),
      shard_count(0) {}

std::vector<ProjectionDatastoreShard>& ProjectionDatastoreProxy::getShards() {
  return this->shards;
}

std::map<std::string, int>& ProjectionDatastoreProxy::getMovieIndices() {
  return this->movie_indices;
}

void ProjectionDatastoreProxy::upload(
    std::map<std::string, std::vector<float>> projection,
    std::map<std::string, int> movie_indices) {
  this->saveData(movie_indices);
  this->cacheData(movie_indices);
  this->uploadToShards(projection);
}

void ProjectionDatastoreProxy::cacheData(
    std::map<std::string, int> movie_indices) {
  this->movie_indices = movie_indices;
}

std::string ProjectionDatastoreProxy::getShardFilepath(int shard_index) {
  return this->projection_filepath_root + std::to_string(shard_index) +
         std::string(".json");
}

void ProjectionDatastoreProxy::createNewShard() {
  int id = this->createShardId();
  std::string filepath = this->getShardFilepath(id);
  auto new_shard = ProjectionDatastoreShard(file_store, filepath);
  this->shards.push_back(new_shard);
}

int ProjectionDatastoreProxy::createShardId() { return shard_count++; }

// TODO this can be multithreaded, createNewShard uses an atomic counter to be
// thread safe.
void ProjectionDatastoreProxy::initializeShards() {
  this->shard_count = 0;
  this->shards = std::vector<ProjectionDatastoreShard>();
  while (this->shard_count < MAX_SHARDS &&
         this->file_store.objectExists(
             this->getShardFilepath(this->shard_count))) {
    this->createNewShard();
  }
}

void ProjectionDatastoreProxy::loadMovieIndices() {
  if (this->file_store.objectExists(this->movie_indices_filepath)) {
    this->movie_indices =
        this->file_store.getMovieIndices(this->movie_indices_filepath);
  }
}

void ProjectionDatastoreProxy::saveData(
    std::map<std::string, int> movie_indices) {
  this->file_store.putMovieIndices(this->movie_indices_filepath, movie_indices);
}

void ProjectionDatastoreProxy::loadData() {
  this->loadMovieIndices();
  this->initializeShards();
  for (auto& shard : this->shards) {
    shard.loadData();
  }
}

void ProjectionDatastoreProxy::uploadToShards(
    std::map<std::string, std::vector<float>> projection) {
  int projection_size = projection.size();
  int offset = 0;
  std::atomic<int> shard_index = 0;
  // TODO this can be done in parallel.
  while (offset < projection_size) {
    // Create a new shard if we need one
    if (shard_index == this->shard_count) {
      this->createNewShard();
    }

    std::map<std::string, std::vector<float>> projection_for_shard;
    int batch_size = std::min(this->shard_size, projection_size - offset);
    for (int batch_index = 0; batch_index < batch_size; batch_index++) {
      std::string author;
      std::vector<float> ratings;
      projection_for_shard[author] = ratings;
    }
    this->shards[shard_index++].upload(projection_for_shard);
    offset += batch_size;
  }
}