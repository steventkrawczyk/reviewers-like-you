#include <memory>

#include "app/common/cpp/clients/main_datastore_client.h"
#include "app/common/cpp/clients/projection_datastore_client.h"
#include "app/common/cpp/projection/popularity_analyzer.h"
#include "app/common/cpp/projection/projection_builder.h"

// This class orchestrates projection building
class ProjectionEngine {
 public:
  ProjectionEngine(
      std::shared_ptr<MainDatastoreClient> main_datastore,
      std::shared_ptr<ProjectionDatastoreClient> projection_datastore);

  void createProjection();

 private:
  std::shared_ptr<MainDatastoreClient> main_datastore;
  std::shared_ptr<ProjectionDatastoreClient> projection_datastore;
  std::unique_ptr<PopularityAnalyzer> popularity_analyzer;
  std::unique_ptr<ProjectionBuilder> projection_builder;
};
