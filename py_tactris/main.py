import pygame
from core import GRAY
from grid import Grid
from sidebar import Sidebar


class Tactris:
    def __init__(self, screen):
        self.screen = screen
        self.sidebar = None
        self.grid = None
        self.draw()

    def click(self, x, y):
        if x <= 500 and y <= 500:
            self.grid.click(x, y)

    def draw(self):
        self.screen.fill(GRAY)
        self.sidebar = Sidebar(self.screen)
        self.grid = Grid(self.screen, self.sidebar)


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
