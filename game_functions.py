import sys
import pygame
from random import choice


def update_screen(settings, screen, apple, snake):
    screen.fill(settings.bg_color)
    screen.blit(apple.skin, apple.pos)
    for pos in snake.pos:
        screen.blit(snake.skin, pos)
    update_snake(snake)
    pygame.display.flip()


def check_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake)


def check_keydown_events(event, snake):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_UP and snake.snake_direction != "down":
        snake.snake_direction = "up"
    elif event.key == pygame.K_DOWN and snake.snake_direction != "up":
        snake.snake_direction = "down"
    elif event.key == pygame.K_RIGHT and snake.snake_direction != "left":
        snake.snake_direction = "right"
    elif event.key == pygame.K_LEFT and snake.snake_direction != "right":
        snake.snake_direction = "left"


def update_snake(snake):
    """Atualiza a posição da cobra"""
    # Controla a  posição da cabeça
    if snake.snake_direction == "up":
        snake.pos[0] = (snake.pos[0][0], snake.pos[0][1] - 10)
    elif snake.snake_direction == "down":
        snake.pos[0] = (snake.pos[0][0], snake.pos[0][1] + 10)
    elif snake.snake_direction == "right":
        snake.pos[0] = (snake.pos[0][0] + 10, snake.pos[0][1])
    elif snake.snake_direction == "left":
        snake.pos[0] = (snake.pos[0][0] - 10, snake.pos[0][1])

    # Controla a posição do corpo da cobra
    for i in range(len(snake.pos) - 1, 0, -1):
        snake.pos[i] = (snake.pos[i - 1][0], snake.pos[i - 1][1])


def check_snake_apple_pos(settings, apple, snake):
    "Checa a posição e se há a colisão entre maçã e cobra"
    if apple.pos == snake.pos[0]:
        for c in range(0, settings.snake_add):
            snake.pos.append((0, 0))
        available_space = check_available_space(settings, snake)
        apple.pos = choice(available_space)


def check_collisions(settings, apple, snake):
    """Verifica se a cobra atingiu o canto da tela ou ela mesmo e reinicia a posição da maçã e da cobra"""
    if snake.pos[0][1] < 0 or settings.screen_height < snake.pos[0][1] or \
            settings.screen_width < snake.pos[0][0] or snake.pos[0][0] < 0:
        # Remove e centraliza a cobra caso tenha atingido um canto da tela
        snake.pos.clear()
        snake.pos = [(settings.screen_width // 2, settings.screen_height // 2),
                     (settings.screen_width // 2 + 10, settings.screen_height // 2),
                     (settings.screen_width // 2 + 20, settings.screen_height // 2)]
        available_space = check_available_space(settings, snake)
        apple.pos = choice(available_space)

    # Verifica se a cabeça da cobra atingiu alguma parte do corpo
    for i, pos in enumerate(snake.pos):
        if i > 5 and snake.pos[0] == pos:
            snake.pos.clear()
            snake.pos = [(settings.screen_width // 2, settings.screen_height // 2),
                         (settings.screen_width // 2 + 10, settings.screen_height // 2),
                         (settings.screen_width // 2 + 20, settings.screen_height // 2)]
            available_space = check_available_space(settings, snake)
            apple.pos = choice(available_space)


def create_grid_space(settings):
    grid_space = list()
    for y in range(0, settings.screen_height, 10):
        for x in range(0, settings.screen_width, 10):
            grid_space.append((x, y))
    return grid_space


def check_available_space(settings, snake):
    grid_space = create_grid_space(settings)
    for pos in snake.pos:
        try:
            grid_space.remove(pos)
        except:
            pass
    return grid_space
