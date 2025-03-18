import pygame
from Button import Button
from Platform import Platform
SCREENW = 800
SCREENH = 800

class Level1():
    def __init__(self, up, down, left, right):
        self.screen = pygame.display.set_mode((SCREENW, SCREENH))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Level 1")
        self.image = pygame.image.load("Backgrounds/Background_level1.png")
        self.image = pygame.transform.scale(self.image, (SCREENW, SCREENH))
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    @staticmethod
    def add_platform():
        all_sprites_list = pygame.sprite.Group()

        #1st platform
        plat_1 = Platform((255, 0, 0), 200, 200)
        plat_1.rect.x = 200
        plat_1.rect.y = 300
        all_sprites_list.add(plat_1)

        #2nd
        plat_2 = Platform((200, 255, 0), 200, 200)
        plat_2.rect.x = 400
        plat_2.rect.y = 300
        all_sprites_list.add(plat_2)


        all_sprites_list.update()
        return all_sprites_list

    def run(self):
        running = True
        while running:
            self.screen.blit(self.image, (0, 0))
            self.add_platform().draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            self.clock.tick(30)

