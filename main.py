import pygame
import sys
from Button import Button  # Import the Button class

class Main:
    def __init__(self):
        pygame.init()
        res = (720, 720)
        self.screen = pygame.display.set_mode(res)

        # Load and scale background image
        self.image = pygame.image.load("Backgrounds/Home_Screen_Background.webp")
        self.image = pygame.transform.scale(self.image, res)

        # Create button instance
        self.button = Button(self.screen)

    def run(self):
        running = True
        while running:
            self.screen.blit(self.image, (0, 0))  # Draw background

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self.button.handle_event(event)

            self.button.draw()  # Draw button
            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Main().run()



