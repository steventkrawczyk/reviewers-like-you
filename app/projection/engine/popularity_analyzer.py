from typing import List, Set

from app.ingestion.main_datastore_proxy import MainDatastoreProxy


class PopularityAnalyzer:
    '''
    This class encapsulated the logic for creating a list of popular movies
    to use as the rows in our projection of the movie reviews into a vector
    space for finding user-reviewer matches.
    '''

    def __init__(self, main_datastore_proxy: MainDatastoreProxy):
        self.main_datastore_proxy = main_datastore_proxy

    def compute_popular_movies(self, authors: List[str]) -> Set[str]:
        popular_movies = set()

        # Idea: popular movies are ones that every reviewer has
        # reviewed.
        for author in authors:
            reviews_by_author = self.main_datastore_proxy.get(author)
            movies_by_author = set(
                [review.movie for review in reviews_by_author])
            if popular_movies:
                popular_movies = popular_movies.intersection(movies_by_author)
            else:
                popular_movies = movies_by_author

        return popular_movies
