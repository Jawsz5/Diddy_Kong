import pygame
from Player import Player
from HealthBar import HealthBar
from Treasure import Treasure
SCREENW = 800
SCREENH = 800

class Level:
    def __init__(self, up, down, left, right):
        self.screen = pygame.display.set_mode((SCREENW, SCREENH))
        self.clock = pygame.time.Clock()
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.player = Player(SCREENW, SCREENH, 150, 700)
        self.treasure = Treasure(700,50)


    def add_sprite(self):
        all_sprites_list = pygame.sprite.Group()
        return all_sprites_list

    def run(self):
        running = True
        while running:
            self.add_sprite().draw(self.screen)
            self.screen.blit(self.player.get_surface(), self.player.get_rect())
            self.screen.blit(self.treasure.get_surface(),self.treasure.get_rect())
            HealthBar(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.player.update([self.up, self.down, self.left, self.right])

            pygame.display.flip()
            self.clock.tick(90)









