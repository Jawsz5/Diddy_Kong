import pygame
from Button import Button
from Platform import Platform
from Player import Player
from HealthBar import HealthBar
from Level import Level
SCREENW = 800
SCREENH = 800

class Level3(Level):
    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        pygame.display.set_caption("Level 2")
        self.image = pygame.image.load("Backgrounds/Background_level3.png")
        self.image = pygame.transform.scale(self.image, (SCREENW, SCREENH))
        self.screen.blit(self.image, (0, 0))

    def add_sprite(self):
        all_sprites_list = pygame.sprite.Group()

        # Horizontal Platforms (20% smaller than original)
        plat_1 = Platform((255, 0, 0), 80, 90)  # originally (150, 200)
        plat_1.rect.x = 100
        plat_1.rect.y = 600
        all_sprites_list.add(plat_1)

        plat_2 = Platform((0, 255, 0), 110, 120)  # originally (200, 200)
        plat_2.rect.x = 400
        plat_2.rect.y = 550
        all_sprites_list.add(plat_2)

        plat_3 = Platform((0, 0, 255), 54, 98)  # originally (120, 200)
        plat_3.rect.x = 300
        plat_3.rect.y = 400
        all_sprites_list.add(plat_3)

        plat_4 = Platform((255, 255, 0), 92, 112)  # originally (180, 200)
        plat_4.rect.x = 50
        plat_4.rect.y = 300
        all_sprites_list.add(plat_4)

        plat_5 = Platform((0, 255, 255), 100, 64)  # originally (200, 150)
        plat_5.rect.x = 200
        plat_5.rect.y = 100
        all_sprites_list.add(plat_5)

        plat_6 = Platform((100, 100, 100), 95, 77)  # originally (200, 200)
        plat_6.rect.x = 500
        plat_6.rect.y = 300
        all_sprites_list.add(plat_6)

        return all_sprites_list
    def run(self):
        # Create the platforms group once outside the loop
        platforms = self.add_sprite()

        running = True
        while running:
            # Draw the background
            self.screen.blit(self.image, (0, 0))
            # Draw platforms
            platforms.draw(self.screen)
            # Draw the player
            self.screen.blit(self.player.get_surface(), self.player.get_rect())
            HealthBar(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update player with keys and platform group
            self.player.update([self.up, self.down, self.left, self.right], platforms)

            pygame.display.flip()
            self.clock.tick(90)

