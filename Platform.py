import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, image_height=None, image_width=None, texture=None):
        super().__init__()
        # Create a surface with the given width and height.
        # Optionally fill with a background color if desired:
        # self.image.fill((0, 0, 0))   or another color
        self.rect = pygame.Rect(x, y, width, height)
        if texture is not None:
            if image_height is None or image_width is None:
                raise ValueError("image_height and image_width must be set")
            self.image = pygame.transform.scale(texture, (image_width, image_height))
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill((100,100,100))
        # Draw the platform rectangle starting at (0,0)
        # Get the rect from the image (which now matches the drawn platform)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
