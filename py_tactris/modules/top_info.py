from core import BACKGROUND_COLOR, BLUE, FONT_SCORE, WHITE


class TopInfo:
    def __init__(self, screen, max_score=0):
        self.screen = screen
        self.score_x, self.score_y = 515, 20
        self.max_score_x, self.max_score_y = self.score_x + 80, self.score_y
        self.score = 0
        self.max_score = max_score
        self.draw()

    def _update(self):
        score_value_surface, _ = FONT_SCORE.render(str(self.score), BLUE, BACKGROUND_COLOR)
        max_score_value_surface, _ = FONT_SCORE.render(str(self.max_score), BLUE, BACKGROUND_COLOR)
        self.screen.blit(score_value_surface, (self.score_x + 40, self.score_y))
        self.screen.blit(max_score_value_surface, (self.max_score_x + 55, self.max_score_y))

    @staticmethod
    def calculate_score_incr(lines_removed: int):
        default_incr = 4
        lines_incr = lines_removed * 10 * lines_removed
        return default_incr + lines_incr

    def update(self, lines_removed: int):
        score_incr = self.calculate_score_incr(lines_removed)
        self.score += score_incr
        if self.score > self.max_score:
            self.max_score += score_incr
        self._update()

    def draw(self):
        score_text_surface, _ = FONT_SCORE.render("Счёт: ", WHITE, BACKGROUND_COLOR)
        max_score_text_surface, _ = FONT_SCORE.render("Рекорд: ", WHITE, BACKGROUND_COLOR)
        self.screen.blit(score_text_surface, (self.score_x, self.score_y))
        self.screen.blit(max_score_text_surface, (self.max_score_x, self.max_score_y))
        self._update()
