#include "app/services/projection_datastore/projection/backend/projection_backend.h"

// TODO, here names refer to versions, and we have to construct the projection
// on the backend from the documents in that version. We may need to modify the
// datastore to be more agnostic about the structure of the name, e.g. move the
// name logic to the backend. Only issue would be shard numbering, but we can
// decouple shard id from name generation.
class ProjectionShardElasticsearchBackend : ProjectionElasticsearchBackendImpl {
  ProjectionObject getObject(std::string& name) override;
  void putObject(std::string& name, ProjectionObject& object) override;
  bool objectExists(std::string& name);
};