from abc import ABC, abstractmethod
from typing import List, Set

from app.common.python.model.review import Review


class MainDatastoreProxy(ABC):
    '''
    This is the client for the primary storage for raw input to the system,
    ingested from web scrapers, manual uploads, and user input.
    '''

    @abstractmethod
    def upload(self, review: Review) -> None:
        pass

    @abstractmethod
    def batch_upload(self, reviews: List[Review]) -> None:
        pass

    @abstractmethod
    def get(self, author: str) -> List[Review]:
        pass

    @abstractmethod
    def get_keys(self) -> Set[str]:
        pass
