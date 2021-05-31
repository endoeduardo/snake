import pygame
from random import randint


class Apple():
    """Configurações da maçã"""
    def __init__(self, settings):
        self.settings = settings

        #Criando uma surface pra maçã
        self.skin = pygame.Surface((self.settings.apple_width, self.settings.apple_height))
        self.skin.fill(self.settings.apple_color)

        #Gerando uma posição aleatória pra maçã
        self.pos = (randint(0, (settings.screen_width - 10))//10*10, randint(0, (settings.screen_height - 10))//10*10)


class Snake():
    """Configuração da cobra"""
    def __init__(self, settings):
        self.settings = settings

        #Criando uma suface para a cobra
        self.skin = pygame.Surface((self.settings.snake_width, self.settings.snake_height))
        self.skin.fill(self.settings.snake_color)

        #Lista que armazena a posição da cobra
        self.pos = [(settings.screen_width//2, settings.screen_height//2),
                     (settings.screen_width//2 + 10, settings.screen_height//2),
                     (settings.screen_width//2 + 20, settings.screen_height//2)]

        #Direção inicial da cobra
        self.snake_direction = "down"