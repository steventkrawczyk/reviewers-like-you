#!/bin/sh

echo "Running end-to-end tests (in-memory)..."
docker run -v ${PWD}:/reviewers-like-you \
    stevenkrawczyk/reviewers-like-you python -m unittest tests.test_pipeline_in_memory
echo "Running integration tests (containers)..."
docker compose up -d
docker run -v ${PWD}:/reviewers-like-you \
    --env AWS_ACCESS_KEY_ID=fakeKeyId --env AWS_SECRET_ACCESS_KEY=fakeAccessKey --env AWS_DEFAULT_REGION=us-west-2 \
    --network reviewers-like-you_default \
    stevenkrawczyk/reviewers-like-you python -m unittest tests.test_pipeline_containers
docker compose down
echo "Done."