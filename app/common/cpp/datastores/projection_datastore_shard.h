#include <map>
#include <string>
#include <vector>

#include "app/common/cpp/clients/projection_file_client.h"

class ProjectionDatastoreShard {
 public:
  ProjectionDatastoreShard(std::shared_ptr<ProjectionFileClient> file_store,
                           std::string projection_filepath);

  void upload(std::map<std::string, std::vector<float>> projection);

  void loadData();

  std::map<std::string, std::vector<float>> getAll();

  std::vector<float> get(std::string author_name);

  int size();

 private:
  std::shared_ptr<ProjectionFileClient> file_store;
  std::map<std::string, std::vector<float>> projection;
  std::string projection_filepath;

  void cacheData(std::map<std::string, std::vector<float>> projection);

  void saveData(std::map<std::string, std::vector<float>> projection);

  void loadProjection();
};