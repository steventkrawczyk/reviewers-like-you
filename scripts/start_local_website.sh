#!/bin/sh

docker compose up -d
python -m tools.manage_table create movie_reviews
python -m tools.upload_data tests/test_data.csv
python -m tools.create_projection
echo "Adding some delay to give React a chance to start..."
for i in 3 2 1
do
    echo "$((i*5)) more seconds..."
    sleep 5
done
open http://localhost:5000