import pygame

class Main:
    def __init__(self):
        SCREENSIZE = (800, 600)
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.clock = pygame.time.Clock()
    def new_game(self):

