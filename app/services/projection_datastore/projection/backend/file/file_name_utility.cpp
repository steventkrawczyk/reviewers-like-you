#include "app/services/projection_datastore/projection/backend/file/file_name_utility.h"

FileNameUtility::FileNameUtility(std::string projection_document_name_root,
                                 std::string movie_indices_document_name_root)
    : projection_document_name_root(projection_document_name_root),
      movie_indices_document_name_root(movie_indices_document_name_root) {}

std::string FileNameUtility::getShardDocumentName(int shard_index) {
  return this->projection_document_name_root + "_" +
         std::to_string(shard_index) + std::string(".json");
}

std::string FileNameUtility::getMovieIndicesDocumentName() {
  return this->movie_indices_document_name_root + std::string(".json");
}