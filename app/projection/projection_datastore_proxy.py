'''
This class is used as a proxy to the database that stores our
projection.
'''
class ProjectionDatastoreProxy:
    def __init__(self):
        self.movie_indices = dict()
        self.projection = dict()

    def upload(self, projection, movie_indices):
        self.projection = projection
        self.movie_indices = movie_indices

    def get(self):
        return self.projection

    def get_movie_indices(self):
        return self.movie_indices