#include "app/common/cpp/clients/projection_datastore_client.h"

#include <grpcpp/create_channel.h>
#include <grpcpp/security/credentials.h>

ProjectionDatastoreClient::ProjectionDatastoreClient(std::string endpoint_url) {
  this->channel =
      grpc::CreateChannel(endpoint_url, grpc::InsecureChannelCredentials());
  this->stub = proto::ProjectionDatastoreService::NewStub(this->channel);
}

void ProjectionDatastoreClient::upload(
    std::map<std::string, std::vector<float>> projection,
    std::map<std::string, int> movie_indices, std::string version) {
  proto::UploadProjectionRequest request;
  proto::Payload payload;

  auto projection_pb = this->marshaller.projectionToProto(projection, version);
  auto movie_indices_pb =
      this->marshaller.movieIndicesToProto(movie_indices, version);
  request.set_allocated_projection(&projection_pb);
  request.set_allocated_movieindices(&movie_indices_pb);

  auto status =
      this->stub->UploadProjection(&(this->context), request, &payload);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }
}

void ProjectionDatastoreClient::append(
    std::map<std::string, std::vector<float>> projection, std::string version) {
  proto::AppendProjectionRequest request;
  proto::Payload payload;

  auto projection_pb = this->marshaller.projectionToProto(projection, version);
  request.set_allocated_projection(&projection_pb);

  auto status =
      this->stub->AppendProjection(&(this->context), request, &payload);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }
}

std::map<std::string, std::vector<float>>
ProjectionDatastoreClient::getShardProjection(int shard_id) {
  proto::DownloadProjectionRequest request;
  proto::DownloadProjectionResponse response;
  request.set_shardid(shard_id);

  auto status =
      this->stub->DownloadProjection(&(this->context), request, &response);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }

  auto projection = this->marshaller.protoToProjection(response.projection());
  return projection;
}

std::map<std::string, int>& ProjectionDatastoreClient::getMovieIndices() {
  proto::DownloadMovieIndicesRequest request;
  proto::DownloadMovieIndicesResponse response;

  auto status =
      this->stub->DownloadMovieIndices(&(this->context), request, &response);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }

  auto movie_indices =
      this->marshaller.protoToMovieIndices(response.movieindices());
  return movie_indices;
}

int ProjectionDatastoreClient::getShardCount() {
  proto::ShardCountRequest request;
  proto::ShardCountResponse response;
  auto status = this->stub->ShardCount(&(this->context), request, &response);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }
  return response.count();
}
