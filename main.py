import pygame
import game_functions as gf
from settings import Settings
from objects import Apple
from objects import Snake


def run_game():
    pygame.init()
    settings = Settings()
    pygame.display.set_caption("Snake_mk2")
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    apple = Apple(settings)
    snake = Snake(settings)
    clock = pygame.time.Clock()
    while True:
        clock.tick(20)
        gf.check_events(snake)
        gf.update_screen(settings, screen, apple, snake)
        gf.check_snake_apple_pos(settings, apple, snake)
        gf.check_collisions(settings, apple, snake)


run_game()