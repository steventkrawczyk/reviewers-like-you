# How To Demo

Make sure you have the good python environment set up (i.e. using Python 3.7 ot later)!

## Unit tests

Try unit tests by running `python -m unittest tests.<test_file_name>` from the root dir of this repo, or run all tests with `pytest tests` 

## Jupyter notebook

Check out `notebooks/DataPipelineDemo.ipynb` for an overview and demonstration of our backend data processing

## Running the local website

1. Setup a local dynamodb instance by following the link below, and run `python tools/create_movie_reviews_table.py` from the root dir of this repo to setup a table for the flask app to use:
  * https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html
2. Populate the DynamoDb table with data using `python -m tools.upload_csv tests/test_data.csv`
3. Try the flask server by running `FLASK_APP=app/recommendation_server.py flask run`. Currently, the flask app requires you to manually enter user input as query parameters on the URL, like `http://127.0.0.1:5000/match?bladerunner=1`
4. To run the react app: with the flask app and dynamodb server running, `cd` into the `app/frontend` dir and run `yarn start`. It will open a web page. 

# Design

![image info](./images/SystemDesign.png)

https://tinyurl.com/reviewers-like-you
