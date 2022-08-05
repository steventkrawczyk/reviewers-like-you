#include <map>
#include <string>

#include "projection_datastore_shard.h"
#include "projection_file_store.h"

#define MAX_SHARDS 20
#define SHARD_SIZE 25

class ProjectionDatastoreProxy {
 public:
  static std::unique_ptr<ProjectionDatastoreProxy> create(
      ProjectionFileStore file_store, std::string projection_filepath_root,
      std::string movie_indices_filepath);

  // TODO append vs overwrite projection data. Eventually we will need to chunk
  // it out
  void upload(std::map<std::string, std::vector<float>> projection,
              std::map<std::string, int> movie_indices);

  std::vector<ProjectionDatastoreShard>& getShards();

  std::map<std::string, int>& getMovieIndices();

 private:
  ProjectionFileStore file_store;
  std::string projection_filepath_root;
  std::string movie_indices_filepath;
  int shard_size;
  std::vector<ProjectionDatastoreShard> shards;
  std::map<std::string, int> movie_indices;
  std::atomic<int> shard_count;

  ProjectionDatastoreProxy(ProjectionFileStore file_store,
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
};
