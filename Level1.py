import pygame
from Button import Button
from Platform import Platform
from Player import Player
from HealthBar import HealthBar
from Level import Level
SCREENW = 800
SCREENH = 800

class Level1(Level):
    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        pygame.display.set_caption("Level 1")
        self.image = pygame.image.load("Backgrounds/Background_level1.png")
        self.image = pygame.transform.scale(self.image, (SCREENW, SCREENH))
        self.screen.blit(self.image, (0, 0))



    def add_sprite(self):
        all_sprites_list = pygame.sprite.Group()

        # Horizontal Platforms
        plat_1 = Platform((255, 0, 0), 150, 200)
        plat_1.rect.x = 100
        plat_1.rect.y = 600
        all_sprites_list.add(plat_1)


        plat_2 = Platform((0, 255, 0), 200, 200)
        plat_2.rect.x = 400
        plat_2.rect.y = 550
        all_sprites_list.add(plat_2)


        plat_3 = Platform((0, 0, 255), 120, 200)
        plat_3.rect.x = 300
        plat_3.rect.y = 400
        all_sprites_list.add(plat_3)

        plat_4 = Platform((255, 255, 0), 180, 200)
        plat_4.rect.x = 50
        plat_4.rect.y = 300
        all_sprites_list.add(plat_4)


        # Vertical Platforms
        plat_5 = Platform((255, 0, 255), 200, 100)
        plat_5.rect.x = 650
        plat_5.rect.y = 200
        all_sprites_list.add(plat_5)


        plat_6 = Platform((0, 255, 255), 200, 150)
        plat_6.rect.x = 200
        plat_6.rect.y = 100
        all_sprites_list.add(plat_6)


        plat_7 = Platform((100, 100, 100), 200, 200)
        plat_7.rect.x = 500
        plat_7.rect.y = 300
        all_sprites_list.add(plat_7)
        return all_sprites_list


    def run(self):
        running = True
        while running:
            self.add_sprite().draw(self.screen)
            self.screen.blit(self.player.get_surface(), self.player.get_rect())
            HealthBar(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.player.update([self.up, self.down, self.left, self.right])

            pygame.display.flip()
            self.clock.tick(90)

            self.screen.blit(self.image, (0, 0))



