import pygame
from Helper import animate

WIDTH     =  50
HEIGHT    =  50

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, platforms, animations):
        super(Enemy, self).__init__()
        self.image = animations[0]
        size = (w, h)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velX = 0
        self.turn = 0
        self.switch = True
        self.rate = 15
        self.r_final = 10
        self.animations = animations
        self.hp = 30

        self.platform_bounds = self.get_platform_bounds(platforms)

    def get_platform_bounds(self, platforms):
        for platform in platforms:
            if platform.rect.colliderect(self.rect):
                return (platform.rect.left - 20, platform.rect.right - self.rect.width + 20)
        # Default fallback if not on a platform
        return (self.rect.x - 50, self.rect.x + 50)

    def get_surface(self):
        return self.image

    def get_rect(self):
        return self.rect

    def update(self):
        left_bound, right_bound = self.platform_bounds

        if self.turn == 1:
            self.velX = -2
        else:
            self.velX = 2

        if self.rect.x > right_bound:
            self.turn = 1

        if self.rect.x < left_bound:
            self.turn = 0

        self.rect.x += self.velX

        animate(self, self.velX, 0, self.animations)
