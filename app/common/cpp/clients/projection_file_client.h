#include <iostream>
#include <map>
#include <string>

#include "app/common/cpp/marshaller/data_marshaller.h"
#include "app/generated/cpp/resource_services.grpc.pb.h"

// This client is used to access the filestore, specifically for projection use
// cases.
class ProjectionFileClient {
 public:
  ProjectionFileClient(std::string& endpoint_url, std::string& bucket_name);

  bool objectExists(std::string& name);

  proto::DownloadObjectResponse getObject(std::string& name);

  void putObject(proto::UploadObjectRequest& request);

 private:
  std::shared_ptr<grpc::Channel> channel;
  std::unique_ptr<proto::FilestoreService::Stub> stub;
  grpc::ClientContext context;
  std::string bucket_name;
};
