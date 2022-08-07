#include "review.pb.h"

class MainDatastoreProxy {
 public:
  MainDatastoreProxy(std::string table_name);

  void upload(reviewers::Review review);

  void batchUpload(std::vector<reviewers::Review> review);

  std::vector<reviewers::Review> get(std::string author);

  std::vector<std::string> getKeys();

  // TODO scan, paging
 private:
  std::string table_name;
};