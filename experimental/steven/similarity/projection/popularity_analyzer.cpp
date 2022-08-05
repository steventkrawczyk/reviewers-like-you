#include "popularity_analyzer.h"

#include <set>

#include "review.pb.h"

PopularityAnalyzer::PopularityAnalyzer(MainDatastoreProxy& datastore) {
  this->datastore = datastore;
}

std::set<std::string> PopularityAnalyzer::computePopularMovies(
    std::vector<std::string> authors) {
  std::set<std::string> popular_movies;

  for (auto const& author : authors) {
    std::vector<reviewers::Review> reviews_by_author =
        this->datastore.get(author);
    std::set movies_by_author;
    for (auto const& review : reviews_by_author) {
      movies_by_author.add(review.movie());
    }
    if (popular_movies.size() > 0) {
      std::set new_popular_movies;
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
