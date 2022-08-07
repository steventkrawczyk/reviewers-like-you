#include <memory>
#include <restbed>

void put_create_handler(const std::shared_ptr<restbed::Session> session) {
  session->close(OK, "Hello, World!",
                 {{"Content-Length", "13"}, {"Connection", "close"}});
}

int main(const int, const char**) {
  auto closest_resource = make_shared<restbed::Resource>();
  create_resource->set_path("/create");
  create_resource->set_method_handler("PUT", put_create_handler);

  auto settings = make_shared<restbed::Settings>();
  settings->set_port(5000);

  Service service;
  service.publish(create_resource);
  service.start(settings);

  return EXIT_SUCCESS;
}