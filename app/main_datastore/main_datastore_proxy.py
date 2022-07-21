'''
This is the client for the primary storage for raw input to the system,
ingested from web scrapers, manual uploads, and user input.

NOTE: The current implementation uses a simple in memory database, a
dictionary. At scale, we will need to replace this with a big data
key-value store that supports appending to list values.

TODO: We need our schema to protect against duplicate reviews. Today
it does not.
'''
from collections import defaultdict

class MainDatastoreProxy:
    def __init__(self):
        self.keys = set()
        self.database = defaultdict(list)

    def upload(self, author: str, movie: str, review: str) -> None:
        self.database[author].append((movie, review))
        self.keys.add(author)

    def batch_upload(self, reviews: [(str, str, str)]) -> None:
        for review in reviews:
            self.upload(review)

    def get(self, author: str) -> [(str, str)]:
        return self.database[author]

    def get_keys(self):
        return self.keys
