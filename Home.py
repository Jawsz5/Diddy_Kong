import pygame

SCREENW = 800
SCREENH = 600

class Home():
    def __init__(self, screen):
        self.screen = pygame.display.set_mode((SCREENW, SCREENH))
        self.clock = pygame.time.Clock()

    def play_button(self):
        pass

    def rules_button(self):
        pass

    def settings_button(self):
        pass