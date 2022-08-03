#include "similarity_engine.h"

class SimilarityEngineFactory {
  public:
    SimilarityEngineFactory();

    SimilarityEngine build();
};