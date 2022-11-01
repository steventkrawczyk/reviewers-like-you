use actix_web::{get, web, App, HttpServer, Responder};

#[get("/match")]
async fn movies(name: web::Path<String>) -> impl Responder {
    format!("Match!")

    // TODO async emit log of user ratings (with -1's) to ES.
    // We can use a Kafka topic, ingestion service, or some other batching/queue
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