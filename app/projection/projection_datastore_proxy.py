'''
This class is used as a proxy to the database that stores our
projection.
'''
class ProjectionDatastoreProxy:
    def __init__(self):
        self.projection = dict()

    def upload(self, projection):
        self.projection = projection

    def get(self):
        return self.projection