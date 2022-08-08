#include "app/common/cpp/clients/projection_file_client.h"

#include <grpcpp/create_channel.h>
#include <grpcpp/security/credentials.h>

#include "app/generated/cpp/data_model.pb.h"

ProjectionFileClient::ProjectionFileClient(std::string endpoint_url,
                                           std::string bucket_name) {
  this->channel =
      grpc::CreateChannel(endpoint_url, grpc::InsecureChannelCredentials());
  this->stub = proto::FilestoreService::NewStub(this->channel);
  this->bucket_name = bucket_name;
}

bool ProjectionFileClient::objectExists(std::string name) {
  proto::StatObjectRequest request;
  proto::StatObjectResponse response;

  auto status = this->stub->StatObject(&(this->context), request, &response);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }

  return response.found();
}

std::map<std::string, int> ProjectionFileClient::getMovieIndices(
    std::string name) {
  proto::DownloadObjectRequest request;
  proto::DownloadObjectResponse response;
  auto status =
      this->stub->DownloadObject(&(this->context), request, &response);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }

  std::map<std::string, int> movie_indices;
  if (response.found()) {
    std::string serialized_response = response.data();
    proto::MovieIndices movie_indices_pb;
    movie_indices_pb.ParseFromString(serialized_response);
    movie_indices = this->marshaller.protoToMovieIndices(movie_indices_pb);
  }

  return movie_indices;
}

std::map<std::string, std::vector<float>> ProjectionFileClient::getProjection(
    std::string name) {
  proto::DownloadObjectRequest request;
  proto::DownloadObjectResponse response;
  auto status =
      this->stub->DownloadObject(&(this->context), request, &response);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }

  std::map<std::string, std::vector<float>> projection;
  if (response.found()) {
    std::string serialized_response =
        response.data() proto::Projection projection_pb;
    projection_pb.ParseFromString(serialized_response);
    projection = this->marshaller.protoToProjection(projection_pb);
  }

  return projection;
}

void ProjectionFileClient::putMovieIndices(
    std::string name, std::map<std::string, int> movie_indices) {
  proto::MovieIndices movie_indices_pb =
      this->marshaller.movieIndicesToProto(movie_indices);

  std::string serialized_movie_indices;
  movie_indices_pb.SerializeToString(&serialized_movie_indices);

  proto::UploadObjectRequest request;
  proto::Payload payload;
  request.set_allocated_bucketname(&(this->bucket_name));
  request.set_allocated_objectname(&name);
  request.set_allocated_serializedobject(&serialized_movie_indices);

  auto status = this->stub->UploadObject(&(this->context), request, &payload);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }
}

void ProjectionFileClient::putProjection(
    std::string name, std::map<std::string, std::vector<float>> projection) {
  proto::Projection projection_pb =
      this->marshaller.projectionToProto(projection);

  std::string serialized_projection;
  projection_pb.SerializeToString(&serialized_projection);

  proto::UploadObjectRequest request;
  proto::Payload payload;
  request.set_allocated_bucketname(&(this->bucket_name));
  request.set_allocated_objectname(&name);
  request.set_allocated_serializedobject(&serialized_projection);

  auto status = this->stub->UploadObject(&(this->context), request, &payload);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }
}