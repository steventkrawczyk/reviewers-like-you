#include <map>
#include <string>
#include <vector>

#include "app/services/projection_datastore/projection/backend/projection_backend.h"

// This class is responsible for storing a chunk of projection data. It takes
// orders from the head.
class ProjectionDatastoreShard {
 public:
  ProjectionDatastoreShard(std::shared_ptr<ProjectionBackend> backend,
                           std::string projection_filepath);

  void upload(std::map<std::string, std::vector<float>> projection);

  void append(std::map<std::string, std::vector<float>> projection);

  void loadData();

  std::map<std::string, std::vector<float>> getAll();

  std::vector<float> get(std::string author_name);

  int size();

 private:
  std::shared_ptr<ProjectionBackend> backend;
  // TODO guard this with a mutex 
  std::map<std::string, std::vector<float>> projection;
  std::string projection_filepath;

  void cacheData(std::map<std::string, std::vector<float>> projection);

  void appendData(std::map<std::string, std::vector<float>> projection);

  void saveData();

  void loadProjection();
};