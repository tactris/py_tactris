from enum import Enum
from typing import Tuple

import pygame.freetype

pygame.freetype.init()


class Color(Tuple, Enum):
    WHITE = (229, 229, 229)
    BLUE = (170, 221, 255)
    BLACK = (0, 0, 0)
    GRAY = (51, 51, 51)


class State(str, Enum):
    PRESSED = "pressed"
    UNPRESSED = "unpressed"
    FILLED = "filled"
    REMOVED = "removed"

    __STATE_TO_COLOR__ = {
        PRESSED: Color.BLUE,
        UNPRESSED: Color.BLACK,
        FILLED: Color.WHITE,
        REMOVED: Color.GRAY,
    }

    @classmethod
    def to_color(cls, state):
        return cls.__STATE_TO_COLOR__[state]

    def __str__(self):
        return self.value


class ButtonState(str, Enum):

    NORMAL = "normal"
    HOVER = "hover"

    __STATE_TO_COLOR__ = {NORMAL: Color.BLUE, HOVER: Color.WHITE}

    @classmethod
    def to_color(cls, state):
        return cls.__STATE_TO_COLOR__[state]


class Font:
    BUTTON_FONT = pygame.freetype.Font("font/HelveticaNeueCyr-Light.ttf", 17)
    TOP_INFO_FONT = pygame.freetype.Font("font/HelveticaNeueCyr-Light.ttf", 14)
