#include "main_datastore_proxy.h"

#include <aws/core/Aws.h>
#include <aws/core/utils/Outcome.h>
#include <aws/dynamodb/DynamoDBClient.h>
#include <aws/dynamodb/model/AttributeDefinition.h>
#include <aws/dynamodb/model/GetItemRequest.h>

#include <iostream>

MainDatastoreProxy::MainDatastoreProxy(std::string table_name) {
  Aws::Client::ClientConfiguration clientConfig;
  Aws::DynamoDB::DynamoDBClient dynamoClient(clientConfig);
  this->client = dynamodbClient;
  this->table_name = table_name;
}

void MainDatastoreProxy::upload(reviewers::Review review) {
  Aws::DynamoDB::Model::PutItemRequest putItemRequest;
  putItemRequest.SetTableName(this->table_name);

  Aws::DynamoDB::Model::AttributeValue author_attr;
  Aws::DynamoDB::Model::AttributeValue movie_attr;
  Aws::DynamoDB::Model::AttributeValue rating_attr;
  author_attr.SetS(review.author());
  movie_attr.SetS(review.movie());
  rating_attr.SetN(review.rating());

  // Add all AttributeValue objects.
  putItemRequest.AddItem("author", author_attr);
  putItemRequest.AddItem("movie", movie_attr);
  putItemRequest.AddItem("rating", rating_attr);

  const Aws::DynamoDB::Model::PutItemOutcome result =
      this->client.PutItem(putItemRequest);

  // TODO deal with success/failure
}

void MainDatastoreProxy::batchUpload(std::vector<reviewers::Review> review);

std::vector<reviewers::Review> MainDatastoreProxy::get(std::string author) {
  Aws::DynamoDB::Model::GetItemRequest req;
  req.SetTableName(this->table);
  Aws::DynamoDB::Model::AttributeValue hashKey;
  hashKey.SetS(author);
  req.AddKey("author", hashKey);

  const Aws::DynamoDB::Model::GetItemOutcome& result =
      this->client.GetItem(req);

  // TODO unpack response
}

std::vector<std::string> MainDatastoreProxy::getKeys();
