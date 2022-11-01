#include <string>

#include "app/common/cpp/clients/projection_datastore_client.h"

// This factory will be used to create multiple partition engines for different
// versions. If we don't set the version, the most recent version will be used.
class PartitionEngineFactory {
 public:
  PartitionEngineFactory(std::string endpoint_url);
  void setVersion(std::string version);
  void build();

 private:
  std::shared_ptr<ProjectionDatastoreClient> datastore;
  std::optional<std::string> version;
  std::string endpoint_url;
};