#!/bin/sh

docker compose up -d
python -m tools.manage_table delete movie_reviews
docker compose down