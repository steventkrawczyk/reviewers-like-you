#!/bin/sh

./scripts/start_containers.sh
echo "Waiting for website to start..."
./scripts/wait_for_status.bash http://localhost:5000 200
open http://localhost:5000
docker-compose logs -f -t 

trap cleanup 0

cleanup()
{
  echo "Caught Signal ... cleaning up."
  python -m tools.manage_table delete movie_reviews
  docker compose down
  echo "Done cleanup ... quitting."
  exit 1
}