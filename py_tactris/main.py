import pygame
import pygame.freetype
from core import BG_COLOR
from modules import Actions, Grid, ShapeChoice, TopInfo


class Tactris:
    def __init__(self, screen):
        self.screen = screen
        self.top_info: TopInfo
        self.shape_choice: ShapeChoice
        self.actions: Actions
        self.grid: Grid
        self.draw()

    def restart(self):
        max_score = self.top_info.max_score
        self.draw(max_score)

    def revert(self):
        pass

    def mouse(self, x, y):
        """
        Handler for mouse-movement events
        """
        self.actions.update(x, y)

    def mouse_up(self, x, y):
        """
        Handler for mouse UP events
        """
        shape_hash, lines_removed = self.grid.mouse_up()
        if shape_hash:
            self.shape_choice.update(shape_hash)
            self.top_info.update(lines_removed)
            self.grid.set_shapes(self.shape_choice.shapes)

        action = self.actions.click(x, y)
        if action:
            if action == Actions.ACTION_RESTART:
                self.restart()
            elif action == Actions.ACTION_REVERT:
                self.revert()

    def mouse_down(self, x, y):
        """
        Handler for mouse DOWN events
        """
        self.grid.mouse_down(x, y)

    def draw(self, max_score=0):
        self.screen.fill(BG_COLOR)
        self.top_info = TopInfo(self.screen, max_score=max_score)  # noqa
        self.actions = Actions(self.screen)  # noqa
        self.shape_choice = ShapeChoice(self.screen)  # noqa
        self.grid = Grid(self.screen, self.shape_choice.shapes)  # noqa


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600), 0, 32)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Tactris")

    running = True

    tactris = Tactris(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                tactris.mouse_up(*pos)

            if event.type == pygame.QUIT:
                running = False

        mouse_pos = pygame.mouse.get_pos()
        tactris.mouse(*mouse_pos)

        mouse_pressed, *_ = pygame.mouse.get_pressed()
        if mouse_pressed:
            tactris.mouse_down(*mouse_pos)

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.


if __name__ == "__main__":
    main()
