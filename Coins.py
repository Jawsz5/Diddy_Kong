import pygame

class Coins(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        super(Coins, self).__init__()
        self.image = pygame.image.load("Bananas/Banana.png")
        self.image = pygame.transform.scale(self.image, (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def get_surface(self):
        return self.image

    def get_rect(self):
        return self.rect
