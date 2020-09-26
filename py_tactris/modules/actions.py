from core import BACKGROUND_COLOR, BUTTON_STATE, FONT_BUTTON


class Button:
    def __init__(self, screen, x, y):
        self.x, self.y = x, y
        self.screen = screen
        self.state = BUTTON_STATE.NORMAL
        self.draw()

    def _update(self):
        text_surface, _ = FONT_BUTTON.render(self.TEXT, self.state, BACKGROUND_COLOR)  # noqa
        self.screen.blit(text_surface, (self.x, self.y))

    def hover(self):
        if self.state == BUTTON_STATE.NORMAL:
            self.state = BUTTON_STATE.HOVER
            self._update()

    def normal(self):
        if self.state == BUTTON_STATE.HOVER:
            self.state = BUTTON_STATE.NORMAL
            self._update()

    def draw(self):
        self._update()


class ButtonRevert(Button):
    TEXT = "Отменить ход"


class ButtonRestart(Button):
    TEXT = "Новая игра"


class Actions:
    ACTION_REVERT = "revert"
    ACTION_RESTART = "restart"

    def __init__(self, screen):
        self.rev_x, self.rev_y = 515, 165
        self.res_x, self.res_y = 515, 200
        self.screen = screen
        self.button_revert: ButtonRevert
        self.button_restart: ButtonRestart
        self.draw()

    def update(self, x, y):
        if 605 > x > 515 and 200 > y > 165:
            self.button_revert.hover()
        else:
            self.button_revert.normal()

        if 605 > x > 515 and 235 > y > 200:
            self.button_restart.hover()
        else:
            self.button_restart.normal()

    def click(self, x, y):
        if 605 > x > 515 and 200 > y > 165:
            return self.ACTION_REVERT
        elif 605 > x > 515 and 235 > y > 200:
            return self.ACTION_RESTART

    def draw(self):
        self.button_revert = ButtonRevert(self.screen, self.rev_x, self.rev_y)  # noqa
        self.button_restart = ButtonRestart(self.screen, self.res_x, self.res_y)  # noqa
