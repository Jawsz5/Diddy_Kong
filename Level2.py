import pygame
from Button import Button
from Platform import Platform
from Player import Player
SCREENW = 800
SCREENH = 800

class Level2():
    def __init__(self, up, down, left, right):
        self.screen = pygame.display.set_mode((SCREENW, SCREENH))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Level 2")
        self.image = pygame.image.load("Backgrounds/Background_level2.png")
        self.image = pygame.transform.scale(self.image, (SCREENW, SCREENH))
        self.screen.blit(self.image, (0, 0))
        self.up = up
        self.down = down
        self.left = left
        self.right = right

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
            self.add_sprite().draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            self.clock.tick(30)


