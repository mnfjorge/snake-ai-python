import pygame

from constants import GRID_LINE_THICKNESS, GRID_RENDER
from game_object import GameObject


class Grid(GameObject):
    def __init__(self, horizontal, vertical, step):
        self.horizontal = horizontal
        self.vertical = vertical
        self.step = step

    def draw(self, screen):
        if not GRID_RENDER:
            return

        for x in range(1, self.horizontal):
            pygame.draw.line(
                surface=screen,
                color="white",
                start_pos=(x * self.step, 0),
                end_pos=(x * self.step, self.vertical * self.step),
                width=GRID_LINE_THICKNESS,
            )

        for y in range(1, self.vertical):
            pygame.draw.line(
                surface=screen,
                color="white",
                start_pos=(0, y * self.step),
                end_pos=(self.horizontal * self.step, y * self.step),
                width=GRID_LINE_THICKNESS,
            )

        # for y in range(0, self.height, self.step):
        # pygame.draw.rect(screen, color="white", rect=(self.x, self.y, self.width, self.height), width=1)
