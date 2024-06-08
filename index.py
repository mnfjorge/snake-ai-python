import math

import pygame

from collision import check_collision_with_screen, check_collision_with_food
from food import Food
from grid import Grid
from snake import Snake
from ui import render_score, render_game_over

FPS = 60

pygame.init()
screen: pygame.Surface = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
game_over = False
clock_delta = 0

screen_ratio = screen.get_width() / screen.get_height()
grid_size = 10
rect_size = math.floor(screen.get_width() / grid_size)

grid = Grid(
    horizontal=grid_size,
    vertical=grid_size,
    step=rect_size,
)

snake = Snake(
    grid_size=grid_size,
    rect_size=rect_size,
    x=round(grid_size / 2)-1,
    y=round(grid_size / 2)-1,
)

food = Food(
    rect_size=rect_size,
    max_x=grid_size-1,
    max_y=grid_size-1,
)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # Tick
        grid.tick(clock_delta)
        snake.tick(clock_delta)
        food.tick(clock_delta)

        # Food
        if check_collision_with_food(snake, food):
            food.kill()
            snake.eat()

    # Game over
    if check_collision_with_screen(snake, grid.horizontal - 1, grid.vertical - 1):
        print("Game over")
        game_over = True

    # Draw
    screen.fill("black")
    grid.draw(screen)
    snake.draw(screen)
    food.draw(screen)

    render_score(screen, snake.food_eaten)

    if game_over:
        render_game_over(screen)

    pygame.display.flip()
    clock_delta = clock.tick(FPS) / 1000

pygame.quit()
