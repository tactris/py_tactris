import pygame.freetype

WHITE = (229, 229, 229)
BLUE = (170, 221, 255)
BLACK = (0, 0, 0)
GRAY = (51, 51, 51)

BG_COLOR = (51, 51, 51)

pygame.freetype.init()


class BlockCore:
    STATE_PRESSED = "pressed"
    STATE_UNPRESSED = "unpressed"
    STATE_FILLED = "filled"
    STATE_REMOVED = "removed"

    STATE_TO_COLOR = {STATE_PRESSED: BLUE, STATE_UNPRESSED: BLACK, STATE_FILLED: WHITE, STATE_REMOVED: GRAY}

    @classmethod
    def to_color(cls, state):
        return cls.STATE_TO_COLOR[state]


class ButtonCore:
    BG_COLOR = GRAY
    FONT = pygame.freetype.Font("font/HelveticaNeueCyr-Light.ttf", 17)

    STATE_NORMAL = "normal"
    STATE_HOVER = "hover"

    SATE_TO_COLOR = {STATE_NORMAL: BLUE, STATE_HOVER: WHITE}

    @classmethod
    def to_color(cls, state):
        return cls.SATE_TO_COLOR[state]


class TopInfoCore:
    BG_COLOR = GRAY
    TITLE_COLOR = WHITE
    SCORE_COLOR = BLUE

    FONT = pygame.freetype.Font("font/HelveticaNeueCyr-Light.ttf", 14)
