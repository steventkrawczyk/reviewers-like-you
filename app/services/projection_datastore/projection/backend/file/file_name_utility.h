#include <string>

#include "app/services/projection_datastore/projection/backend/projection_backend.h"

class FileNameUtility : NameUtility {
 public:
  FileNameUtility(std::string projection_document_name_root,
                  std::string movie_indices_document_name_root);
  std::string getShardDocumentName(int shard_index);
  std::string getMovieIndicesDocumentName();

 private:
  std::string projection_document_name_root;
  std::string movie_indices_document_name_root;
};