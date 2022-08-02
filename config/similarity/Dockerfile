# syntax=docker/dockerfile:1
FROM stevenkrawczyk/reviewers-like-you:latest
WORKDIR /reviewers-like-you
ENV FLASK_APP=app/servers/similarity_server.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
COPY app/ app/
CMD ["python", "-m", "flask", "run", "-p", "5000"]