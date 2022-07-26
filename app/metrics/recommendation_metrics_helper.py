'''
This class will be used to store user data from the recommendation service.
'''

from typing import List

from app.metrics.timed_metrics_helper import TimedMetricsHelper


class RecommendationMetricsHelper(TimedMetricsHelper):
    def __init__(self, version: str, filepath: str = f'data/recommendation_metrics.csv'):
        self.version = version
        self.filepath = filepath

    def record_user_preference(self, user_preference_vector: List[float]):
        pass

    def record_similarity_performance(self):
        pass
        