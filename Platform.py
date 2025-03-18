import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill('Brown')
        self.image.set_colorkey('Brown')
        pygame.draw.rect(self.image, color, pygame.Rect(100, 100, 50, 50))
        self.rect = self.image.get_rect()
        '''
        super(Platform, self).__init__()
        self.surface = pygame.Surface((100, 100))
        self.surface.fill("Brown")
        self.rect = self.surface.get_rect()
        self.x = x
        self.y = y
        '''


    """

    def get_surface(self):
        return self.surface

    def get_rect(self):
        return self.rect

    def update(self):
        pass
    """
