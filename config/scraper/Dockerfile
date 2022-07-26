# syntax=docker/dockerfile:1
FROM reviewers-like-you:latest
WORKDIR /reviewers-like-you
ENV FLASK_APP=app/scraper_server.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5003
CMD ["python", "-m", "flask", "run", "-p", "5003"]