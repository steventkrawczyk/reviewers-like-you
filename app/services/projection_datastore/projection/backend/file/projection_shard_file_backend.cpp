#include "app/services/projection_datastore/projection/backend/file/projection_shard_file_backend.h"

ProjectionObject ProjectionShardFileBackend::getObject(std::string& name) {
  auto response = this->client.getObject(name);

  std::map<std::string, std::vector<float>> projection;
  if (response.found()) {
    std::string serialized_response = response.data();
    proto::Projection projection_pb;
    projection_pb.ParseFromString(serialized_response);
    projection = this->marshaller.protoToProjection(projection_pb);
  }

  return ShardProjectionObject(projection);
}

void ProjectionShardFileBackend::putObject(std::string& name,
                                           ProjectionObject& object) {
  auto unwrapped_object = static_cast<ShardProjectionObject&>(object).get();

  proto::Projection projection_pb =
      this->marshaller.projectionToProto(unwrapped_object, this->version);
  std::string serialized_projection;
  projection_pb.SerializeToString(&serialized_projection);

  proto::UploadObjectRequest request;
  request.set_allocated_objectname(&name);
  request.set_allocated_serializedobject(&serialized_projection);

  this->client.putObject(request);
}