import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill('Brown')
        self.image.set_colorkey('Brown')
        pygame.draw.rect(self.image, color, pygame.Rect(100, 100, height, width))
        self.rect = self.image.get_rect()
