import pygame
import sys
from Button import Button
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_w,
    K_a,
    K_s,
    K_d,
    K_i,
    K_j,
    K_k,
    K_l
)

UP = K_w
DOWN = K_s
LEFT = K_a
RIGHT = K_d

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
            Button(self.screen, "Play", self.SCREENW // 2 - 100, 250, 200, 50),
            Button(self.screen, "Rules", self.SCREENW // 2 - 100, 350, 200, 50),
            Button(self.screen, "Settings", self.SCREENW // 2 - 100, 450, 200, 50)
        ]
        self.settings_buttons = [
            Button(self.screen, "Default (WASD)", self.SCREENW // 2 - 100, 250, 200, 50),
            Button(self.screen, "IJKL", self.SCREENW // 2 - 100, 300, 200, 50),
            Button(self.screen, "Arrows", self.SCREENW // 2 - 100, 350, 200, 50)

        ]



        self.screen_state = "home"  # Initially on the home screen

        # Title Font (Bubble-style)
        self.title_font = pygame.font.Font("Fonts/Bubblegum.ttf", 45)  # Ensure you have a bubble-style font
        self.title_text = self.title_font.render("Welcome to Diddy Kong Island!", True, (255, 69, 0))  # Bold bubble font
        self.title_rect = self.title_text.get_rect(center=(self.SCREENW // 2, 150))

        # Rules Font
        self.rules_font = pygame.font.Font("Fonts/Bubblegum.ttf", 30)
        self.rules_text = [
            "Guide Diddy Kong to the treasure while",
            " avoiding danger! Keep an eye on his health bar.",
            "If it hits zero, the game is over.",
            "Beat the clock and choose from three",
            "difficulty levels: Easy, Medium, or Hard."
        ]
        self.settings_text = [
            "Choose between the three presets below: "
        ]



    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Clear screen before drawing
            if self.screen_state == "home":
                self.screen.blit(self.image, (0, 0))  # Draw home screen background

                # Draw title
                self.screen.blit(self.title_text, self.title_rect)

                # Handle button clicks
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                for button in self.buttons:
                    button.draw() #Draws the buttons

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

                if self.screen_state == "rules":
                    y_offset = 150
                    for line in self.rules_text:
                        text_surface = self.rules_font.render(line, True, (255, 69, 0))
                        text_rect = text_surface.get_rect(center=(self.SCREENW // 2, y_offset))
                        self.screen.blit(text_surface, text_rect)
                        y_offset += 40

                # Handle back button click
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back.rect.collidepoint(pygame.mouse.get_pos()):
                            self.screen_state = "home"  # Go back to home screen

            pygame.display.update()

        pygame.quit()
        sys.exit() #

if __name__ == "__main__":
    Main().run()