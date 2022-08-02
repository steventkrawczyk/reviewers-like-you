#!/bin/sh

docker compose up dynamodb-local -d
docker compose up minio -d
echo "Waiting for databases to startup..."
while ! echo exit | nc localhost 8000; do sleep 5; done
while ! echo exit | nc localhost 9000; do sleep 5; done
python -m tools.manage_table create movie_reviews
docker compose up internalproxy -d
echo "Waiting for internal services to startup..."
while ! echo exit | nc localhost 5002; do sleep 5; done
echo "Setting up data..."
python -m tools.upload_data tests/test_data.csv
python -m tools.create_projection
docker compose up -d
echo "Waiting for website to start..."
./scripts/wait_for_status.bash http://localhost:5000 200 300
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