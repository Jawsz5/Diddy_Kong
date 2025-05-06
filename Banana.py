import pygame

from Helper import animate


class Banana(pygame.sprite.Sprite):
    def __init__(self,x,y,w,h):
        super(Banana, self).__init__()
        self.image = pygame.image.load("Bananas/Banana.png")
        size = (w,h)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velX = 0
        self.velY = 0
        self.animations = [self.image, 0, 0,
        pygame.transform.scale(pygame.image.load("Bananas/banana1.png"), size),
        pygame.transform.scale(pygame.image.load("Bananas/banana2.png"), size),
        pygame.transform.scale(pygame.image.load("Bananas/banana1.png"), size),
        pygame.transform.scale(pygame.image.load("Bananas/banana2.png"), size)]

    def get_surface(self):
        return self.image

    def get_rect(self):
        return self.rect

    def update_velX(self, n):
        #only moves horizontally
        self.velX = n

    def update(self):
        self.rect.x += self.velX
        animate(self, self.velX, self.velY, self.animations)
