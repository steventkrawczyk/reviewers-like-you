#include "app/services/projection_engine/projection/popularity_analyzer.h"

#include <set>

#include "app/generated/cpp/data_model.pb.h"

PopularityAnalyzer::PopularityAnalyzer(
    std::shared_ptr<MainDatastoreClient> datastore)
    : datastore(datastore) {}

std::set<std::string> PopularityAnalyzer::computePopularMovies(
    std::vector<std::string> authors) {
  std::set<std::string> popular_movies;

  // TODO parallelize. We just need a mutex on popular_movies
  for (auto const& author : authors) {
    proto::ReviewList reviews_by_author = this->datastore->get(author);
    std::set<std::string> movies_by_author;
    for (auto const& review : reviews_by_author.review()) {
      movies_by_author.insert(review.movie());
    }

    if (popular_movies.size() > 0) {
      std::set<std::string> new_popular_movies;
      std::set_intersection(popular_movies.begin(), popular_movies.end(),
                            movies_by_author.begin(), movies_by_author.end(),
                            new_popular_movies.begin());
      popular_movies = new_popular_movies;
    } else {
      popular_movies = movies_by_author;
    }
  }

  return popular_movies;
}
