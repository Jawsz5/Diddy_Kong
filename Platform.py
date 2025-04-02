import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        # Create a surface with the given width and height.
        self.image = pygame.Surface((width, height))
        # Optionally fill with a background color if desired:
        # self.image.fill((0, 0, 0))  # or another color
        # Draw the platform rectangle starting at (0,0)
        pygame.draw.rect(self.image, color, (0, 0, width, height))
        # Get the rect from the image (which now matches the drawn platform)
        self.rect = self.image.get_rect()
