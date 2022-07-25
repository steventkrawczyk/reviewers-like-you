# reviewers-like-you
Steven Krawczyk, Isaac Malsky

July 2022

## Design

![image info](./images/SystemDesign.png)

https://tinyurl.com/reviewers-like-you

## Setup

1. Install anaconda at: https://docs.anaconda.com/anaconda/install/
2. Run `conda env create -f environment.yml` to create an environment to run our code
3. Run `conda activate reviewers-like-you-env` to activate the enviroment
4. Run `conda env list` to verify that the environment was created correctly

Based on: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file

## How to demo

### Unit tests

Try unit tests by running `python -m unittest tests.<test_file_name>` from the root dir of this repo, or run all tests with `pytest tests` 

### Jupyter notebook

Check out `notebooks/DataPipelineDemo.ipynb` for an overview and demonstration of our backend data processing

### Running the local website

1. Setup a local dynamodb instance by following the link below, and run `python tools/create_movie_reviews_table.py` from the root dir of this repo to setup a table for the flask app to use:
  * https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html
  * Note: There is already a version of dynamodb in this repo, in `dynamodb/`. Consider using that instead of downloading another copy to your machine.
2. Populate the DynamoDb table with data using `python -m tools.upload_csv tests/test_data.csv`
3. Try the flask server by running `FLASK_APP=app/recommendation_server.py flask run`. Currently, the flask app requires you to manually enter user input as query parameters on the URL, like `http://127.0.0.1:5000/match?bladerunner=1`
4. To run the react app: with the flask app and dynamodb server running, `cd` into the `app/frontend` dir and run `yarn start`. It will open a web page. For troubleshooting with the frontend, look at the `README.md` in that dir.

## Getting started

1. Before you get started, run either `cp -R hooks/ .git/hooks` or `git config core.hooksPath hooks/` to set up the `pre-push` git hook, which will make sure all tests are passing locally before pushing your changes to remote.
2. Make your changes and test locally, using `pytest tests`, and `unittest`, as well as manual testing with the local website.
3. Commit your changes to a feature branch (not `main`) and push it.
4. Follow the steps below to create a github PR from your branch:  
 * https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request

