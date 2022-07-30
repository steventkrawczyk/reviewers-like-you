#!/bin/sh

docker compose up -d
echo "Generating test coverage report..."
docker run --rm -v ${PWD}:/reviewers-like-you \
    --env AWS_ACCESS_KEY_ID=fakeKeyId --env AWS_SECRET_ACCESS_KEY=fakeAccessKey --env AWS_DEFAULT_REGION=us-west-2 \
    --network reviewers-like-you_default stevenkrawczyk/reviewers-like-you \
    pytest . --cov --cov-branch --cov-fail-under=80 > data/metrics/pytest/coverage_report.txt
echo "Done."
docker compose down