#include "app/common/cpp/clients/main_datastore_client.h"

// This class determines our popular movie set
class PopularityAnalyzer {
 public:
  PopularityAnalyzer(std::shared_ptr<MainDatastoreClient> datastore);

  // TODO function to chain computePopularMovies and storePopularMovies

  std::set<std::string> computePopularMovies(std::vector<std::string> authors);

 private:
  std::shared_ptr<MainDatastoreClient> datastore;
  std::string version;

  // TODO Uploads to ES. We need an ES client
  void storePopularMovies(std::set<std::string> movies);
};