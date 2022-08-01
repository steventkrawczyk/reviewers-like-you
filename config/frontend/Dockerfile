# syntax=docker/dockerfile:1
FROM node:alpine
WORKDIR /reviewers-like-you
RUN yarn install
EXPOSE 3000
COPY app/frontend/ .
CMD ["yarn", "start"]