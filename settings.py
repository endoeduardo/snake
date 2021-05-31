class Settings():
    """Configurações do jogo"""
    def __init__(self):
        #Configurações da tela
        self.screen_width, self.screen_height = 800, 600
        self.bg_color = 0, 0, 0

        #Configurações da maçã
        self.apple_width, self.apple_height = 10, 10
        self.apple_color = 255, 0, 0

        #Configurações da cobra
        self.snake_width, self.snake_height = 10, 10
        self.snake_color = 255, 255, 255
        #Quantas segmentos a cobra ganha ao comer uma maçã
        self.snake_add = 4

