import pygame
from core import STATES


class Block:
    def __init__(self, screen, x, y, i, j, state=STATES.UNPRESSED, width=49, height=49):
        self.screen = screen
        self.x, self.y = x, y
        self.i, self.j = i, j
        self.state = state
        self.width, self.height = width, height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.draw()

    @property
    def is_pressed(self):
        return self.state == STATES.PRESSED

    @property
    def is_filled(self):
        return self.state == STATES.FILLED

    def _update(self):
        pygame.draw.rect(self.screen, self.state, self.rect)

    def press(self):
        self.state = STATES.PRESSED
        self._update()

    def unpress(self):
        self.state = STATES.UNPRESSED
        self._update()

    def fill(self):
        self.state = STATES.FILLED
        self._update()

    def remove(self):
        self.state = STATES.REMOVED
        self._update()

    def draw(self):
        self._update()

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, i: {self.i}, j: {self.j}"
