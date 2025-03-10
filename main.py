import pygame
import sys
from Rules import Rules
from Button import Button


class Main:
    def __init__(self):
        pygame.init()
        self.res = (720, 720)
        self.SCREENW = self.res[0]
        self.screen = pygame.display.set_mode(self.res)
        pygame.display.set_caption("Game Menu")

        # Load and scale background image
        self.image = pygame.image.load("Backgrounds/Home_Screen_Background.webp")
        self.image = pygame.transform.scale(self.image, self.res)

        # Initialize buttons here
        self.buttons = [
            Button(self.screen, "Play", self.SCREENW // 2 - 100, 200, 200, 50),
            Button(self.screen, "Rules", self.SCREENW // 2 - 100, 300, 200, 50),
            Button(self.screen, "Settings", self.SCREENW // 2 - 100, 400, 200, 50)
        ]

    def run(self):
        running = True
        while running:

            self.screen.blit(self.image, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw buttons
            for button in self.buttons:
                button.draw()

            if pygame.mouse.get_pressed()[0] and self.buttons[0].rect.collidepoint(pygame.mouse.get_pos()):
                pass
            if pygame.mouse.get_pressed()[0] and self.buttons[1].rect.collidepoint(pygame.mouse.get_pos()):
                back = Button(self.screen, "Back", self.SCREENW // 2 - 300, 100, 200, 50)
                self.screen.fill("White")
                back.draw()
                pygame.display.update()
                while not (pygame.mouse.get_pressed()[0] and back.rect.collidepoint(pygame.mouse.get_pos())):
                    back.draw()
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0] and self.buttons[2].rect.collidepoint(pygame.mouse.get_pos()):
                self.screen.fill("White")

            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Main().run()

