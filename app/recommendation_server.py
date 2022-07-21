from flask import Flask
from flask import render_template
from flask import request
import pandas as pd
from pathlib import Path

from app.main_datastore.main_datastore_proxy import MainDatastoreProxy
from app.main_datastore.dataframe_ingestion_client import DataframeIngestionClient
from app.projection.projection_datastore_proxy import ProjectionDatastoreProxy
from app.projection.projection_engine import ProjectionEngine
from app.recommendation.match_generator import MatchGenerator


# NOTE: This approach is only for testing while we don't have a
# persistent DB.
test_data_file = Path(__file__).parent.parent / "tests/test_data.csv"
test_data = pd.read_csv(test_data_file, header=0)
database = MainDatastoreProxy()
client = DataframeIngestionClient(database)
client.upload(test_data)

authors = list(database.get_keys())
projection_databse = ProjectionDatastoreProxy()
projection_engine = ProjectionEngine(database, projection_databse)
projection_engine.create_projection()
# End test setup

match_generator = MatchGenerator(database, projection_databse)
app = Flask(__name__)

@app.route('/')
def default():
    return "<p>Please submit movie preferences:</p>"
    
@app.route('/match', methods=['GET'])
def match():
    match_data = {}
    user_input = {}

    # TODO cleanse user input
    for movie, review in request.args.items():
        user_input[movie] = float(review)
        print(user_input)

    match_data = match_generator.get_match(user_input)
    print(match_data)
    return render_template('review_table.html', author=match_data[0], 
                           reviews=match_data[1])
    