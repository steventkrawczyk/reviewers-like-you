#include "app/common/cpp/marshaller/data_marshaller.h"

#include "app/generated/cpp/data_model.pb.h"

DataMarshaller::DataMarshaller() {}

std::map<std::string, int> DataMarshaller::protoToMovieIndices(
    proto::MovieIndices movie_indices_pb) {
  std::map<std::string, int> movie_indices;
  for (const proto::MovieIndicesEntry& entry : movie_indices_pb.entry()) {
    movie_indices[entry.movie()] = entry.index();
  }

  return movie_indices;
}

std::map<std::string, std::vector<float>> DataMarshaller::protoToProjection(
    proto::Projection projection_pb) {
  std::map<std::string, std::vector<float>> projection;
  for (const proto::ProjectionEntry& entry : projection_pb.entry()) {
    std::vector<float> ratings;
    for (const auto& rating : entry.rating()) {
      ratings.push_back(rating);
    }
    projection[entry.author()] = ratings;
  }

  return projection;
}

proto::MovieIndices DataMarshaller::movieIndicesToProto(
    std::map<std::string, int> movie_indices, std::string version) {
  proto::MovieIndices movie_indices_pb;
  for (auto const& [movie, index] : movie_indices) {
    proto::MovieIndicesEntry* entry = movie_indices_pb.add_entry();
    entry->set_movie(movie);
    entry->set_index(index);
  }
  movie_indices_pb.set_version(version);
  return movie_indices_pb;
}

proto::Projection DataMarshaller::projectionToProto(
    std::map<std::string, std::vector<float>> projection, std::string version) {
  proto::Projection projection_pb;
  for (auto const& [author, ratings] : projection) {
    proto::ProjectionEntry* entry = projection_pb.add_entry();
    entry->set_author(author);

    for (auto const& rating : ratings) {
      entry->add_rating(rating);
    }
  }
  projection_pb.set_version(version);
  return projection_pb;
}
