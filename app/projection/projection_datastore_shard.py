

import json
import logging
import os
from typing import Dict, List


class ProjectionDatastoreShard:
    def __init__(self, projection_filepath: str, in_memory: bool):
        self.projection = dict()
        self.projection_filepath = projection_filepath
        self.in_memory = in_memory

    def _load_projection(self) -> None:
        if os.path.isfile(self.projection_filepath):
            logging.info("Loading projection data from file.")
            with open(self.projection_filepath) as f:
                self.projection = json.load(f)

    def _save_data(self, projection: Dict[str, List[float]]) -> None:
        with open(self.projection_filepath, 'w+', encoding='utf-8') as f:
            json.dump(projection, f, ensure_ascii=False, indent=4)

    def _cache_data(self, projection: Dict[str, List[float]]) -> None:
        self.projection = projection

    def load_data(self):
        if not self.in_memory:
            self._load_projection()

    def upload(self, projection: Dict[str, List[float]]) -> None:
        if not self.in_memory:
            self._save_data(projection)
        self._cache_data(projection)

    def get_all(self) -> Dict[str, List[float]]:
        return self.projection

    def get(self, author: str):
        return self.projection[author]
