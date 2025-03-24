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

        #1st platform
        plat_1 = Platform((255, 0, 0), 150, 200)
        plat_1.rect.x = 200
        plat_1.rect.y = 300
        all_sprites_list.add(plat_1)

        #2nd
        plat_2 = Platform((200, 255, 0), 150, 200)
        plat_2.rect.x = 400
        plat_2.rect.y = 300
        all_sprites_list.add(plat_2)



        all_sprites_list.update()
        return all_sprites_list

    def run(self):
        running = True
        while running:
            if pygame.key.get_pressed()[self.up]:
                print([self.up, self.down, self.left, self.right])
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