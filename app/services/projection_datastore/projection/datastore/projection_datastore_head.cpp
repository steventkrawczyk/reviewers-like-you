#include "app/services/projection_datastore/projection/datastore/projection_datastore_head.h"

std::unique_ptr<ProjectionDatastoreHead> ProjectionDatastoreHead::create(
    std::shared_ptr<ProjectionBackend> backend,
    std::shared_ptr<NameUtility> name_utility) {
  auto datastore = ProjectionDatastoreHead(backend, name_utility, SHARD_SIZE);
  datastore.loadData();
  return std::make_unique<ProjectionDatastoreHead>(datastore);
}

ProjectionDatastoreHead::ProjectionDatastoreHead(
    std::shared_ptr<ProjectionBackend> backend,
    std::shared_ptr<NameUtility> name_utility, int shard_size)
    : backend(backend),
      name_utility(name_utility),
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
  this->cacheData(movie_indices);
  this->saveData();
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

void ProjectionDatastoreHead::createNewShard() {
  int id = this->createShardId();
  std::string document_name = this->name_utility->getShardDocumentName(id);
  auto new_shard = ProjectionDatastoreShard(backend, document_name);
  this->shards.push_back(new_shard);
}

int ProjectionDatastoreHead::createShardId() { return shard_count++; }

// TODO this can be multithreaded, createNewShard uses an atomic counter to be
// thread safe.
void ProjectionDatastoreHead::initializeShards() {
  std::lock_guard<std::mutex> guard(this->shards_mutex);
  this->shard_count = 0;
  this->shards = std::vector<ProjectionDatastoreShard>();
  std::string document_name =
      this->name_utility->getShardDocumentName(this->shard_count);
  while (this->shard_count < MAX_SHARDS &&
         this->backend->objectExists(document_name)) {
    this->createNewShard();
  }
}

void ProjectionDatastoreHead::loadMovieIndices() {
  std::string document_name = this->name_utility->getMovieIndicesDocumentName();
  auto wrapped_object = this->backend->getObject(document_name);
  auto unwrapped_object =
      static_cast<HeadProjectionObject&>(wrapped_object).get();
  if (unwrapped_object.size() > 0) {
    this->movie_indices = unwrapped_object;
  }
}

void ProjectionDatastoreHead::saveData() {
  std::string document_name = this->name_utility->getMovieIndicesDocumentName();
  auto wrapped_object = HeadProjectionObject(this->movie_indices);
  this->backend->putObject(document_name, wrapped_object);
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
    this->shards[this->shard_count - 1].append(projection_for_shard);
    offset += batch_size;
  }
}

void ProjectionDatastoreHead::resetShards() {
  std::lock_guard<std::mutex> guard(this->shards_mutex);
  this->shards = std::vector<ProjectionDatastoreShard>();
  this->shard_count = 0;
}

std::map<std::string, std::vector<float>>
ProjectionDatastoreHead::getShardProjection(int shard_id) {
  return this->shards[shard_id].getAll();
}

int ProjectionDatastoreHead::getShardCount() { return this->shard_count; }