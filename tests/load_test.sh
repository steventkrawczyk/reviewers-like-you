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
echo "Running load tests..."
docker run --rm -v ${PWD}:/reviewers-like-you \
    --env AWS_ACCESS_KEY_ID=fakeKeyId --env AWS_SECRET_ACCESS_KEY=fakeAccessKey --env AWS_DEFAULT_REGION=us-west-2 \
    --network reviewers-like-you_default stevenkrawczyk/reviewers-like-you \
    locust -f tests/locustfile.py -u 10 -r 1 -t 60 --headless --only-summary -H http://localhost:5000 --csv data/metrics/locust/perf
echo "Done."

trap cleanup 0

cleanup()
{
  echo "Caught Signal ... cleaning up."
  python -m tools.manage_table delete movie_reviews
  docker compose down
  echo "Done cleanup ... quitting."
  exit 1
}