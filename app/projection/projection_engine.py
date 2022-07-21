'''
This class is used to download data from the main datastore and create
a projection of popular movies to use for similarity computations.
'''
import math

class ProjectionEngine:
    def __init__(self, main_datastore_proxy, projection_datastore_proxy):
        self.main_datastore_proxy = main_datastore_proxy
        self.authors = list(self.main_datastore_proxy.get_keys())
        self.projection_datastore_proxy = projection_datastore_proxy
    
    def create_projection(self):
        popular_movies = self.compute_popular_movies()
        author_vectors = self.build_vectors(popular_movies)
        self.store_projection(author_vectors)

    def compute_popular_movies(self):
        popular_movies = set()

        # Idea: popular movies are ones that every reviewer has
        # reviewed.
        for author in self.authors:
            reviews_by_author = self.main_datastore_proxy.get(author)
            movies_by_author = set()
            for movie, review in reviews_by_author:
                if not math.isnan(float(review)):
                    movies_by_author.add(movie)
            if not popular_movies:
                popular_movies = movies_by_author
            popular_movies = popular_movies.intersection(movies_by_author)

        return popular_movies

    def build_vectors(self, popular_movies):
        movie_indices = dict()
        for index, movie in enumerate(popular_movies):
            movie_indices[movie] = index

        author_vectors = dict()
        dim = len(popular_movies)

        for author in self.authors:
            author_vector = [0.0] * dim
            reviews_by_author = self.main_datastore_proxy.get(author)
            for movie, review in reviews_by_author:
                if movie in movie_indices:
                    author_vector[movie_indices[movie]] = float(review)
            author_vectors[author] = author_vector

        return author_vectors

    def store_projection(self, author_vectors):
        self.projection_datastore_proxy.upload(author_vectors)

        


