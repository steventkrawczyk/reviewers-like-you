use actix_web::{get, web, App, HttpServer, Responder, HttpRequest, HttpResponse};

// Eventually with reloads, this will be shared mutable state
struct AppState {
    movies_list: Vec<String>,
}

#[get("/movies")]
async fn movies(data: web::Data<AppState>) -> impl Responder {
    // Look into https://github.com/jaemk/cached to cache json serialization
    movies_json = json::encode(&data.movies_list).unwrap();
    HttpResponse::Ok().json(movies_json)
}

#[actix_web::main] // or #[tokio::main]
async fn main() -> std::io::Result<()> {
    env_logger::init();

    HttpServer::new(|| {
        App::new()
        .app_data(web::Data::new(AppState {
            // Load movies from some cache, could grpc datastore, use redis, or store in memory somehow...
            movies_list: Vec::new(),
        }))
        .service(movies)
    })
    .bind(("127.0.0.1", 5000))
    .unwrap()
    .run()
    .unwrap();
}