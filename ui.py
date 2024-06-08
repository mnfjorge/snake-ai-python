import pygame
from pygame import Surface


font = pygame.font.Font('freesansbold.ttf', 32)


def render_score(screen: Surface, score: int):
    text = font.render(f"Score: {score}", True, "white")
    screen.blit(text, (10, 10))


def render_game_over(screen):
    text = font.render(f"GAME OVER", True, "red")
    screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - text.get_height() / 2))