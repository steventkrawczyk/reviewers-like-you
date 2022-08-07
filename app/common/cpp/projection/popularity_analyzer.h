#include "app/common/cpp/clients/main_datastore_client.h"

class PopularityAnalyzer {
 public:
  PopularityAnalyzer(std::shared_ptr<MainDatastoreClient> datastore);

  std::set<std::string> computePopularMovies(std::vector<std::string> authors);

 private:
  std::shared_ptr<MainDatastoreClient> datastore;
};