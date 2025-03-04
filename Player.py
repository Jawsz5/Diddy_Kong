import pygame

SPEED  =  2
WIDTH  = 50
HEIGHT = 50


from pygame.locals import (
   K_UP,
   K_DOWN,
   K_LEFT,
   K_RIGHT,
)


UP = K_UP
DOWN = K_DOWN
LEFT = K_LEFT
RIGHT = K_RIGHT


class Player(pygame.sprite.Sprite):
   def __init__(self, screen_w, screen_h, x, y):
       super(Player, self).__init__()
       self.surf = pygame.Surface((WIDTH, HEIGHT))
       self.surf.fill("Black")
       self.rect = self.surf.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.screen_w = screen_w
       self.screen_h = screen_h


   def get_surface(self):
       return self.surf
   def get_rect(self):
       return self.rect
   # Move the sprite based on user keypresses
   def update(self, pressed_keys):
       if pressed_keys[UP]:
           self.rect.move_ip(0, -SPEED)
       if pressed_keys[DOWN]:
           self.rect.move_ip(0, SPEED)
       if pressed_keys[LEFT]:
           self.rect.move_ip(-SPEED, 0)
       if pressed_keys[RIGHT]:
           self.rect.move_ip(SPEED, 0)


       # Keep player on the screen
       if self.rect.left < 0:
           self.rect.left = 0
       if self.rect.right > self.screen_w:
           self.rect.right = self.screen_w
