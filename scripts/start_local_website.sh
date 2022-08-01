#!/bin/sh

docker compose up -d
echo "Waiting 10 seconds for services to startup..."
sleep 10
echo "Setting up data..."
python -m tools.manage_table create movie_reviews
python -m tools.upload_data tests/test_data.csv
python -m tools.create_projection
echo "Waiting for React to start..."
for i in 2 1
do
    echo "$((i*5)) more seconds..."
    sleep 5
done
open http://localhost:5000
docker-compose logs -f -t 

trap cleanup 0

cleanup()
{
  echo "Caught Signal ... cleaning up."
  python -m tools.manage_table delete movie_reviews
  docker compose down
  echo "Done cleanup ... quitting."
  exit 1
}