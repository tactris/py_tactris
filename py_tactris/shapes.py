import random
from typing import Tuple


class Shape:
    def __init__(self):
        self.hash = random.choice(list(self.SHAPES)) # noqa

    def is_match(self, _hash: Tuple) -> bool:
        return self.hash == _hash


class LShape(Shape):
    SHAPES = {
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
    }


class JShape(Shape):
    SHAPES = {
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
    }


class ZShape(Shape):
    SHAPES = {
        (
            (0, 1),
            (1, 1),
            (1, 0)
        ), (
            (1, 1, 0),
            (0, 1, 1)
        )
    }


class SShape(Shape):
    SHAPES = {
        (
            (1, 0),
            (1, 1),
            (0, 1)
        ), (
            (0, 1, 1),
            (1, 1, 0)
        )
    }


class TShape(Shape):
    SHAPES = {
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
    }


class OShape(Shape):
    SHAPES = {
        (
            (1, 1),
            (1, 1)
        )
    }


class IShape(Shape):
    SHAPES = {
        (
            (1,),
            (1,),
            (1,),
            (1,)
        ), (
            (1, 1, 1, 1),
        )
    }


def get_random_shape(*shapes) -> Shape:
    classes = [LShape, JShape, ZShape, SShape, TShape, OShape, IShape]
    for shape in shapes:
        classes.remove(shape.__class__)
    cls = random.choice(classes)
    return cls()
