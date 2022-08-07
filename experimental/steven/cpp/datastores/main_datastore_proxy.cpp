#include "main_datastore_proxy.h"

#include <iostream>

MainDatastoreProxy::MainDatastoreProxy(std::string table_name) {
  this->table_name = table_name;
}

void MainDatastoreProxy::upload(reviewers::Review review) {}

void MainDatastoreProxy::batchUpload(std::vector<reviewers::Review> review) {}

std::vector<reviewers::Review> MainDatastoreProxy::get(std::string author) {}

std::vector<std::string> MainDatastoreProxy::getKeys() {}
