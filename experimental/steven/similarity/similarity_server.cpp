#include <memory>
#include <restbed>

void get_average_handler(const std::shared_ptr<restbed::Session> session) {
  session->close(OK, "Hello, World!",
                 {{"Content-Length", "13"}, {"Connection", "close"}});
}

void post_closest_handler(const std::shared_ptr<restbed::Session> session) {
  session->close(OK, "Hello, World!",
                 {{"Content-Length", "13"}, {"Connection", "close"}});
}

int main(const int, const char**) {
  auto average_resource = make_shared<restbed::Resource>();
  average_resource->set_path("/average");
  average_resource->set_method_handler("GET", get_average_handler);

  auto closest_resource = make_shared<restbed::Resource>();
  closest_resource->set_path("/closest");
  closest_resource->set_method_handler("POST", post_closest_handler);

  auto settings = make_shared<restbed::Settings>();
  settings->set_port(5000);

  Service service;
  service.publish(average_resource);
  service.publish(closest_resource);
  service.start(settings);

  return EXIT_SUCCESS;
}