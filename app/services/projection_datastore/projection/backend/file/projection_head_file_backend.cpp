#include "app/services/projection_datastore/projection/backend/file/projection_head_file_backend.h"

ProjectionObject ProjectionHeadFileBackend::getObject(std::string& name) {
  auto response = this->client.getObject(name);

  std::map<std::string, int> movie_indices;
  if (response.found()) {
    std::string serialized_response = response.data();
    proto::MovieIndices movie_indices_pb;
    movie_indices_pb.ParseFromString(serialized_response);
    movie_indices = this->marshaller.protoToMovieIndices(movie_indices_pb);
  }

  return HeadProjectionObject(movie_indices);
}

void ProjectionHeadFileBackend::putObject(std::string& name,
                                          ProjectionObject& object) {
  auto unwrapped_object = static_cast<HeadProjectionObject&>(object).get();

  proto::MovieIndices movie_indices_pb =
      this->marshaller.movieIndicesToProto(unwrapped_object, this->version);
  std::string serialized_movie_indices;
  movie_indices_pb.SerializeToString(&serialized_movie_indices);

  proto::UploadObjectRequest request;
  request.set_allocated_objectname(&name);
  request.set_allocated_serializedobject(&serialized_movie_indices);

  this->client.putObject(request);
}