import math

import pygame.draw

from constants import DIRECTION_RIGHT, DIRECTION_LEFT, DIRECTION_UP, DIRECTION_DOWN, SNAKE_SECONDS_TO_STEP
from game_object import GameObject


class Snake(GameObject):
    def __init__(self, grid_size, rect_size, x=0, y=0):
        self.grid_size=grid_size
        self.rect_size=rect_size
        self.x = x
        self.y = y
        self.direction = DIRECTION_RIGHT
        self.delta_movement = 0
        self.food_eaten = 0

    def eat(self):
        self.food_eaten += 1

    def tick(self, clock_delta):
        # User input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not self.direction == DIRECTION_LEFT:
            self.direction = DIRECTION_RIGHT
        if keys[pygame.K_LEFT] and not self.direction == DIRECTION_RIGHT:
            self.direction = DIRECTION_LEFT
        if keys[pygame.K_UP] and not self.direction == DIRECTION_DOWN:
            self.direction = DIRECTION_UP
        if keys[pygame.K_DOWN] and not self.direction == DIRECTION_UP:
            self.direction = DIRECTION_DOWN

        # Movement
        self.delta_movement += clock_delta
        if self.delta_movement > SNAKE_SECONDS_TO_STEP:
            self.delta_movement = 0
            if self.direction == DIRECTION_RIGHT:
                self.x += 1
            elif self.direction == DIRECTION_LEFT:
                self.x -= 1
            elif self.direction == DIRECTION_UP:
                self.y -= 1
            elif self.direction == DIRECTION_DOWN:
                self.y += 1

    def draw(self, screen):
        grid_x = self.x * self.rect_size
        grid_y = self.y * self.rect_size

        pygame.draw.rect(
            surface=screen,
            color="yellow",
            rect=(grid_x, grid_y, self.rect_size, self.rect_size),
            width=0,
        )
