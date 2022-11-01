#include <string>

#include "app/common/cpp/clients/projection_file_client.h"
#include "app/common/cpp/marshaller/data_marshaller.h"

class ProjectionObject {};

class HeadProjectionObject : public ProjectionObject {
 public:
  HeadProjectionObject(std::map<std::string, int> movie_indices)
      : movie_indices(movie_indices) {}
  std::map<std::string, int>& get() { return movie_indices; }

 private:
  std::map<std::string, int> movie_indices;
};

class ShardProjectionObject : public ProjectionObject {
 public:
  ShardProjectionObject(std::map<std::string, std::vector<float>> projection)
      : projection(projection) {}
  std::map<std::string, std::vector<float>>& get() { return projection; }

 private:
  std::map<std::string, std::vector<float>> projection;
};

class ProjectionBackend {
 public:
  virtual ProjectionObject getObject(std::string& name) = 0;
  virtual void putObject(std::string& name, ProjectionObject& object) = 0;
  virtual bool objectExists(std::string& name) = 0;
};

class ProjectionFileBackendImpl : ProjectionBackend {
 public:
  ProjectionFileBackendImpl(std::string& endpoint_url, std::string& bucket_name,
                            std::string version)
      : client(ProjectionFileClient(endpoint_url, bucket_name)) {}
  bool objectExists(std::string& name) override {
    return this->client.objectExists(name);
  }

 protected:
  ProjectionFileClient client;
  DataMarshaller marshaller;
  std::string version;
};

class ProjectionElasticsearchBackendImpl : ProjectionBackend {};

class NameUtility {
 public:
  virtual std::string getShardDocumentName(int shard_index) = 0;
  virtual std::string getMovieIndicesDocumentName() = 0;
};