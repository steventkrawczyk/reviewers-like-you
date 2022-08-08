#include <grpcpp/security/credentials.h>
#include <grpcpp/server_builder.h>

#include "app/common/cpp/clients/projection_file_client.h"
#include "app/common/cpp/datastores/projection_datastore_head.h"
#include "app/common/cpp/marshaller/data_marshaller.h"
#include "app/generated/cpp/resource_services.grpc.pb.h"

class ProjectionDatastoreImpl final
    : public proto::ProjectionDatastoreService::Service {
 public:
  ProjectionDatastoreImpl() {
    this->filestore = std::make_shared<ProjectionFileClient>("", "");
    this->datastore =
        std::move(ProjectionDatastoreHead::create(this->filestore, "", ""));
  }

  ::grpc::Status UploadProjection(
      ::grpc::ServerContext* context,
      const ::proto::UploadProjectionRequest* request,
      ::proto::Payload* response) {
    proto::Projection projection = request->projection();
    proto::MovieIndices movie_indices = request->movieindices();

    this->datastore->upload(
        this->marshaller.protoToProjection(projection),
        this->marshaller.protoToMovieIndices(movie_indices));

    std::string successCode = "success";
    response->set_allocated_category(&successCode);
    response->set_status(200);
    return ::grpc::Status();
  }

  ::grpc::Status AppendProjection(
      ::grpc::ServerContext* context,
      const ::proto::AppendProjectionRequest* request,
      ::proto::Payload* response) {
    proto::Projection projection = request->projection();

    this->datastore->append(this->marshaller.protoToProjection(projection));

    std::string successCode = "success";
    response->set_allocated_category(&successCode);
    response->set_status(200);
    return ::grpc::Status();
  }

  ::grpc::Status DownloadProjection(
      ::grpc::ServerContext* context,
      const ::proto::DownloadProjectionRequest* request,
      ::proto::DownloadProjectionResponse* response) {
    auto projection = this->datastore->getShardProjection(request->shardid());
    auto projection_pb = this->marshaller.projectionToProto(projection);
    response->set_allocated_projection(&projection_pb);
    return ::grpc::Status();
  }

  ::grpc::Status DownloadMovieIndices(
      ::grpc::ServerContext* context,
      const ::proto::DownloadMovieIndicesRequest* request,
      ::proto::DownloadMovieIndicesResponse* response) {
    auto movie_indices = this->datastore->getMovieIndices();
    auto movie_indices_pb = this->marshaller.movieIndicesToProto(movie_indices);
    response->set_allocated_movieindices(&movie_indices_pb);
    return ::grpc::Status();
  }

  ::grpc::Status ShardCount(::grpc::ServerContext* context,
                            const ::proto::ShardCountRequest* request,
                            ::proto::ShardCountResponse* response) {
    int shard_count = this->datastore->getShardCount();
    response->set_count(shard_count);
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
  DataMarshaller marshaller;
  std::shared_ptr<ProjectionFileClient> filestore;
  std::unique_ptr<ProjectionDatastoreHead> datastore;
};

void RunServer() {
  std::string server_address("0.0.0.0:5000");
  grpc::Service service = ProjectionDatastoreImpl();

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