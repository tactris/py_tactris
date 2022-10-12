import pickle
from typing import Tuple

import core
import numpy as np
import pygame
import pygame.freetype
from modules import Actions, Grid, ShapeChoice, TopInfo
from shapes import Shape, get_random_shape


class GameState:
    def __init__(self, blocks_states: np.ndarray, shapes: Tuple[Shape, Shape], score: int):
        self.blocks_states = blocks_states
        self.shapes = shapes
        self.score = score
        self.dump()

    def dump(self):
        with open(".t_session.pickle", "wb") as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    @classmethod
    def load(cls):
        try:
            with open(".t_session.pickle", "rb") as f:
                data = pickle.load(f)
        except FileNotFoundError:
            shape1 = get_random_shape()
            shape2 = get_random_shape(shape1)
            data = GameState(blocks_states=np.full((10, 10), False), shapes=(shape1, shape2), score=0)
        return data


class Tactris:
    def __init__(self, screen):
        self.screen = screen
        self.game_state: GameState
        self.top_info: TopInfo
        self.shape_choice: ShapeChoice
        self.actions: Actions
        self.grid: Grid
        self.draw()

    def restart(self):
        max_score = self.top_info.max_score
        self.draw(max_score)

    def save_game(self):
        blocks_states = self.grid.get_blocks_states()
        self.game_state = GameState(blocks_states, self.shape_choice.shapes, self.top_info.score)  # noqa

    def revert(self):
        if self.game_state:
            blocks_states = self.game_state.blocks_states
            score = self.game_state.score
            shapes = self.game_state.shapes
            self.save_game()
            self.grid.set_blocks_states(blocks_states)
            self.top_info.set_score(score)
            self.shape_choice.set_shapes(*shapes)
            self.grid.set_shapes(*shapes)

    def mouse(self, x, y):
        """
        Handler for mouse-movement events
        """
        self.actions.update(x, y)

    def mouse_up(self, x, y):
        """
        Handler for mouse UP events
        """
        matched_shape = self.grid.mouse_up()
        if matched_shape:
            self.save_game()
            lines_removed = self.grid.update()
            self.shape_choice.update(matched_shape)
            self.top_info.update(lines_removed)
            self.grid.set_shapes(*self.shape_choice.shapes)

        action = self.actions.click(x, y)
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
        self.screen.fill(core.Color.GRAY)
        self.game_state = GameState.load()  # noqa
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
