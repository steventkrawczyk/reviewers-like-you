from typing import Dict, List


class ProjectionDatastoreShard:
    '''
    A single shard for projection data storage. Corresponds to one file
    storing projection vectors.
    '''

    def __init__(self):
        self.projection = dict()

    def upload(self, projection: Dict[str, List[float]]) -> None:
        self.projection = projection

    def get_all(self) -> Dict[str, List[float]]:
        return self.projection

    def get(self, author: str):
        return self.projection[author]
