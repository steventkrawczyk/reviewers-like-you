#include <map>
#include <string>

#include "app/services/projection_datastore/projection/backend/projection_backend.h"
#include "app/services/projection_datastore/projection/datastore/projection_datastore_shard.h"

#define MAX_SHARDS 20
#define SHARD_SIZE 25

// This class is responsible for passthrough to shards, shard management, and
// for storing the movie indices.
class ProjectionDatastoreHead {
 public:
  static std::unique_ptr<ProjectionDatastoreHead> create(
      std::shared_ptr<ProjectionBackend> backend,
      std::shared_ptr<NameUtility> name_utility);

  void upload(std::map<std::string, std::vector<float>> projection,
              std::map<std::string, int> movie_indices);

  void append(std::map<std::string, std::vector<float>> projection);

  std::vector<ProjectionDatastoreShard>& getShards();

  std::map<std::string, std::vector<float>> getShardProjection(int shard_id);

  std::map<std::string, int>& getMovieIndices();

  int getShardCount();

 private:
  std::shared_ptr<ProjectionBackend> backend;
  std::map<std::string, int> movie_indices;
  std::atomic<int> shard_count;
  std::vector<ProjectionDatastoreShard> shards;
  std::mutex shards_mutex;
  std::shared_ptr<NameUtility> name_utility;
  int shard_size;

  ProjectionDatastoreHead(std::shared_ptr<ProjectionBackend> backend,
                          std::shared_ptr<NameUtility> name_utility,
                          int shard_size);

  void initializeShards();

  void loadMovieIndices();

  void createNewShard();

  void loadData();

  void cacheData(std::map<std::string, int> movie_indices);

  void saveData();

  void uploadToShards(std::map<std::string, std::vector<float>> projection);

  int createShardId();

  void resetShards();
};
