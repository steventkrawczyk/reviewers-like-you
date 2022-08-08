#include <map>
#include <string>

#include "app/common/cpp/marshaller/data_marshaller.h"
#include "app/generated/cpp/resource_services.grpc.pb.h"

#define MAX_SHARDS 20
#define SHARD_SIZE 25

// This client is used to access the projection datastore
class ProjectionDatastoreClient {
 public:
  ProjectionDatastoreClient(std::string endpoint_url);

  void upload(std::map<std::string, std::vector<float>> projection,
              std::map<std::string, int> movie_indices);

  void append(std::map<std::string, std::vector<float>> projection);

  std::map<std::string, std::vector<float>> getShardProjection(int shard_id);

  std::map<std::string, int>& getMovieIndices();

  int getShardCount();

 private:
  std::unique_ptr<proto::ProjectionDatastoreService::Stub> stub;
  std::shared_ptr<grpc::Channel> channel;
  grpc::ClientContext context;
  DataMarshaller marshaller;
};
