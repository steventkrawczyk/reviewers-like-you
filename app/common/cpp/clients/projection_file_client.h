#include <iostream>
#include <map>
#include <string>

#include "app/common/cpp/marshaller/data_marshaller.h"
#include "app/generated/cpp/resource_services.grpc.pb.h"

class ProjectionFileClient {
 public:
  ProjectionFileClient(std::string endpoint_url, std::string bucket_name);

  bool objectExists(std::string name);

  std::map<std::string, int> getMovieIndices(std::string name);

  std::map<std::string, std::vector<float>> getProjection(std::string name);

  void putMovieIndices(std::string name,
                       std::map<std::string, int> movie_indices);

  void putProjection(std::string name,
                     std::map<std::string, std::vector<float>> projection);

 private:
  DataMarshaller marshaller;
  std::shared_ptr<grpc::Channel> channel;
  std::unique_ptr<proto::FilestoreService::Stub> stub;
  grpc::ClientContext context;
  std::string bucket_name;
};
