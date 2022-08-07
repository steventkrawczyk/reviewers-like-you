#include "app/common/cpp/clients/main_datastore_client.h"

#include <grpcpp/create_channel.h>
#include <grpcpp/security/credentials.h>

#include <iostream>

MainDatastoreClient::MainDatastoreClient(std::string endpoint_url) {
  this->channel =
      grpc::CreateChannel(endpoint_url, grpc::InsecureChannelCredentials());
  this->stub = proto::MainDatastoreService::NewStub(this->channel);
}

void MainDatastoreClient::upload(proto::Review* review) {
  proto::UploadReviewRequest request;
  proto::Payload payload;

  request.set_allocated_review(review);

  auto status = this->stub->UploadReview(&(this->context), request, &payload);
  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }
}

void MainDatastoreClient::batchUpload(proto::ReviewList reviews) {
  proto::BatchUploadReviewRequest request;
  proto::Payload payload;

  request.set_allocated_reviewlist(&reviews);

  auto status =
      this->stub->BatchUploadReview(&(this->context), request, &payload);

  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }
}

proto::ReviewList MainDatastoreClient::get(std::string author) {
  proto::GetReviewsByAuthorRequest request;
  proto::GetReviewsByAuthorResponse response;
  request.set_allocated_author(&author);

  auto status =
      this->stub->GetReviewsByAuthor(&(this->context), request, &response);

  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }

  return response.reviewlist();
}

std::vector<std::string> MainDatastoreClient::getKeys() {
  proto::GetAuthorsRequest request;
  proto::GetAuthorsResponse response;

  auto status = this->stub->GetAuthors(&(this->context), request, &response);

  if (!status.ok()) {
    std::cout << status.error_message() << std::endl;
  }

  std::vector<std::string> authors;
  for (auto const& author : response.author()) {
    authors.push_back(author);
  }

  return authors;
}
