import pygame.freetype
from core import BACKGROUND_COLOR, BLUE, WHITE

pygame.freetype.init()


class TopInfo:
    FONT = pygame.freetype.Font("font/HelveticaNeueCyr-Light.ttf", 14)

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x, self.y = x, y
        self.score = 0
        self.score_text_surface, self.rect = self.FONT.render("Счёт: ", WHITE, BACKGROUND_COLOR)
        self.score_value_surface, self.rect = self.FONT.render("0", BLUE, BACKGROUND_COLOR)
        self.draw()

    @staticmethod
    def calculate_score_incr(lines_removed: int):
        default_incr = 4
        lines_incr = lines_removed * 10 * lines_removed
        return default_incr + lines_incr

    def update(self, lines_removed: int):
        self.score += self.calculate_score_incr(lines_removed)
        self.score_value_surface, self.rect = self.FONT.render(str(self.score), BLUE, BACKGROUND_COLOR)
        self.screen.blit(self.score_value_surface, (self.x + 40, self.y))

    def draw(self):
        self.screen.blit(self.score_text_surface, (self.x, self.y))
        self.screen.blit(self.score_value_surface, (self.x + 40, self.y))
