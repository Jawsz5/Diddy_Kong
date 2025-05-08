import pygame
from Helper import animate

WIDTH     =  50
HEIGHT    =  50

class Enemy(pygame.sprite.Sprite):
   def __init__(self, x,y,w,h):
       super(Enemy,self).__init__()
       self.image = pygame.image.load("Characters/Enemy/Enemy_Stationary.png")
       size = (w, h)
       self.image = pygame.transform.scale(self.image, size)
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.velX = 0
       self.turn = 0
       self.animations = [
           self.image,
           pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/jump.png"), size), #These will never get called
           pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/fall.png"), size),#These will never get called
           pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy_Moving_Right1.png"), size),
           pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy_Moving_Right2.png"), size),
           pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy_Moving_Left1.png"), size),
           pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy_Moving_Left2.png"), size),]


   def get_surface(self):
       return self.image
   def get_rect(self):
       return self.rect
   def update(self):
       if self.turn == 1:
           self.velX = -2
       else:
           self.velX = 2

       if self.rect.x > 800:
           self.turn = 1

       if self.rect.x < 0:
           self.turn = 0

       self.rect.x += self.velX

       animate(self, self.velX, 0, self.animations)

