import pygame
import sys
from Button import Button



class Main:
    def __init__(self):
        pygame.init()
        self.res = (720, 720)
        self.SCREENW = self.res[0]
        self.SCREENH = self.res[1]  # Add the height of the screen
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

        self.screen_state = "home"  # Initially on the home screen

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Clear screen before drawing
            if self.screen_state == "home":
                self.screen.blit(self.image, (0, 0))  # Draw home screen background

                # Handle button clicks
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                for button in self.buttons:
                    button.draw()

                if pygame.mouse.get_pressed()[0] and self.buttons[0].rect.collidepoint(pygame.mouse.get_pos()):
                    pass  # Handle play button action here
                if pygame.mouse.get_pressed()[0] and self.buttons[1].rect.collidepoint(pygame.mouse.get_pos()):
                    self.screen_state = "rules"  # Switch to rules screen
                if pygame.mouse.get_pressed()[0] and self.buttons[2].rect.collidepoint(pygame.mouse.get_pos()):
                    self.screen_state = "settings"  # Switch to settings screen

            elif self.screen_state == "rules" or self.screen_state == "settings":
                # Move the back button to the bottom
                back = Button(self.screen, "Back", self.SCREENW // 2 - 100, self.SCREENH - 200, 200, 50)
                self.screen.blit(self.image, (0, 0))
                back.draw()

                # Handle back button click
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back.rect.collidepoint(pygame.mouse.get_pos()):
                            self.screen_state = "home"  # Go back to home screen


            pygame.display.update()

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Main().run()

