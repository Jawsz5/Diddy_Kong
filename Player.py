import time

import pygame
from Helper import animate
from HealthBar import HealthBar

SPEED  =  2
WIDTH  = 100
HEIGHT = 100
size = (WIDTH, HEIGHT)

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
    def __init__(self, screen_w, screen_h, x, y):
        super(Player, self).__init__()
        image = pygame.image.load("Characters/DIDDY_KONG/stationary.png").convert_alpha()
        self.image = pygame.transform.scale(image, size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.gravity = 1
        self.velY = 0
        self.velX = 0
        self.on_ground = True
        self.jump_count = 2  # Allow 2 jumps: initial jump + double jump
        self.prev_jump_pressed = False  # Tracks previous jump key state
        self.double_jumped = False
        self.switch = True
        self.rate = 15
        self.r_final = 10
        # Flag for whether a double jump has been used
        self.animations = [
            self.image,
            pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/jump.png"), size),
            pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/fall.png"), size),
            pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/right1.png"), size),
            pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/right2.png"), size),
            pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/left1.png"), size),
            pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/left2.png"), size)]
        self.hp = 100
        self.start_time = time.time()
        self.bounce_time = time.time()
        self.bounce_end = time.time()
        self.t = False

    def get_surface(self):
        return self.image

    def get_rect(self):
        return self.rect

    def player_hit(self, object, v):
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        if self.rect.colliderect(object.rect):
            if elapsed_time > 2:
                self.hp -= v
                self.start_time = time.time()

    def bounce(self, Sprite_group):
        for sprite in Sprite_group.copy():
            if self.velY > 5 and self.rect.colliderect(sprite.rect):
                self.velX = 0
                self.velY *= -1
                self.bounce_time = time.time()
                self.jump_count = 2
                self.on_ground = False
                Sprite_group.remove(sprite)
                self.t = True
                return 1
        if self.t and time.time() - self.bounce_time > 0.1:
            self.t = False
        return 0

    def update(self, pressed_keys, platforms):
        # --- Vertical Movement and Collision ---
        # Apply gravity if not on the ground
        self.gravity = 0.5
        if not self.on_ground:
            self.velY += self.gravity
        self.rect.y += self.velY
        #pass the hit boxes of platforms into the sprite collide function
        def collide_hitbox(player, platform):
            """Return True when player's visual rect touches platform.hitbox."""
            return player.rect.colliderect(platform.hitbox)
        collided_platforms = pygame.sprite.spritecollide(self, platforms, False, collide_hitbox)
        for platform in collided_platforms:
            if self.velY > 0:  # Falling down
                #print(platform.hitbox.top, platform.hitbox.bottom)
                self.rect.bottom = platform.hitbox.top
                self.velY = 0
                self.jump_count = 2  # Reset jumps when landing
                self.double_jumped = False
            elif self.velY < 0:  # Moving upward (jumping)
                self.rect.top = platform.hitbox.bottom
                self.velY = 0
        # --- Jump Logic ---
        current_jump_pressed = pygame.key.get_pressed()[pressed_keys[0]]
        if current_jump_pressed and not self.prev_jump_pressed:
            if self.jump_count > 0:
                self.velY = -12
                self.jump_count -= 1
                self.on_ground = False
                if self.jump_count == 0:
                    self.double_jumped = True
        self.prev_jump_pressed = current_jump_pressed

        # Horizontal Movement and Collision
        old_x = self.rect.x
        if pygame.key.get_pressed()[pressed_keys[2]]:
            self.rect.x -= 5
        if pygame.key.get_pressed()[pressed_keys[3]]:
            self.rect.x += 5
        self.velX = self.rect.x - old_x

        # Check horizontal collisions
        collided_platforms = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collided_platforms:
            # Moving right: adjust right side of player

            # TODO ask mourya what this is for. IDR putting it in
            '''
            if self.rect.x > old_x:
                self.rect.right = platform.rect.left
            # Moving left: adjust left side of player
            elif self.rect.x < old_x:
                self.rect.left = platform.rect.right
            '''

        # Ground and Screen Boundary Collision
        # Check collision with the ground (assuming ground level is 750)
        if self.rect.bottom > 750:
            self.rect.bottom = 750
            self.velY = 0
            self.on_ground = True
            self.jump_count = 2
            self.double_jumped = False

        # Prevent the player from going off-screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_w:
            self.rect.right = self.screen_w
        if self.rect.top < 0:
            self.rect.top = 0

        #animation
        animate(self, self.velX, self.velY, self.animations)






