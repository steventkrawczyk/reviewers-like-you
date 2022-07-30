#!/bin/sh

docker compose up -d
python -m tools.manage_table create movie_reviews
python -m tools.upload_data tests/test_data.csv
python -m tools.create_projection
open http://localhost:5000