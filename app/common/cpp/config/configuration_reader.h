
#include <map>
#include <string>

class ConfigurationReader {
 public:
  ConfigurationReader() {}

  void readConfiguration(std::string filename);

  bool getBool(const std::string& key) { return map_of_bools[key]; }

  std::string getString(const std::string& key) { return map_of_strings[key]; }

 private:
  std::map<std::string, std::string> map_of_strings;
  std::map<std::string, bool> map_of_bools;
};