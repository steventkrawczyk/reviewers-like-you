#include <map>
#include <string>
#include <vector>

#include "projection_file_store.h"

class ProjectionDatastoreShard {
 public:
  ProjectionDatastoreShard(ProjectionFileStore& file_store,
                           std::string projection_filepath);

  void upload(std::map<std::string, std::vector<float>> projection);

  void loadData();

  std::map<std::string, std::vector<float>> getAll();

  std::vector<float> get(std::string author_name);

 private:
  ProjectionFileStore& file_store;
  std::map<std::string, std::vector<float>> projection;
  std::string projection_filepath;

  void cacheData(std::map<std::string, std::vector<float>> projection);

  void saveData(std::map<std::string, std::vector<float>> projection);

  void loadProjection();
};