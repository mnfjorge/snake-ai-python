from pygame import Surface

from food import Food
from snake import Snake


def check_collision_with_screen(snake: Snake, max_x: int, max_y: int):
    return snake.x < 0 or snake.y < 0 or snake.x > max_x or snake.y > max_y


def check_collision_with_food(snake: Snake, food: Food):
    return food.alive and snake.x == food.x and snake.y == food.y
