from typing import Optional, Tuple

import numpy as np
from modules import Block
from utlis import matrix
from utlis.stack import SmartStack


class WorkingArea:
    def __init__(self, shapes):
        self.shape1, self.shape2 = shapes
        self.area = []
        self.stack = SmartStack(4)

    def set_shapes(self, shapes):
        self.shape1, self.shape2 = shapes

    def press_block(self, block) -> None:
        if block.is_filled or block.is_pressed:
            return None
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

    def shape_match(self) -> Optional[str]:
        all_cur_shapes = self.shape1.SHAPES | self.shape2.SHAPES
        if self.hash in all_cur_shapes:
            return self.hash
        return None

    def update(self, grid) -> None:
        if not self.stack:
            return
        root_i, root_j = self.get_root_coord()
        self.area = []
        for i in range(root_i - 2, root_i + 1):
            line = []
            for j in range(root_j - 2, root_j + 1):
                line.append(grid[i][j])
            self.area.append(line)

    def get_shape_hash(self) -> Optional[str]:
        shape_hash = self.shape_match()
        if shape_hash:
            self.fill_shape()
            self.stack.clear()
            return shape_hash
        return None

    def fill_shape(self) -> None:
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
        self.grid: np.ndarray
        self.screen = screen
        self.stack = SmartStack(4)
        self.working_area = WorkingArea(cur_shapes)
        self.draw()

    def set_shapes(self, shapes):
        self.working_area.set_shapes(shapes)

    @staticmethod
    def is_line_filled(line):
        return all(block.is_filled for block in line)

    @property
    def _states(self) -> np.ndarray:
        states = []
        for line in self.grid:
            states.append([block.state for block in line])
        return np.array(states)

    def roll_empty_lines(self, rows, columns):
        states = self._states
        for i in rows:
            if i < 5:
                states = matrix.move_to_start(states, i)
            else:
                states = matrix.move_to_end(states, i)

        states_T = states.T
        for j in columns:
            if j < 5:
                states_T = matrix.move_to_start(states_T, j)
            else:
                states_T = matrix.move_to_end(states_T, j)

        return states_T.T

    def unpress_lines(self, rows, columns):
        for row_idx in rows:
            for block in self.grid[row_idx]:
                block.unpress()

        for col_idx in columns:
            for block in self.grid.T[col_idx]:
                block.unpress()

    def tactris(self, rows, columns):
        self.unpress_lines(rows, columns)
        new_states = self.roll_empty_lines(rows, columns)
        for i in range(self.n):
            for j in range(self.n):
                block = self.grid[i][j]
                new_state = new_states[i][j]
                block.set_state(new_state)

    def update(self) -> int:
        rows = []
        for i, line in enumerate(self.grid):
            if self.is_line_filled(line):
                rows.append(i)

        columns = []
        for j, line in enumerate(self.grid.T):
            if self.is_line_filled(line):
                columns.append(j)

        if rows or columns:
            self.tactris(rows, columns)
        return len(rows) + len(columns)

    def mouse_down(self, x, y) -> None:
        i, j = y // 50, x // 50
        if i >= self.n or j >= self.n:
            return
        block = self.grid[i][j]
        self.working_area.press_block(block)
        self.working_area.update(self.grid)

    def mouse_up(self) -> Tuple[Optional[str], Optional[int]]:
        shape_hash = self.working_area.get_shape_hash()
        if shape_hash:
            lines_removed = self.update()
            return shape_hash, lines_removed
        return None, None

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
        self.grid = np.array(grid)  # noqa
