from random import randint

import pygame
from pygame import Surface

from constants import FOOD_SECONDS_TO_SPAWN
from game_object import GameObject


class Food(GameObject):
    def __init__(self, max_x: int, max_y: int, rect_size: int):
        self.alive = False
        self.x = 0
        self.y = 0
        self.max_x = max_x
        self.max_y = max_y
        self.rect_size = rect_size
        self.spawn_delta = 0

    def spawn(self):
        self.x = randint(0, self.max_x)
        self.y = randint(0, self.max_y)
        self.alive = True

    def kill(self):
        self.alive = False

    def tick(self, clock_delta: float):
        if not self.alive:
            self.spawn_delta += clock_delta

            if self.spawn_delta > FOOD_SECONDS_TO_SPAWN:
                self.spawn_delta = 0
                self.spawn()

    def draw(self, screen: Surface):
        if not self.alive:
            return

        grid_x = self.x * self.rect_size
        grid_y = self.y * self.rect_size

        pygame.draw.rect(
            surface=screen,
            color="brown",
            rect=(grid_x, grid_y, self.rect_size, self.rect_size),
            width=0,
        )
