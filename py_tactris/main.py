import pygame
from core import GRAY
from grid import Grid
from sidebar import Sidebar


class Tactris:
    def __init__(self, screen):
        self.screen = screen
        self.sidebar: Sidebar
        self.grid: Grid
        self.draw()

    def click(self, x, y):
        if x <= 500 and y <= 500:
            shape_matched = self.grid.click(x, y)
            if shape_matched:
                self.sidebar.update(shape_matched)
                self.grid.set_shapes(self.sidebar.shapes)

    def draw(self):
        self.screen.fill(GRAY)
        self.sidebar = Sidebar(self.screen)  # noqa
        self.grid = Grid(self.screen, self.sidebar.shapes)  # noqa


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
                tactris.click(*pos)

            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)  # Limit the frame rate to 60 FPS.


if __name__ == "__main__":
    main()
