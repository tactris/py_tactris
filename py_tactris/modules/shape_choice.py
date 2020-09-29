from core import State
from modules import Block
from shapes import Shape, get_random_shape


class ShapeGrid:
    def __init__(self, screen, x, y, n=4):
        self.n = n
        self.screen = screen
        self.x, self.y = x, y
        self.b_width, self.b_height = 24, 24
        self.blocks = []
        self.shape = None
        self.draw()

    def is_matched(self, _hash):
        return _hash in self.shape.SHAPES

    def update(self, shape: Shape):
        self.shape = shape
        for i, line in enumerate(shape.hash):
            for j, is_pressed in enumerate(line):
                if is_pressed:
                    block = self.blocks[i][j]
                    block.press()

    def clear(self):
        for line in self.blocks:
            for block in line:
                block.remove()

    def draw(self):
        x, y = self.x, self.y
        default_state = State.REMOVED
        for i in range(self.n):
            line = []
            for j in range(self.n):
                block = Block(self.screen, x, y, i, j, default_state, self.b_width, self.b_height)
                line.append(block)
                x += 25
            y += 25
            x = self.x
            self.blocks.append(line)

    def __str__(self):
        return f"hash: {self.shape.hash}"


class ShapeChoice:
    def __init__(self, screen):
        self.screen = screen
        self.current_shapes = {}
        self.shape_grid1 = ShapeGrid(self.screen, 520, 65)
        self.shape_grid2 = ShapeGrid(self.screen, 630, 65)
        self.draw()

    @property
    def shapes(self):
        return [self.shape_grid1.shape, self.shape_grid2.shape]

    def update(self, shape):
        assert shape in (self.shape_grid1.shape, self.shape_grid2.shape)
        if self.shape_grid1.shape == shape:
            matched_grid, another_grid = self.shape_grid1, self.shape_grid2
        else:
            matched_grid, another_grid = self.shape_grid2, self.shape_grid1

        matched_grid.clear()
        shape = get_random_shape(matched_grid.shape, another_grid.shape)
        matched_grid.update(shape)

    def draw(self):
        shape_cls1 = get_random_shape()
        shape_cls2 = get_random_shape(shape_cls1)
        self.shape_grid1.update(shape_cls1)
        self.shape_grid2.update(shape_cls2)
