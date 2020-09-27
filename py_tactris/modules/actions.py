from core import ButtonCore


class Button:
    def __init__(self, screen, x, y):
        self.x, self.y = x, y
        self.screen = screen
        self.state = ButtonCore.STATE_NORMAL
        self.draw()

    @property
    def is_state_normal(self):
        return self.state == ButtonCore.STATE_NORMAL

    @property
    def is_state_hover(self):
        return self.state == ButtonCore.STATE_HOVER

    def _update(self):
        color = ButtonCore.to_color(self.state)
        text_surface, _ = ButtonCore.FONT.render(self.TEXT, color, ButtonCore.BG_COLOR)  # noqa
        self.screen.blit(text_surface, (self.x, self.y))

    def hover(self):
        if self.is_state_normal:
            self.state = ButtonCore.STATE_HOVER
            self._update()

    def normal(self):
        if self.is_state_hover:
            self.state = ButtonCore.STATE_NORMAL
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
