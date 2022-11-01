#include "app/services/partition/partition/partition_engine.h"

std::unique_ptr<PartitionEngine> PartitionEngine::create(
    std::shared_ptr<ProjectionDatastoreClient> datastore) {
  std::vector<PartitionShard> compute_shards;

  int shard_count = datastore->getShardCount();
  for (int i = 0; i < shard_count; i++) {
    auto projection = datastore->getShardProjection(i);
    auto compute_shard = PartitionShard::create(projection);
    compute_shards.push_back(compute_shard);
  }

  return std::make_unique<PartitionEngine>(std::move(compute_shards));
}