#include "app/generated/cpp/data_model.pb.h"
#include "app/generated/cpp/resource_services.grpc.pb.h"

class MainDatastoreClient {
 public:
  MainDatastoreClient(std::string endpoint_url);

  void upload(proto::Review* review);

  void batchUpload(proto::ReviewList reviews);

  proto::ReviewList get(std::string author);

  std::vector<std::string> getKeys();

 private:
  std::shared_ptr<grpc::Channel> channel;
  std::unique_ptr<proto::MainDatastoreService::Stub> stub;
  grpc::ClientContext context;
};