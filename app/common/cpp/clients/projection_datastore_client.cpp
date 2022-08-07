#include "app/common/cpp/clients/projection_datastore_client.h"

std::unique_ptr<ProjectionDatastoreHead> ProjectionDatastoreHead::create(
    std::shared_ptr<ProjectionFileStore> file_store,
    std::string projection_filepath_root, std::string movie_indices_filepath) {
  auto datastore = ProjectionDatastoreHead(file_store, projection_filepath_root,
                                           movie_indices_filepath, SHARD_SIZE);
  datastore.loadData();
  return std::make_unique<ProjectionDatastoreHead>(datastore);
}

ProjectionDatastoreHead::ProjectionDatastoreHead(
    std::shared_ptr<ProjectionFileStore> file_store,
    std::string projection_filepath_root, std::string movie_indices_filepath,
    int shard_size)
    : file_store(file_store),
      projection_filepath_root(projection_filepath_root),
      movie_indices_filepath(movie_indices_filepath),
      shard_size(shard_size),
      shard_count(0) {}

std::vector<ProjectionDatastoreShard>& ProjectionDatastoreHead::getShards() {
  return this->shards;
}

std::map<std::string, int>& ProjectionDatastoreHead::getMovieIndices() {
  return this->movie_indices;
}

void ProjectionDatastoreHead::upload(
    std::map<std::string, std::vector<float>> projection,
    std::map<std::string, int> movie_indices) {
  this->saveData(movie_indices);
  this->cacheData(movie_indices);
  this->resetShards();
  this->uploadToShards(projection);
}

void ProjectionDatastoreHead::append(
    std::map<std::string, std::vector<float>> projection) {
  this->uploadToShards(projection);
}

void ProjectionDatastoreHead::cacheData(
    std::map<std::string, int> movie_indices) {
  this->movie_indices = movie_indices;
}

std::string ProjectionDatastoreHead::getShardFilepath(int shard_index) {
  return this->projection_filepath_root + std::to_string(shard_index) +
         std::string(".json");
}

void ProjectionDatastoreHead::createNewShard() {
  int id = this->createShardId();
  std::string filepath = this->getShardFilepath(id);
  auto new_shard = ProjectionDatastoreShard(file_store, filepath);
  this->shards.push_back(new_shard);
}

int ProjectionDatastoreHead::createShardId() { return shard_count++; }

// TODO this can be multithreaded, createNewShard uses an atomic counter to be
// thread safe.
void ProjectionDatastoreHead::initializeShards() {
  std::lock_guard<std::mutex> guard(this->shards_mutex);
  this->shard_count = 0;
  this->shards = std::vector<ProjectionDatastoreShard>();
  while (this->shard_count < MAX_SHARDS &&
         this->file_store->objectExists(
             this->getShardFilepath(this->shard_count))) {
    this->createNewShard();
  }
}

void ProjectionDatastoreHead::loadMovieIndices() {
  if (this->file_store->objectExists(this->movie_indices_filepath)) {
    this->movie_indices =
        this->file_store->getMovieIndices(this->movie_indices_filepath);
  }
}

void ProjectionDatastoreHead::saveData(
    std::map<std::string, int> movie_indices) {
  this->file_store->putMovieIndices(this->movie_indices_filepath,
                                    movie_indices);
}

void ProjectionDatastoreHead::loadData() {
  this->loadMovieIndices();
  this->initializeShards();
  std::lock_guard<std::mutex> guard(this->shards_mutex);
  for (auto& shard : this->shards) {
    shard.loadData();
  }
}

void ProjectionDatastoreHead::uploadToShards(
    std::map<std::string, std::vector<float>> projection) {
  int projection_size = projection.size();
  int offset = 0;
  // TODO this can be done in parallel.
  std::lock_guard<std::mutex> guard(this->shards_mutex);
  while (offset < projection_size) {
    if (this->shard_count == 0 ||
        this->shards[this->shard_count - 1].size() >= this->shard_size) {
      this->createNewShard();
    }

    std::map<std::string, std::vector<float>> projection_for_shard;
    int batch_size = std::min(this->shard_size, projection_size - offset);
    for (int batch_index = 0; batch_index < batch_size; batch_index++) {
      std::string author;
      std::vector<float> ratings;
      projection_for_shard[author] = ratings;
    }
    this->shards[this->shard_count - 1].upload(projection_for_shard);
    offset += batch_size;
  }
}

void ProjectionDatastoreHead::resetShards() {
  std::lock_guard<std::mutex> guard(this->shards_mutex);
  this->shards = std::vector<ProjectionDatastoreShard>();
  this->shard_count = 0;
}