#!/bin/sh

docker compose up dynamodb-local -d
docker compose up minio -d
echo "Waiting for databases to startup..."
for i in 2 1
do
    echo "$((i*5)) more seconds..."
    sleep 5
done
python -m tools.manage_table create movie_reviews
docker compose up internalproxy -d
echo "Waiting for internal services to startup..."
for i in 2 1
do
    echo "$((i*5)) more seconds..."
    sleep 5
done
echo "Setting up data..."
python -m tools.upload_data tests/test_data.csv
python -m tools.create_projection
docker compose up -d
echo "Waiting for website to start..."
for i in 4 3 2 1
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