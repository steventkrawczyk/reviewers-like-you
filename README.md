# reviewers-like-you

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

Questions: 
* Is the naive vector embedding the best approach? e.g. every movie is a column
* How can we incorporate more complex reviews? e.g. all text, no number rating
* Is there any chance of duplicate reviews for the same movie/author?