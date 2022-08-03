#!/bin/sh

./scripts/start_containers.sh
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