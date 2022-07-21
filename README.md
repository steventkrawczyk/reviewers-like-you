# How To Demo

1. Make sure you have the good python environment set up (i.e. using Python 3.7 ot later)
2. Try unit tests by running `python -m unittest tests.<test_file_name>` from the root dir of this repo
3. Try the flask server by running `export FLASK_APP=app/recommendation_server.py` then `flask run`. Currently, the flask app requires you to manually enter user input as query parameters on the URL, like `http://127.0.0.1:5000/match?bladerunner=1`

# Design

Components:
* Ingestion Service
  * Upload data to main data store
    * CSV, Web Scraper, User Input, etc
  * Process data
    * Create projection space of popular movies
    * Lots of other possibilities here
* Recommendation Service
  * API to get movie's to rate, and accept user preferences
  * Service to find the closest neighbor to the user's preferences in the projection space
  * Service to create a recommendation for users based on author (get data from main data store, rank and filter movies)

APIs:
* Ingestion
  * BatchUpload(rows) - used to upload reviews as a CSV, dataframe, etc.
* Recommendation
  * GetPopularMovies() - used to prompt user for reviews
  * GetReviewerMatch(ratings) - used to get reviewer match for given user ratings

Questions: 
* Is the naive vector embedding the best approach? e.g. every movie is a column
* How can we incorporate more complex reviews? e.g. all text, no number rating
* Is there any chance of duplicate reviews for the same movie/author?
