import pygame.draw

from constants import DIRECTION_RIGHT, DIRECTION_LEFT, DIRECTION_UP, DIRECTION_DOWN, SNAKE_SECONDS_TO_STEP
from game_object import GameObject


class SnakeTail:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Snake(GameObject):
    tails: [SnakeTail] = []

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
        # Tail
        if len(self.tails) < self.food_eaten:
            last_tail_x = self.tails[0].x if len(self.tails) > 0 else self.x
            last_tail_y = self.tails[0].y if len(self.tails) > 0 else self.y

            self.tails.append(
                SnakeTail(
                    x=last_tail_x,
                    y=last_tail_y,
                )
            )

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
            previous_x = self.x
            previous_y = self.y

            self.delta_movement = 0
            if self.direction == DIRECTION_RIGHT:
                self.x += 1
            elif self.direction == DIRECTION_LEFT:
                self.x -= 1
            elif self.direction == DIRECTION_UP:
                self.y -= 1
            elif self.direction == DIRECTION_DOWN:
                self.y += 1

            for tail in self.tails:
                temp_tail_x = tail.x
                temp_tail_y = tail.y

                tail.x = previous_x
                tail.y = previous_y

                previous_x = temp_tail_x
                previous_y = temp_tail_y

    def draw(self, screen):
        grid_x = self.x * self.rect_size
        grid_y = self.y * self.rect_size

        pygame.draw.rect(
            surface=screen,
            color="yellow",
            rect=(grid_x, grid_y, self.rect_size, self.rect_size),
            width=0,
        )

        for tail in self.tails:
            grid_x = tail.x * self.rect_size
            grid_y = tail.y * self.rect_size

            pygame.draw.rect(
                surface=screen,
                color="yellow",
                rect=(grid_x, grid_y, self.rect_size, self.rect_size),
                width=0,
            )
