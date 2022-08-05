docker compose up internalproxy -d
echo "Waiting for internal services to startup..."
./scripts/wait_for_status.bash http://localhost:5002/uploadhealth 200
./scripts/wait_for_status.bash http://localhost:5002/ingestionhealth 200
./scripts/wait_for_status.bash http://localhost:5002/projectionhealth 200
echo "Setting up data..."
python -m tools.manage_table create movie_reviews
python -m tools.upload_data tests/test_data.csv
python -m tools.create_projection
docker compose up -d
./scripts/wait_for_status.bash http://localhost:5001/movieshealth 200
./scripts/wait_for_status.bash http://localhost:5001/matchhealth 200
./scripts/wait_for_status.bash http://localhost:5001/similarityhealth 200
