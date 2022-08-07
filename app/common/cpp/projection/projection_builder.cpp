#include "app/common/cpp/projection/projection_builder.h"

ProjectionBuilder::ProjectionBuilder(
    std::shared_ptr<MainDatastoreClient> main_datastore,
    std::shared_ptr<ProjectionDatastoreHead> projection_datastore)
    : main_datastore(main_datastore),
      projection_datastore(projection_datastore) {}

void ProjectionBuilder::buildAndStoreVectors(
    std::vector<std::string> authors, std::vector<std::string> popular_movies) {
  auto movie_indices = this->buildMovieIndices(popular_movies);
  this->projection_datastore->upload(
      std::map<std::string, std::vector<float>>(), movie_indices);

  // To do, slice and multithread
  auto vectors = this->buildVectors(authors, movie_indices);
  this->uploadVectors(vectors);

  auto average_vector = this->buildAverageVector();
  this->uploadVectors(average_vector);
}

std::map<std::string, int> ProjectionBuilder::buildMovieIndices(
    std::vector<std::string> popular_movies) {
  std::map<std::string, int> movie_indices;
  for (int i = 0; i < popular_movies.size(); i++) {
    movie_indices[popular_movies[i]] = i;
  }
  return movie_indices;
}

std::map<std::string, std::vector<float>> ProjectionBuilder::buildVectors(
    std::vector<std::string> authors,
    std::map<std::string, int> movie_indices) {
  std::map<std::string, std::vector<float>> projection;
  for (auto const& author : authors) {
    projection[author] = this->buildVectorForAuthor(author, movie_indices);
    this->incrementCumulativeVector(projection[author]);
  }
  return projection;
}

std::vector<float> ProjectionBuilder::buildVectorForAuthor(
    std::string author, std::map<std::string, int> movie_indices) {
  std::vector<float> author_vector = std::vector<float>(movie_indices.size());
  proto::ReviewList reviewList = this->main_datastore->get(author);
  for (auto const& review : reviewList.review()) {
    if (movie_indices.contains(review.movie())) {
      author_vector[movie_indices[review.movie()]] = review.rating();
    }
  }
  return author_vector;
}

void ProjectionBuilder::uploadVectors(
    std::map<std::string, std::vector<float>> vectors) {
  this->projection_datastore->append(vectors);
}

// May have to think about race conditions here...
void ProjectionBuilder::incrementCumulativeVector(std::vector<float> vec) {
  for (int i = 0; i < this->cumulative_vector.size(); i++) {
    this->cumulative_vector[i] += vec[i];
  }
  this->vector_count++;
}

std::map<std::string, std::vector<float>>
ProjectionBuilder::buildAverageVector() {
  std::map<std::string, std::vector<float>> average_vector_map;
  std::vector<float> average_vector;

  for (auto const& num : this->cumulative_vector) {
    float avg = num / (float)this->vector_count;
    average_vector.push_back(avg);
  }

  average_vector_map["_average"] = average_vector;
  return average_vector_map;
}