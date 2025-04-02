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

    def update(self, pressed_keys):
        # Gravity acceleration (constant downward force)
        self.gravity = 0.5

        # Apply gravity when not on the ground
        if not self.on_ground:
            self.velY += self.gravity

        # Apply vertical movement
        self.rect.move_ip(0, self.velY)

        # Jump logic with keydown detection for double jump:
        current_jump_pressed = pygame.key.get_pressed()[pressed_keys[0]]
        if current_jump_pressed and not self.prev_jump_pressed:
            if self.jump_count > 0:
                self.velY = -12
                self.jump_count -= 1
                self.on_ground = False
                # Set flag if this was the double jump
                if self.jump_count == 0:
                    self.double_jumped = True
        self.prev_jump_pressed = current_jump_pressed

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
            self.jump_count = 2   # Reset jump count upon landing
            self.double_jumped = False

        # Visual feedback to show jump state:
        # - On ground: Black
        # - First jump: Red
        # - Double jump executed: Blue


        # Prevent player from going off-screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_w:
            self.rect.right = self.screen_w
        if self.rect.top < 0:
            self.rect.top = 0

