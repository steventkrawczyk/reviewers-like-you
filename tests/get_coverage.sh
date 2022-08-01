#!/bin/sh

echo "Generating test coverage report..."
docker run --rm -v ${PWD}:/reviewers-like-you \
    --env AWS_ACCESS_KEY_ID=fakeKeyId --env AWS_SECRET_ACCESS_KEY=fakeAccessKey --env AWS_DEFAULT_REGION=us-west-2 stevenkrawczyk/reviewers-like-you \
    pytest tests/test_pipeline_in_memory.py --cov=app/ --cov-branch --cov-config=.coveragerc --cov-fail-under=80 > data/metrics/pytest/coverage_report.txt
echo "Done."