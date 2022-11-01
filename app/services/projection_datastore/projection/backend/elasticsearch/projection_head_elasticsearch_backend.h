#include "app/services/projection_datastore/projection/backend/projection_backend.h"

class ProjectionHeadElasticsearchBackend : ProjectionElasticsearchBackendImpl {
  ProjectionObject getObject(std::string& name) override;
  void putObject(std::string& name, ProjectionObject& object) override;
  bool objectExists(std::string& name);
};