from app.recommendation.similarity_engine import SimilarityEngine

class MatchGenerator:
    # TODO create a factory for this
    def __init__(self, main_datastore, projection_datastore):
        self.main_datastore = main_datastore
        self.projection_datastore = projection_datastore

        # We cache these because the calls to DB might be expensive
        # TODO Once a real DB is implemented, evaluate the tradeoff
        self.projection = self.projection_datastore.get()
        self.movie_indices = self.projection_datastore.get_movie_indices()
        
        self.dim = len(self.movie_indices)
        self._build_similarity_engine()

    def _build_similarity_engine(self):
        vectors = []
        self.author_by_index = dict()
        index = 0
        for author, vector in self.projection.items():
            self.author_by_index[index] = author
            index +=1
            vectors.append(vector)
        self.similarity_engine = SimilarityEngine(vectors)

    def get_match(self, user_input):
        # TODO handle incomplete user input (i.e. did not rate all movies)
        vector = [0.0] * self.dim
        for movie, review in user_input.items():
            vector[self.movie_indices[movie]] = review
        index_of_match = self.similarity_engine.get_closest_neighbor(vector)
        author_match = self.author_by_index[index_of_match]
        author_reviews = self.main_datastore.get(author_match)
        return (author_match, author_reviews)