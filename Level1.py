import pygame
from Button import Button
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

    def run(self):
        running = True
        while running:
            self.screen.blit(self.image, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
            self.clock.tick(30)

