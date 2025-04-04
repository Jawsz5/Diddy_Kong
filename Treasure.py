import pygame

width = 50
height = 50

class Treasure(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Treasure, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill("Green")
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_surface(self):
        return self.surf

    def get_rect(self):
        return self.rect

    def update(self):
        pass


