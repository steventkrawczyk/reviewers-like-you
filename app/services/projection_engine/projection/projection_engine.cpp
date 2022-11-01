#include "app/services/projection_engine/projection/projection_engine.h"

ProjectionEngine::ProjectionEngine(
    std::shared_ptr<MainDatastoreClient> main_datastore,
    std::shared_ptr<ProjectionDatastoreClient> projection_datastore)
    : main_datastore(main_datastore),
      projection_datastore(projection_datastore) {
  this->popularity_analyzer =
      std::make_unique<PopularityAnalyzer>(this->main_datastore);
  this->projection_builder = std::make_unique<ProjectionBuilder>(
      this->main_datastore, this->projection_datastore);
}

void ProjectionEngine::createProjection() {
  auto authors = this->main_datastore->getKeys();
  auto popular_movies =
      this->popularity_analyzer->computePopularMovies(authors);
  std::vector<std::string> popular_movies_vec(popular_movies.size());
  std::copy(popular_movies.begin(), popular_movies.end(),
            popular_movies_vec.begin());
  this->projection_builder->buildAndStoreVectors(authors, popular_movies_vec);

  // TODO publish kafka message about new projection
}