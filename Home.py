import pygame
from Button import Button
import Rules

SCREENW = 800
SCREENH = 600

class Home:
    def __init__(self, screen):
        self.screen = screen  # Pass the screen from main.py
        self.clock = pygame.time.Clock()

        # Initialize buttons here
        self.buttons = [
            Button(self.screen, "Play", SCREENW // 2 - 100, 200, 200, 50),
            Button(self.screen, "Rules", SCREENW // 2 - 100, 300, 200, 50),
            Button(self.screen, "Settings", SCREENW // 2 - 100, 400, 200, 50)
        ]

    def show_rules(self, screen):
        #rules = Rules.Rules(screen)
        #rules.run()
        pass

    def show_settings(self):
        pass

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw buttons
            for button in self.buttons:
                button.draw()

            # https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
            if pygame.mouse.get_pressed()[0] and self.buttons[1].rect.collidepoint(pygame.mouse.get_pos()):
                self.show_rules(self.screen)

            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()


