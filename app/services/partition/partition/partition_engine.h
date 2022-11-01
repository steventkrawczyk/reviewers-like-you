#include <memory>
#include <vector>

#include "app/common/cpp/clients/projection_datastore_client.h"
#include "app/services/partition/partition/partition_shard.h"

class PartitionEngine {
 public:
  static std::unique_ptr<PartitionEngine> create(
      std::shared_ptr<ProjectionDatastoreClient> datastore);

  // Returns k-means, and stores the corresponding partitions. Paritions can get
  // looked up by index.
  std::vector<std::vector<float>> buildPartitions();

  // Use given "means", e.g. authors, for clustering. Does not return
  // means, but stores partitions in memory to be looked up.
  void buildPartitions(std::vector<std::vector<float>> means);

  std::vector<std::vector<float>> getPartition(int index);

  int getPartitionCount();

 private:
  std::vector<PartitionShard> partitions;
  std::vector<std::vector<float>> givenMeans;

  PartitionEngine(std::vector<PartitionShard>&& shards);
};
