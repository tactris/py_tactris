import pygame
from core import BlockCore


class Block:
    def __init__(self, screen, x, y, i, j, state=BlockCore.STATE_UNPRESSED, width=49, height=49):
        self.screen = screen
        self.x, self.y = x, y
        self.i, self.j = i, j
        self.state = state
        self.width, self.height = width, height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.draw()

    @property
    def is_pressed(self):
        return self.state == BlockCore.STATE_PRESSED

    @property
    def is_filled(self):
        return self.state == BlockCore.STATE_FILLED

    def _update(self):
        color = BlockCore.to_color(self.state)
        pygame.draw.rect(self.screen, color, self.rect)

    def press(self):
        self.state = BlockCore.STATE_PRESSED
        self._update()

    def unpress(self):
        self.state = BlockCore.STATE_UNPRESSED
        self._update()

    def fill(self):
        self.state = BlockCore.STATE_FILLED
        self._update()

    def remove(self):
        self.state = BlockCore.STATE_REMOVED
        self._update()

    def set_state(self, state):
        self.state = state
        self._update()

    def draw(self):
        self._update()

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, i: {self.i}, j: {self.j}"
