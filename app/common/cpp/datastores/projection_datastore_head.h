#include <map>
#include <string>

#include "app/common/cpp/clients/projection_file_client.h"
#include "app/common/cpp/datastores/projection_datastore_shard.h"

#define MAX_SHARDS 20
#define SHARD_SIZE 25

class ProjectionDatastoreHead {
 public:
  static std::unique_ptr<ProjectionDatastoreHead> create(
      std::shared_ptr<ProjectionFileClient> file_store,
      std::string projection_filepath_root, std::string movie_indices_filepath);

  void upload(std::map<std::string, std::vector<float>> projection,
              std::map<std::string, int> movie_indices);

  void append(std::map<std::string, std::vector<float>> projection);

  std::vector<ProjectionDatastoreShard>& getShards();

  std::map<std::string, int>& getMovieIndices();

 private:
  std::shared_ptr<ProjectionFileClient> file_store;
  std::string projection_filepath_root;
  std::string movie_indices_filepath;
  int shard_size;
  std::map<std::string, int> movie_indices;
  std::atomic<int> shard_count;
  std::vector<ProjectionDatastoreShard> shards;
  std::mutex shards_mutex;

  ProjectionDatastoreHead(std::shared_ptr<ProjectionFileClient> file_store,
                          std::string projection_filepath_root,
                          std::string movie_indices_filepath, int shard_size);

  void initializeShards();

  void loadMovieIndices();

  void createNewShard();

  void loadData();

  void cacheData(std::map<std::string, int> movie_indices);

  void saveData(std::map<std::string, int> movie_indices);

  void uploadToShards(std::map<std::string, std::vector<float>> projection);

  std::string getShardFilepath(int shard_index);

  int createShardId();

  void resetShards();
};
