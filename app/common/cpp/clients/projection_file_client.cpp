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

bool ProjectionFileClient::objectExists(std::string& name) {
  proto::StatObjectRequest request;
  proto::StatObjectResponse response;

  auto status = this->stub->StatObject(&(this->context), request, &response);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }

  return response.found();
}

proto::DownloadObjectResponse ProjectionFileClient::getObject(
    std::string& name) {
  proto::DownloadObjectRequest request;
  proto::DownloadObjectResponse response;
  auto status =
      this->stub->DownloadObject(&(this->context), request, &response);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }

  return response;
}

void ProjectionFileClient::putObject(proto::UploadObjectRequest& request) {
  request.set_allocated_bucketname(&(this->bucket_name));

  proto::Payload payload;
  auto status = this->stub->UploadObject(&(this->context), request, &payload);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }
}