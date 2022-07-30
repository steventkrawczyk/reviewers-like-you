#!/bin/sh

echo "Running end-to-end tests (in-memory)..."
docker run --rm -v ${PWD}:/reviewers-like-you stevenkrawczyk/reviewers-like-you \
    python -m unittest tests.test_pipeline_in_memory
echo "Done with end-to-end tests."
docker compose up -d
echo "Running integration tests (containers)..."
docker run --rm -v ${PWD}:/reviewers-like-you \
    --env AWS_ACCESS_KEY_ID=fakeKeyId --env AWS_SECRET_ACCESS_KEY=fakeAccessKey --env AWS_DEFAULT_REGION=us-west-2 \
    --network reviewers-like-you_default stevenkrawczyk/reviewers-like-you \
    python -m unittest tests.test_pipeline_containers
echo "Done with integration tests."
docker compose down