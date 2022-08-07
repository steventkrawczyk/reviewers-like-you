#include <iostream>
#include <map>
#include <string>

class ProjectionFileStore {
 public:
  ProjectionFileStore(std::string endpoint_url, std::string bucket_name);

  void makeBucketIfItDoesntExist();

  bool objectExists(std::string name);

  std::map<std::string, int> getMovieIndices(std::string name);

  std::map<std::string, std::vector<float>> getProjection(std::string name);

  void putMovieIndices(std::string name,
                       std::map<std::string, int> movie_indices);

  void putProjection(std::string name,
                     std::map<std::string, std::vector<float>> projection);

 private:
  std::string bucket_name;
};
