#include "projection_file_store.h"

#include "movie_indices.pb.h"
#include "projection.pb.h"

ProjectionFileStore::ProjectionFileStore(std::string endpoint_url,
                                         std::string bucket_name) {}

void ProjectionFileStore::makeBucketIfItDoesntExist() {}

bool ProjectionFileStore::objectExists(std::string name) {}

std::map<std::string, int> ProjectionFileStore::getMovieIndices(
    std::string name) {
  std::string serialized_response;
  // Get serialized response
  reviewers::MovieIndices movie_indices_pb;
  movie_indices_pb.ParseFromString(serialized_response);

  std::map<std::string, int> movie_indices;
  for (const reviewers::MovieIndicesEntry& entry : movie_indices_pb.entries()) {
    movie_indices[entry.movie()] = entry.index();
  }

  return movie_indices;
}

std::map<std::string, std::vector<float>> ProjectionFileStore::getProjection(
    std::string name) {
  std::string serialized_response;
  // Get serialized response
  reviewers::Projection projection_pb;
  projection_pb.ParseFromString(serialized_response);

  std::map<std::string, std::vector<float>> projection;
  for (const reviewers::ProjectionEntry& entry : projection_pb.entries()) {
    std::vector<float> ratings;
    for (const auto& rating : entry.rating()) {
      ratings.push_back(rating);
    }
    projection[entry.author()] = ratings;
  }

  return projection;
}

void ProjectionFileStore::putMovieIndices(
    std::string name, std::map<std::string, int> movie_indices) {
  reviewers::MovieIndices movie_indices_pb;
  for (auto const& [movie, index] : movie_indices) {
    reviewers::MovieIndicesEntry* entry = movie_indices_pb.add_entries();
    entry->set_movie(movie);
    entry->set_index(index);
  }

  std::string serialized_movie_indices;
  movie_indices_pb.SerializeToString(&serialized_movie_indices);

  // TODO put serialized object
}

void ProjectionFileStore::putProjection(
    std::string name, std::map<std::string, std::vector<float>> projection) {
  reviewers::Projection projection_pb;
  for (auto const& [author, ratings] : projection) {
    reviewers::ProjectionEntry* entry = projection_pb.add_entries();
    entry->set_author(author);

    for (auto const& rating : ratings) {
      entry->add_rating(rating);
    }
  }

  std::string serialized_projection;
  projection_pb.SerializeToString(&serialized_projection);

  // TODO put serialized object
}