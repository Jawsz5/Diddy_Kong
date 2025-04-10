import pygame
from Player import Player

width = 50
height = 50
SCREENW = 800
SCREENH = 800

class Treasure(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Treasure, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill("Gold")
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        background_images = [pygame.image.load("Characters/treasure.png"),
                             pygame.image.load("Characters/treasure_open.png")]
        image = background_images[0]

    def get_surface(self):
        return self.surf

    def get_rect(self):
        return self.rect

    def update(self):
        pass


