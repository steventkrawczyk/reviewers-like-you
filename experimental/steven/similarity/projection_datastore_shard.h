#include <map>
#include <string>
#include <vector>

class ProjectionDatastoreShard {
  public:
    ProjectionDatastoreShard();

    void upload(std::map<std::string, std::vector<float>> projection);

    void loadData();

    std::map<std::string, std::vector<float>> getAll();

    std::vector<float> get(std::string author_name);

  private:
    std::map<std::string, std::vector<float>> projection;
    bool in_memory = false;

    void cacheData(std::map<std::string, std::vector<float>> projection);

    void saveData(std::map<std::string, std::vector<float>> projection);

    void loadProjection();
};