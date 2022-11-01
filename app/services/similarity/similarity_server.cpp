#include <grpcpp/security/credentials.h>
#include <grpcpp/server_builder.h>

#include "app/common/cpp/clients/projection_datastore_client.h"
#include "app/generated/cpp/backend_services.grpc.pb.h"
#include "app/services/similarity/similarity/similarity_engine.h"

class SimilarityImpl final : public proto::SimilarityEngineService::Service {
 public:
  SimilarityImpl() {
    this->datastore = std::make_shared<ProjectionDatastoreClient>("");
    this->similarity_engine = SimilarityEngine::create(this->datastore);
  }

  ::grpc::Status GetClosestNeighbor(
      ::grpc::ServerContext* context,
      const ::proto::GetClosestNeighborRequest* request,
      ::proto::GetClosestNeighborResponse* response) {
    proto::Vector vec_pb = request->vector();

    std::vector<float> vec;
    for (auto const& num : vec_pb.entry()) {
      vec.push_back(num);
    }

    auto neighbor = this->similarity_engine->getClosestNeighbor(vec);

    response->set_allocated_author(&neighbor);
    return ::grpc::Status();
  }

  ::grpc::Status FindAverageVector(
      ::grpc::ServerContext* context,
      const ::proto::FindAverageVectorRequest* request,
      ::proto::FindAverageVectorResponse* response) {
    auto vec = this->similarity_engine->findAverageVector();

    proto::Vector vec_pb;
    for (auto const& num : vec) {
      vec_pb.add_entry(num);
    }

    response->set_allocated_vector(&vec_pb);
    return ::grpc::Status();
  }

  ::grpc::Status CheckHealth(::grpc::ServerContext* context,
                             const ::proto::HealthCheckRequest* request,
                             ::proto::Payload* response) {
    // TODO add a more robust health check - forward to data gateway admin
    // service
    std::string successCode = "success";
    response->set_allocated_category(&successCode);
    response->set_status(200);
    return ::grpc::Status();
  }

 private:
  std::shared_ptr<ProjectionDatastoreClient> datastore;
  std::unique_ptr<SimilarityEngine> similarity_engine;
};

void RunServer() {
  std::string server_address("0.0.0.0:5000");
  grpc::Service service = SimilarityImpl();

  grpc::ServerBuilder builder;
  builder.AddListeningPort(server_address, grpc::InsecureServerCredentials());
  builder.RegisterService(&service);
  std::unique_ptr<grpc::Server> server(builder.BuildAndStart());
  std::cout << "Server listening on " << server_address << std::endl;
  server->Wait();
}

int main(int argc, char** argv) {
  RunServer();

  return 0;
}