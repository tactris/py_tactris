from core import BACKGROUND_COLOR, BUTTON_STATE, FONT_BUTTON
from pygame.surface import Surface


class Actions:

    ACTION_RESTART = "restart"
    ACTION_REVERT = "revert"

    def __init__(self, screen, x, y):
        self.x, self.y = x, y
        self.screen = screen
        self.text_surface: Surface
        self.state = BUTTON_STATE.NORMAL
        self.draw()

    def _update(self):
        self.text_surface, _ = FONT_BUTTON.render("Новая игра", self.state, BACKGROUND_COLOR)
        self.screen.blit(self.text_surface, (self.x, self.y))

    def hover(self):
        self.state = BUTTON_STATE.HOVER
        self._update()

    def normal(self):
        self.state = BUTTON_STATE.NORMAL
        self._update()

    def update(self, x, y):
        if 605 > x > 515 and 200 > y > 165:
            self.state == BUTTON_STATE.NORMAL and self.hover()
        else:
            self.state == BUTTON_STATE.HOVER and self.normal()

    def click(self, x, y):
        if 605 > x > 515 and 200 > y > 165:
            return self.ACTION_RESTART

    def draw(self):
        self._update()
