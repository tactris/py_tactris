from typing import Type

from block import Block
from core import STATES
from shapes import Shape, get_random_shape


class ShapeGrid:
    def __init__(self, screen, x, y, n=3):
        self.n = n
        self.screen = screen
        self.x, self.y = x, y
        self.b_width, self.b_height = 24, 24
        self.blocks = []
        self.shape = None
        self.draw()

    def update(self, shape_cls: Type[Shape]):
        self.shape = shape_cls
        shape_hash = shape_cls.get_hash()
        hash_iter = iter(shape_hash)
        for i in range(self.n):
            for j in range(self.n):
                ch = next(hash_iter)
                if ch == "1":
                    block = self.blocks[i][j]
                    block.press()

    def clear(self):
        for line in self.blocks:
            for block in line:
                block.remove()

    def draw(self):
        x, y = self.x, self.y
        for i in range(self.n):
            line = []
            for j in range(self.n):
                block = Block(self.screen, x, y, i, j, STATES.REMOVED, self.b_width, self.b_height)
                line.append(block)
                x += 25
            y += 25
            x = self.x
            self.blocks.append(line)


class Sidebar:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.record = 0
        self.current_shapes = {}
        self.shape_grid1 = ShapeGrid(self.screen, 520, 65)
        self.shape_grid2 = ShapeGrid(self.screen, 600, 65)
        self.draw()

    def update(self, _hash):
        if _hash in self.shape_grid1.shape.SHAPES:
            shape_grid = self.shape_grid1
        elif _hash in self.shape_grid2.shape.SHAPES:
            shape_grid = self.shape_grid2
        else:
            raise AssertionError("Unexpected shape")
        shape_grid.clear()
        shape_cls = get_random_shape()
        shape_grid.update(shape_cls)

    def draw(self):
        shape_cls1 = get_random_shape()
        shape_cls2 = get_random_shape(shape_cls1)
        self.shape_grid1.update(shape_cls1)
        self.shape_grid2.update(shape_cls2)
