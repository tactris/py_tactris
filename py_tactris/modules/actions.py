import core


class Button:
    def __init__(self, screen, x, y):
        self.x, self.y = x, y
        self.screen = screen
        self.state = core.ButtonState.NORMAL
        self.draw()

    @property
    def is_state_normal(self):
        return self.state == core.ButtonState.NORMAL

    @property
    def is_state_hover(self):
        return self.state == core.ButtonState.HOVER

    def _update(self):
        color = core.ButtonState.to_color(self.state)
        text_surface, _ = core.Font.BUTTON_FONT.render(self.TEXT, color, core.Color.GRAY)  # noqa
        self.screen.blit(text_surface, (self.x, self.y))

    def hover(self):
        if self.is_state_normal:
            self.state = core.ButtonState.HOVER
            self._update()

    def normal(self):
        if self.is_state_hover:
            self.state = core.ButtonState.NORMAL
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
        self.rev_x, self.rev_y = 515, 200
        self.res_x, self.res_y = 515, 235
        self.screen = screen
        self.button_revert: ButtonRevert
        self.button_restart: ButtonRestart
        self.draw()

    def update(self, x, y):
        if 515 < x < 605 and 200 < y < 235:
            self.button_revert.hover()
        else:
            self.button_revert.normal()

        if 515 < x < 605 and 235 < y < 270:
            self.button_restart.hover()
        else:
            self.button_restart.normal()

    def click(self, x, y):
        if 515 < x < 605 and 200 < y < 235:
            return self.ACTION_REVERT
        elif 515 < x < 605 and 235 < y < 270:
            return self.ACTION_RESTART

    def draw(self):
        self.button_revert = ButtonRevert(self.screen, self.rev_x, self.rev_y)  # noqa
        self.button_restart = ButtonRestart(self.screen, self.res_x, self.res_y)  # noqa
