# How To Demo

1. Make sure you have the good python environment set up (i.e. using Python 3.7 ot later)
2. Try unit tests by running `python -m unittest tests.<test_file_name>` from the root dir of this repo

3. Setup a local dynamodb instance by following the link below, and run `python tools/create_dynamodb_table.py` from the root dir of this repo to setup a table for the flask app to use:
  * https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html
4. Try the flask server by running `FLASK_APP=app/recommendation_server.py flask run`. Currently, the flask app requires you to manually enter user input as query parameters on the URL, like `http://127.0.0.1:5000/match?bladerunner=1`
5. To run the react app: with the flask app running, `cd` into the `frontend` dir and run `yarn start`. It will open a web page. 

# Design

https://docs.google.com/document/d/1sPTaOpxOl5q8VmGsr-TLnwGrpLGtXugPjhlEqxvhL1Q/edit?usp=sharing
