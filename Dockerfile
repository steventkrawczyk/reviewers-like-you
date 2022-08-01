# syntax=docker/dockerfile:1
FROM python:3.9-alpine
WORKDIR /reviewers-like-you
RUN apk add --no-cache gcc g++ musl-dev linux-headers
RUN pip install -r requirements.txt