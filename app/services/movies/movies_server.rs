use actix_web::{get, web, App, HttpServer, Responder};

#[get("/movies")]
async fn movies(name: web::Path<String>) -> impl Responder {
    format!("Movies!")
}

#[actix_web::main] // or #[tokio::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().service(greet)
    })
    .bind(("127.0.0.1", 5000))?
    .run()
    .await
}