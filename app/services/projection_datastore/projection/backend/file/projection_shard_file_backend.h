#include "app/services/projection_datastore/projection/backend/projection_backend.h"

class ProjectionShardFileBackend : ProjectionFileBackendImpl {
  ProjectionObject getObject(std::string& name) override;
  void putObject(std::string& name, ProjectionObject& object) override;
};