import random


class Shape:
    def __init__(self):
        self.hash = random.choice(list(self.SHAPES))


class LShape(Shape):
    SHAPES = {
        "100" "100" "110",
        "010" "010" "011",
        "001" "111" "000",
        "000" "001" "111",
        "110" "010" "010",
        "011" "001" "001",
        "111" "100" "000",
        "000" "111" "100",
    }


class JShape(Shape):
    SHAPES = {
        "100" "111" "000",
        "000" "100" "111",
        "010" "010" "110",
        "001" "001" "011",
        "111" "001" "000",
        "000" "111" "001",
        "110" "100" "100",
        "011" "010" "010",
    }


class ZShape(Shape):
    SHAPES = {"110" "011" "000", "000" "110" "011", "010" "110" "100", "001" "011" "010"}


class SShape(Shape):
    SHAPES = {"011" "110" "000", "000" "011" "110", "100" "110" "010", "010" "011" "001"}


class TShape(Shape):
    SHAPES = {
        "010" "111" "000",
        "000" "010" "111",
        "100" "110" "100",
        "010" "011" "010",
        "111" "010" "000",
        "000" "111" "010",
        "010" "110" "010",
        "001" "011" "001",
    }


class OShape(Shape):
    SHAPES = {"110" "110" "000", "000" "110" "110", "011" "011" "000", "000" "011" "011"}


def get_random_shape(*shapes) -> Shape:
    classes = [LShape, JShape, ZShape, SShape, TShape, OShape]
    for shape in shapes:
        classes.remove(shape.__class__)
    cls = random.choice(classes)
    return cls()


ALL_SHAPES = LShape.SHAPES | JShape.SHAPES | ZShape.SHAPES | SShape.SHAPES | TShape.SHAPES | OShape.SHAPES
