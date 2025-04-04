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
    def __init__(self, screen_w, screen_h, x, y):
        super(Player, self).__init__()
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
        self.jump_count = 2  # Allow 2 jumps: initial jump + double jump
        self.prev_jump_pressed = False  # Tracks previous jump key state
        self.double_jumped = False      # Flag for whether a double jump has been used

    def get_surface(self):
        return self.surf

    def get_rect(self):
        return self.rect

    def update(self, pressed_keys, platforms):
        # --- Vertical Movement and Collision ---
        # Apply gravity if not on the ground
        self.gravity = 0.5
        if not self.on_ground:
            self.velY += self.gravity
        self.rect.y += self.velY

        # Check vertical collisions
        collided_platforms = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collided_platforms:
            if self.velY > 0:  # Falling down
                self.rect.bottom = platform.rect.top
                self.velY = 0
                self.jump_count = 2  # Reset jumps when landing
                self.double_jumped = False
            elif self.velY < 0:  # Moving upward (jumping)
                self.rect.top = platform.rect.bottom
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

        # --- Horizontal Movement and Collision ---
        old_x = self.rect.x
        if pygame.key.get_pressed()[pressed_keys[2]]:
            self.rect.x -= 5
        if pygame.key.get_pressed()[pressed_keys[3]]:
            self.rect.x += 5

        # Check horizontal collisions
        collided_platforms = pygame.sprite.spritecollide(self, platforms, False)
        for platform in collided_platforms:
            # Moving right: adjust right side of player
            if self.rect.x > old_x:
                self.rect.right = platform.rect.left
            # Moving left: adjust left side of player
            elif self.rect.x < old_x:
                self.rect.left = platform.rect.right

        # --- Ground and Screen Boundary Collision ---
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
