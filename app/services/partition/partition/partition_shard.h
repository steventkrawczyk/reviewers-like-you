#include <vector>

class PartitionShard {
 public:
  static PartitionShard create(
      std::map<std::string, std::vector<float>> projection);

  PartitionShard();

  std::vector<std::vector<float>> get();

  std::vector<float> getMean();

  void append(std::vector<float> vec);

  void reset();
};