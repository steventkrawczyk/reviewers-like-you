from dataclasses import dataclass
from decimal import localcontext
from typing import Dict


@dataclass
class Review:
    '''
    Data class for review, the primary entity of our main data store.
    '''
    author: str
    movie: str
    rating: float

    def to_dict(self) -> Dict[str, object]:
        with localcontext() as ctx:
            ctx.prec = 3
            return {'author': self.author, 'movie': self.movie,
                    'rating': ctx.create_decimal_from_float(self.rating)}

    @staticmethod
    def from_dict(input: Dict[str, object]):
        return Review(input['author'], input['movie'], float(input['rating']))
