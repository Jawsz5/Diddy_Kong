import pygame

WIDTH     =  50
HEIGHT    =  50

class Enemy(pygame.sprite.Sprite):
   def __init__(self, screen_w, screen_h, x, y):
       super(Enemy,self).__init__()
       self.surf = pygame.Surface((WIDTH, HEIGHT))
       self.surf.fill("black")
       self.rect = self.surf.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.screen_w = screen_w
       self.screen_h = screen_h


   def get_surface(self):
       return self.surf
   def get_rect(self):
       return self.rect
   def update(self):
       raise NotImplemented