import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, color, width, height, texture=None):
        super().__init__()
        # Create a surface with the given width and height.
        # Optionally fill with a background color if desired:
        # self.image.fill((0, 0, 0))   or another color
        if texture is not None:
            self.image = pygame.transform.scale(texture, (width, height))
        else:
            self.image = pygame.Surface((width, height))
        # Draw the platform rectangle starting at (0,0)
        # Get the rect from the image (which now matches the drawn platform)
        self.rect = self.image.get_rect()
