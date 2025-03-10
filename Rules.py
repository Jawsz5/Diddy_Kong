import pygame
from Button import Button
SCREENW = 800
SCREENH = 600

class Rules:
    def __init__(self):
        res = (720, 720)
        self.screen = pygame.display.set_mode(res)
        pygame.display.set_caption("Game Menu")

        self.clock = pygame.time.Clock()

        self.button = Button(self.screen, "Back", SCREENW // 2 - 300, 100, 200, 50)

    def go_home(self):
        pass

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.button.draw()

            if pygame.mouse.get_pressed()[0] and self.button.rect.collidepoint(pygame.mouse.get_pos()):
                self.go_home()

            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()

