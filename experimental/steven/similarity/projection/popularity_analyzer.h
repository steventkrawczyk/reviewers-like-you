#include "main_datastore_proxy.h"

class PopularityAnalyzer {
 public:
  PopularityAnalyzer(MainDatastoreProxy& datastore);

  std::set<std::string> computePopularMovies(std::vector<std::string> authors);

 private:
  MainDatastoreProxy& datastore;
};