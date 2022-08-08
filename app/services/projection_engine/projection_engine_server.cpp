#include <grpcpp/security/credentials.h>
#include <grpcpp/server_builder.h>

#include "app/common/cpp/clients/main_datastore_client.h"
#include "app/common/cpp/clients/projection_datastore_client.h"
#include "app/common/cpp/projection/projection_engine.h"
#include "app/generated/cpp/internal_services.grpc.pb.h"

class ProjectionEngineImpl final
    : public proto::ProjectionEngineService::Service {
 public:
  ProjectionEngineImpl() {
    this->main_datastore = std::make_shared<MainDatastoreClient>("");
    this->projection_datastore =
        std::make_shared<ProjectionDatastoreClient>("");
    this->projection_engine = std::make_unique<ProjectionEngine>(
        this->main_datastore, this->projection_datastore);
  }

  ::grpc::Status CreateProjection(
      ::grpc::ServerContext* context,
      const ::proto::CreateProjectionRequest* request,
      ::proto::Payload* response) {
    this->projection_engine->createProjection();
    std::string successCode = "success";
    response->set_allocated_category(&successCode);
    response->set_status(200);
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
  std::shared_ptr<MainDatastoreClient> main_datastore;
  std::shared_ptr<ProjectionDatastoreClient> projection_datastore;
  std::unique_ptr<ProjectionEngine> projection_engine;
};

void RunServer() {
  std::string server_address("0.0.0.0:5000");
  grpc::Service service = ProjectionEngineImpl();

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