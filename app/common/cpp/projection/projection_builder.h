#include <atomic>
#include <memory>
#include <string>
#include <vector>

#include "app/common/cpp/clients/main_datastore_client.h"
#include "app/common/cpp/clients/projection_datastore_client.h"

// This class builds our projection from authors and a popular movie set
class ProjectionBuilder {
 public:
  ProjectionBuilder(
      std::shared_ptr<MainDatastoreClient> main_datastore,
      std::shared_ptr<ProjectionDatastoreClient> projection_datastore);

  void buildAndStoreVectors(std::vector<std::string> authors,
                            std::vector<std::string> popular_movies);

 private:
  std::shared_ptr<MainDatastoreClient> main_datastore;
  std::shared_ptr<ProjectionDatastoreClient> projection_datastore;
  std::vector<float> cumulative_vector;
  std::atomic<int> vector_count;

  std::map<std::string, int> buildMovieIndices(
      std::vector<std::string> popular_movies);
  std::map<std::string, std::vector<float>> buildVectors(
      std::vector<std::string> authors,
      std::map<std::string, int> movie_indices);
  inline std::vector<float> buildVectorForAuthor(
      std::string author, std::map<std::string, int> movie_indices);
  void uploadVectors(std::map<std::string, std::vector<float>> vectors);
  inline void incrementCumulativeVector(std::vector<float> vec);
  std::map<std::string, std::vector<float>> buildAverageVector();
};
