import pygame
import sys
from Home import Home  # Import Home class from Home.py

class Main:
    def __init__(self):
        pygame.init()
        res = (720, 720)
        self.screen = pygame.display.set_mode(res)
        pygame.display.set_caption("Game Menu")

        # Load and scale background image
        self.image = pygame.image.load("Backgrounds/Home_Screen_Background.webp")
        self.image = pygame.transform.scale(self.image, res)

    def run(self):
        running = True
        while running:

            self.screen.blit(self.image, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            home = Home(self.screen)
            home.run()

            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Main().run()

