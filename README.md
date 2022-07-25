# reviewers-like-you
Steven Krawczyk, Isaac Malsky

July 2022

## Design

![image info](./images/SystemDesign.png)

https://tinyurl.com/reviewers-like-you

## Setup

Make sure you already have python3 installed. Then run the following commands
1. `pip install virtualenv` (or `pip3 install virtualenv`).
2. `virtualenv reviewers-like-you-venv`
3. `source reviewers-like-you-venv/bin/activate`
4. `pip install -r requirements.txt`

Now you have a virtual environment for running our python code. You will need to activate it by running `source reviewers-like-you-venv/bin/activate` whenever you want to develop in this repo.

## How to demo

### Unit tests

Try unit tests by running `python -m unittest tests.<test_file_name>` from the root dir of this repo, or run all tests with `pytest tests` 

### Jupyter notebook

Check out `notebooks/DataPipelineDemo.ipynb` for an overview and demonstration of our backend data processing

### Running the local website

1. Setup a local dynamodb instance by installing docker and kicking off a container with dynamodb by running `docker compose up`
  * You may have to configure your AWS credentials in order to get things working, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html
2. Populate the DynamoDb table with data using `python -m tools.upload_csv tests/test_data.csv`
3. Try the flask server by running `FLASK_APP=app/recommendation_server.py flask run`. Currently, the flask app requires you to manually enter user input as query parameters on the URL, like `http://127.0.0.1:5000/match?bladerunner=1`
4. To run the react app: with the flask app and dynamodb server running, `cd` into the `app/frontend` dir and run `yarn start`. It will open a web page. For troubleshooting with the frontend, look at the `README.md` in that dir.

## Getting started

1. Before you get started, run either `cp -R hooks/ .git/hooks` or `git config core.hooksPath hooks/` to set up the `pre-push` git hook, which will make sure all tests are passing locally before pushing your changes to remote.
2. Make your changes and test locally, using `pytest tests`, and `unittest`, as well as manual testing with the local website.
3. Commit your changes to a feature branch (not `main`) and push it.
4. Follow the steps below to create a github PR from your branch:  
 * https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

