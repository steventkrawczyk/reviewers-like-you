# How To Demo

1. Make sure you have the good python environment set up (i.e. using Python 3.7 ot later)
2. Try unit tests by running `python -m unittest tests.<test_file_name>` from the root dir of this repo
3. Try the flask server by running `export FLASK_APP=app/recommendation_server.py` then `flask run`. Currently, the flask app requires you to manually enter user input as query parameters on the URL, like `http://127.0.0.1:5000/match?bladerunner=1`
4. To run the react app: with the flask app running, `cd` into the `frontend` dir and run `yarn start`. It will open a web page. 

# Design

https://docs.google.com/document/d/1sPTaOpxOl5q8VmGsr-TLnwGrpLGtXugPjhlEqxvhL1Q/edit?usp=sharing
