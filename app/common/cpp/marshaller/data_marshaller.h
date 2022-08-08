#include "app/generated/cpp/data_model.pb.h"

// This class translates data from protobufs to internal representations
class DataMarshaller {
 public:
  DataMarshaller();

  std::map<std::string, int> protoToMovieIndices(
      proto::MovieIndices movie_indices_pb);
  std::map<std::string, std::vector<float>> protoToProjection(
      proto::Projection projection_pb);

  proto::MovieIndices movieIndicesToProto(
      std::map<std::string, int> movie_indices);
  proto::Projection projectionToProto(
      std::map<std::string, std::vector<float>> projection);
};