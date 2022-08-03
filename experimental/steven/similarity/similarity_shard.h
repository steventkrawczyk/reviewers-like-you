#include <map>
#include <string>
#include <vector>

struct SimilarityShardRepsonse {
  int index;
  float distance;
};

class SimilarityShard {
  public:
    SimilarityShard(std::vector<std::vector<float>> vectors,
                    std::map<int, std::string> author_index, 
                    std::optional<std::vector<float>> average_vector);

    SimilarityShardRepsonse getClosestNeighbor(std::vector<float> input_vector);

    std::optional<std::string> decodeMatch(int index_of_match);

    std::optional<std::vector<float>> findAverageVector();

    std::vector<float> getVector(int index);

  private:
    std::vector<std::vector<float>> vectors;
    std::map<int, std::string> author_index;
    std::optional<std::vector<float>> average_vector = std::nullopt;

    template <class T>
    inline T computeDistance(std::vector<T> v, std::vector<T> w);
};