import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, hit_box, img_rect, plat=None, color=(100, 100, 100)):
        super().__init__()
        # Create a surface with the given width and height.
        # 1)  collision area  (independent of the artwork)
        self.hitbox = pygame.Rect(hit_box)
        # 2)  artwork
        sx, sy, w, h = img_rect    # unpack the four values
        if plat is not None:
            # grab that sub‑image, copy it so the platform stays read‑only
            #self.image = plat.subsurface(pygame.Rect(hit_box)).copy()
            self.image = pygame.transform.scale(plat, (w, h))
        else:
            # if no image is passed, plain coloured rectangle
            self.image = pygame.Surface((w, h), pygame.SRCALPHA)
            self.image.fill(color)

        #self.image = pygame.transform.scale(plat, (w, h))
        # 3)  where to BLIT the image; use either of the 2 lines below, not both
        # the next line can be commented to decouple the image and rect
        #self.image_rect = self.image.get_rect(topleft=self.rect.topleft)
        self.image = pygame.transform.scale(plat, (w, h))
        # place the image manually
        self.rect = pygame.Rect(img_rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect)