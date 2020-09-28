import core
import pygame


class Block:
    def __init__(self, screen, x, y, i, j, state=core.State.UNPRESSED, width=49, height=49):
        self.screen = screen
        self.x, self.y = x, y
        self.i, self.j = i, j
        self.state = state
        self.width, self.height = width, height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.draw()

    @property
    def is_pressed(self):
        return self.state == core.State.PRESSED

    @property
    def is_filled(self):
        return self.state == core.State.FILLED

    def _update(self):
        color = core.State.to_color(self.state)
        pygame.draw.rect(self.screen, color, self.rect)

    def press(self):
        self.state = core.State.PRESSED
        self._update()

    def unpress(self):
        self.state = core.State.UNPRESSED
        self._update()

    def fill(self):
        self.state = core.State.FILLED
        self._update()

    def remove(self):
        self.state = core.State.REMOVED
        self._update()

    def set_state(self, state):
        self.state = state
        self._update()

    def draw(self):
        self._update()

    def __str__(self):
        return f"x: {self.x}, y: {self.y}, i: {self.i}, j: {self.j}"
