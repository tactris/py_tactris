import random
from typing import Tuple


class Shape:
    def __init__(self, _hash):
        self.hash = _hash

    def is_match(self, _hash: Tuple) -> bool:
        return self.hash == _hash

    SHAPES = {
        "L": {
            (
                (1, 0),
                (1, 0),
                (1, 1)
            ), (
                (0, 0, 1),
                (1, 1, 1)
            ), (
                (1, 1),
                (0, 1),
                (0, 1)
            ), (
                (1, 1, 1),
                (1, 0, 0)
            )
        },
        "J": {
            (
                (1, 0, 0),
                (1, 1, 1)
            ), (
                (0, 1),
                (0, 1),
                (1, 1)
            ), (
                (1, 1, 1),
                (0, 0, 1)
            ), (
                (1, 1),
                (1, 0),
                (1, 0)
            )
        },
        "Z": {
            (
                (0, 1),
                (1, 1),
                (1, 0)
            ), (
                (1, 1, 0),
                (0, 1, 1)
            )
        },
        "S": {
            (
                (1, 0),
                (1, 1),
                (0, 1)
            ), (
                (0, 1, 1),
                (1, 1, 0)
            )
        },
        "T": {
            (
                (0, 1, 0),
                (1, 1, 1)
            ), (
                (1, 0),
                (1, 1),
                (1, 0)
            ), (
                (1, 1, 1),
                (0, 1, 0)
            ), (
                (0, 1),
                (1, 1),
                (0, 1)
            )
        },
        "O": {
            (
                (1, 1),
                (1, 1)
            )
        },
        "I": {
            (
                (1,),
                (1,),
                (1,),
                (1,)
            ), (
                (1, 1, 1, 1),
            )
        }
    }

    ALL_SHAPES: set = set().union(*SHAPES.values())  # type: ignore


def get_random_shape(*shapes: Shape) -> Shape:
    all_shapes = Shape.ALL_SHAPES - set(shape.hash for shape in shapes)
    _hash = random.choice(list(all_shapes))
    return Shape(_hash)
