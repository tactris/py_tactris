import numpy as np
import pygame
from shapes import ALL_SHAPES

WHITE = (229, 229, 229)
BLUE = (170, 221, 255)
BLACK = (0, 0, 0)
GRAY = (51, 51, 51)


class SmartStack:
    def __init__(self, size):
        self.size = size
        self._data = []

    def append(self, elem):
        self._data.append(elem)
        if len(self._data) > self.size:
            return self._data.pop(0)

    def remove(self, elem):
        self._data.remove(elem)

    def clear(self):
        self._data = []

    def __iter__(self):
        return iter(self._data)

    def __bool__(self):
        return bool(self._data)


class Block:

    FILLED = WHITE
    PRESSED = BLUE
    UNPRESSED = BLACK

    def __init__(self, screen, x, y, i, j):
        self.screen = screen
        self.x, self.y = x, y
        self.i, self.j = i, j
        self.is_pressed = False
        self.is_filled = False
        self.width, self.height = 49, 49
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def press(self):
        pygame.draw.rect(self.screen, self.PRESSED, self.rect)
        self.is_pressed = True

    def unpress(self):
        pygame.draw.rect(self.screen, self.UNPRESSED, self.rect)
        self.is_pressed = False

    def fill(self):
        pygame.draw.rect(self.screen, self.FILLED, self.rect)
        self.is_pressed = False
        self.is_filled = True

    def unfill(self):
        pygame.draw.rect(self.screen, self.UNPRESSED, self.rect)
        self.is_filled = False

    def draw(self):
        pygame.draw.rect(self.screen, self.UNPRESSED, self.rect)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, i: {self.i}, j: {self.j}"


class WorkingArea:
    def __init__(self):
        self.area = []
        self.stack = SmartStack(4)

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

    def figure_match(self):
        return self.hash in ALL_SHAPES

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

        if self.figure_match():
            self.fill_figure()
            self.stack.clear()
            return True
        return False

    def fill_figure(self):
        for line in self.area:
            for block in line:
                if block.is_pressed:
                    block.fill()

    @property
    def hash(self):
        return "".join("1" if b.is_pressed else "0" for line in self.area for b in line)


class Grid:
    def __init__(self, screen, n=10):
        self.n = n
        self.grid: np.ndarray
        self.screen = screen
        self.stack = SmartStack(4)
        self.working_area = WorkingArea()

    @staticmethod
    def is_line_filled(line):
        return all(block.is_filled for block in line)

    def tactris(self, blocks):
        for block in blocks:
            block.unfill()

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

    def draw(self):
        grid = []
        x, y = 0, 0
        for i in range(self.n):
            line = []
            for j in range(self.n):
                block = Block(self.screen, x, y, i, j)
                block.draw()
                line.append(block)
                x += 50
            grid.append(line)
            x = 0
            y += 50
        self.grid = np.array(grid)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), 0, 32)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Tactris")

    running = True

    screen.fill(GRAY)
    field = Grid(screen)
    field.draw()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                field.click(*pos)

            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.


if __name__ == "__main__":
    main()
