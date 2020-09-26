import pygame.freetype

WHITE = (229, 229, 229)
BLUE = (170, 221, 255)
BLACK = (0, 0, 0)
GRAY = (51, 51, 51)

BACKGROUND_COLOR = (51, 51, 51)

pygame.freetype.init()
FONT_SCORE = pygame.freetype.Font("font/HelveticaNeueCyr-Light.ttf", 14)
FONT_BUTTON = pygame.freetype.Font("font/HelveticaNeueCyr-Light.ttf", 17)


class BLOCK_STATE:  # noqa
    FILLED = WHITE
    PRESSED = BLUE
    UNPRESSED = BLACK
    REMOVED = GRAY


class BUTTON_STATE:  # noqa
    NORMAL = BLUE
    HOVER = WHITE
