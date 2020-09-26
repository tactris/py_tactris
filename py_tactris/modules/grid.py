import numpy as np
from modules import Block
from utlis import SmartStack


class WorkingArea:
    def __init__(self, shapes):
        self.shape1, self.shape2 = shapes
        self.area = []
        self.stack = SmartStack(4)

    def set_shapes(self, shapes):
        self.shape1, self.shape2 = shapes

    def press_block(self, block):
        if block.is_filled:
            return
        elif block.is_pressed:
            block.unpress()
            self.stack.remove(block)
        else:
            block.press()
            popped_block = self.stack.append(block)
            if popped_block:
                popped_block.unpress()

    def get_root_coord(self):
        """
        Root is the lowest right element of working area
        """
        lowest = max(self.stack, key=lambda x: x.i)
        rightest = max(self.stack, key=lambda x: x.j)
        lowest_i = lowest.i if lowest.i > 2 else 2
        rightest_j = rightest.j if rightest.j > 2 else 2
        return lowest_i, rightest_j

    def shape_match(self):
        all_cur_shapes = self.shape1.SHAPES | self.shape2.SHAPES
        if self.hash in all_cur_shapes:
            return self.hash

    def update(self, grid):
        if not self.stack:
            return None
        root_i, root_j = self.get_root_coord()
        self.area = []
        for i in range(root_i - 2, root_i + 1):
            line = []
            for j in range(root_j - 2, root_j + 1):
                line.append(grid[i][j])
            self.area.append(line)

        matched_shape = self.shape_match()
        if matched_shape:
            self.fill_shape()
            self.stack.clear()
            return matched_shape

    def fill_shape(self):
        for line in self.area:
            for block in line:
                if block.is_pressed:
                    block.fill()

    @property
    def hash(self):
        return "".join("1" if b.is_pressed else "0" for line in self.area for b in line)


class Grid:
    def __init__(self, screen, cur_shapes, n=10):
        self.n = n
        self.grid: np.ndarray = np.array([])
        self.screen = screen
        self.stack = SmartStack(4)
        self.working_area = WorkingArea(cur_shapes)
        self.draw()

    def set_shapes(self, shapes):
        self.working_area.set_shapes(shapes)

    @staticmethod
    def is_line_filled(line):
        return all(block.is_filled for block in line)

    def tactris(self, blocks):
        for block in blocks:
            block.unpress()

    def update(self):
        blocks = set()
        for line in self.grid:
            if self.is_line_filled(line):
                blocks |= set(line)

        for line in self.grid.T:
            if self.is_line_filled(line):
                blocks |= set(line)

        self.tactris(blocks)

    def click(self, x, y):
        i, j = y // 50, x // 50
        if i >= self.n or j >= self.n:
            return
        block = self.grid[i][j]
        self.working_area.press_block(block)
        shape_matched = self.working_area.update(self.grid)
        if shape_matched:
            self.update()
            return shape_matched

    def draw(self):
        grid = []
        x, y = 0, 0
        for i in range(self.n):
            line = []
            for j in range(self.n):
                block = Block(self.screen, x, y, i, j)
                line.append(block)
                x += 50
            grid.append(line)
            x = 0
            y += 50
        self.grid = np.array(grid)
