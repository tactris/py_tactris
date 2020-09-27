from typing import List, Optional, Tuple

import numpy as np
from core import BlockCore
from modules import Block
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

    @property
    def _states(self) -> np.ndarray:
        states = []
        for line in self.grid:
            states.append([block.state for block in line])
        return np.array(states)

    @staticmethod
    def is_line_filled(line):
        return all(block.is_filled for block in line)

    @staticmethod
    def unpress_line(line):
        for block in line:
            block.unpress()

    def get_replacers(self, lines: List[int]) -> Tuple[List, List]:
        closest_lines, farthest_lines = [], []
        for i in lines:
            if i < 5:
                closest_lines.append([BlockCore.STATE_UNPRESSED] * self.n)
            else:
                farthest_lines.append([BlockCore.STATE_UNPRESSED] * self.n)
        return closest_lines, farthest_lines

    def roll_empty_lines(self, states, lines: List[int]) -> np.ndarray:
        closest_lines, farthest_lines = self.get_replacers(lines)
        new_states = closest_lines
        for i, line in enumerate(states):
            if i not in lines:
                new_states.append(line)
        new_states += farthest_lines
        return np.array(new_states)

    def transform_grid(self, rows, cols):
        _new_states = self.roll_empty_lines(self._states, rows)
        _new_states = self.roll_empty_lines(_new_states.T, cols)  # TODO: this doesn't work :|
        new_states = _new_states.T
        for i in range(self.n):
            for j in range(self.n):
                block = self.grid[i][j]
                new_state = new_states[i][j]
                block.set_state(new_state)

    def update(self) -> int:
        rows, cols = [], []
        for i, row in enumerate(self.grid):
            if self.is_line_filled(row):
                self.unpress_line(row)
                rows.append(i)

        for j, col in enumerate(self.grid.T):
            if self.is_line_filled(col):
                self.unpress_line(col)
                cols.append(j)

        if rows or cols:
            self.transform_grid(rows, cols)
        return len(rows) + len(cols)

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
