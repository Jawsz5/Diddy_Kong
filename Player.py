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


W = K_UP
S = K_DOWN
A = K_LEFT
D = K_RIGHT


class Player(pygame.sprite.Sprite):
   def __init__(self, screen_w, screen_h, x, y,):
       super(Player,self).__init__()
       self.surf = pygame.Surface((WIDTH, HEIGHT))
       self.surf.fill("Black")
       self.rect = self.surf.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.screen_w = screen_w
       self.screen_h = screen_h
       self.gravity = 1
       self.velY = 0
       self.on_ground = True


   def get_surface(self):
       return self.surf
   def get_rect(self):
       return self.rect
   # Move the sprite based on user keypresses
   def update(self, pressed_keys):
       # Gravity acceleration (constant downward force)
       self.gravity = 0.5
       if not self.on_ground:
           self.velY += self.gravity  # Gradual increase in downward velocity

       # Apply vertical movement
       self.rect.move_ip(0, self.velY)

       # Jumping logic (key press, not hold)
       if pygame.key.get_pressed()[pressed_keys[0]] and self.on_ground:
           self.velY = -12  # Upward velocity for jump (adjust as needed)
           self.on_ground = False

       # Crouch (if needed)
       #if pygame.key.get_pressed()[pressed_keys[1]] and self.on_ground:
           #self.rect.move_ip(0, 100)  # Move player downward (adjust as needed)

       # Horizontal movement (left/right)
       if pygame.key.get_pressed()[pressed_keys[2]]:
           self.rect.move_ip(-5, 0)
       if pygame.key.get_pressed()[pressed_keys[3]]:
           self.rect.move_ip(5, 0)

       # Collision with ground (assuming 750 is ground level)
       if self.rect.bottom > 750:
           self.rect.bottom = 750
           self.velY = 0
           self.on_ground = True  # Player is back on the ground

       # Prevent player from going off-screen
       if self.rect.left < 0:
           self.rect.left = 0
       if self.rect.right > self.screen_w:
           self.rect.right = self.screen_w
       if self.rect.top < 0:
           self.rect.top = 0








