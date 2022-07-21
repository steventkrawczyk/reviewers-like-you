'''
This is the client for the primary storage for raw input to the system,
ingested from web scrapers, manual uploads, and user input.
NOTE: The current implementation uses a simple in memory database, a
dictionary. At scale, we will need to replace this with a big data
key-value store that supports appending to list values.
'''
from collections import defaultdict

class MainDatastoreProxy:
    def __init__(self):
        self.database = defaultdict(list)

    def upload(self, author: str, movie: str, review: str) -> None:
        self.database[author].append((movie, review))

    def batch_upload(self, reviews: [(str, str, str)]) -> None:
        for review in reviews:
            self.upload(review)

    def get(self, author: str) -> [(str, str)]:
        return self.database[author]
