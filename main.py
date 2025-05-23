import pygame
import sys
from Button import Button
from Level1 import Level1
from Level2 import Level2
from Level3 import Level3
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

class Main:
    def __init__(self):
        pygame.init()
        self.res = (800, 800)
        self.SCREENW = self.res[0]
        self.SCREENH = self.res[1]  # Add the height of the screen
        self.screen = pygame.display.set_mode(self.res)
        pygame.display.set_caption("Game Menu")

        # Load and scale background image
        self.image = pygame.image.load("Backgrounds/Home_Screen_Background.webp")
        self.image = pygame.transform.scale(self.image, self.res)

        scale_rules = (600,700)
        self.image1 = pygame.image.load("Backgrounds/rules.png")
        self.image1 = pygame.transform.scale(self.image1, scale_rules)

        self.image2 = pygame.image.load("Backgrounds/Title_Text_Background.png")
        self.image2 = pygame.transform.scale(self.image2, (720, 75))

        self.UP = K_w
        self.DOWN = K_s
        self.LEFT = K_a
        self.RIGHT = K_d
        self.SHOOT = K_SPACE
        # Initialize buttons here
        self.buttons = [
            Button(self.screen, "Play", self.SCREENW // 2 - 100, 250, 200, 50),
            Button(self.screen, "Rules", self.SCREENW // 2 - 100, 350, 200, 50),
            Button(self.screen, "Settings", self.SCREENW // 2 - 100, 450, 200, 50),
            Button(self.screen, "Quit", self.SCREENW // 2 - 100, 650, 200, 50)
        ]
        self.settings_buttons = [
            Button(self.screen, "WASD", self.SCREENW // 2 - 100, 250, 200, 50),
            Button(self.screen, "IJKL", self.SCREENW // 2 - 100, 325, 200, 50),
            Button(self.screen, "Arrows", self.SCREENW // 2 - 100, 400, 200, 50)

        ]
        self.levels = [
            Button(self.screen, "Easy", self.SCREENW // 2 - 100, 325, 200, 50),
            Button(self.screen, "Medium", self.SCREENW // 2 - 100, 410, 200, 50),
            Button(self.screen, "Hard", self.SCREENW // 2 - 100, 495, 200, 50)
        ]

        self.screen_state = "home"
        self.player1 = None# Initially on the home screen

        # Title Font (Bubble-style)
        self.title_font = pygame.font.Font("Fonts/Bubblegum.ttf", 45)  # Ensure you have a bubble-style font
        self.title_text = self.title_font.render("Welcome to Diddy Kong Island!", True, (255, 230, 60))  # Bold bubble font
        self.title_rect = self.title_text.get_rect(center=(self.SCREENW // 2, 150))
        self.title_rect_back = self.title_text.get_rect(center=(self.SCREENW // 2 - 15, 130))

        # Rules Font
        self.rules_font = pygame.font.Font("Fonts/Bubblegum.ttf", 15)
        self.rules_text = [
            "Guide Diddy Kong to the treasure",
            "while avoiding danger! ",
            "Keep an eye on his health bar.",
            "If it hits zero, "
            "the game is over.",
            "Beat the clock, choose from three",
            "difficulty levels: ",
            "Easy, Medium, Hard."
        ]
        self.settings_font = pygame.font.Font("Fonts/Bubblegum.ttf", 30)
        self.settings_text = [
            "Choose between the three presets below: "
        ]
        self.settings_text_2 = ["You are using the WASD preset"]


    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Clear screen before drawing
            if self.screen_state == "home":
                self.image2 = pygame.transform.scale(self.image2, (720, 75))
                self.screen.blit(self.image, (0, 0))  # Draw home screen background

                # Draw title
                self.screen.blit(self.image2, self.title_rect_back)
                self.screen.blit(self.title_text, self.title_rect)

                # Handle button clicks
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                for button in self.buttons:
                    button.draw() #Draws the buttons

                if pygame.mouse.get_pressed()[0] and self.buttons[0].rect.collidepoint(pygame.mouse.get_pos()):
                    self.screen_state = "play" # Switch to play screen
                if pygame.mouse.get_pressed()[0] and self.buttons[1].rect.collidepoint(pygame.mouse.get_pos()):
                    self.screen_state = "rules"  # Switch to rules screen
                if pygame.mouse.get_pressed()[0] and self.buttons[2].rect.collidepoint(pygame.mouse.get_pos()):
                    self.screen_state = "settings"  # Switch to settings screen
                if pygame.mouse.get_pressed()[0] and self.buttons[3].rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()


            elif self.screen_state == "rules" or self.screen_state == "play" or self.screen_state == "settings":
                # Move the back button to the bottom
                back = Button(self.screen, "Back", self.SCREENW // 2 - 100, self.SCREENH - 100, 200, 50)
                self.screen.blit(self.image, (0, 0))
                back.draw()

                if self.screen_state == "rules":
                    y_offset = 260
                    self.screen.blit(self.image1, (100, 0))
                    for line in self.rules_text:
                        text_surface = self.rules_font.render(line, True, (30, 0, 0))
                        text_rect = text_surface.get_rect(center=(self.SCREENW // 2, y_offset))
                        self.screen.blit(text_surface, text_rect)
                        y_offset += 40



                if self.screen_state == "settings":
                    y_offset = 150
                    self.image2 = pygame.transform.scale(self.image2, (700, 50))
                    for line in self.settings_text:
                        text_surface = self.settings_font.render(line, True, (255, 230, 60))
                        text_rect = text_surface.get_rect(center=(self.SCREENW // 2, y_offset))
                        text_rect_back1 = text_surface.get_rect(center=(self.SCREENW // 2 - 40, y_offset - 10))

                        self.screen.blit(self.image2, text_rect_back1)
                        self.screen.blit(text_surface, text_rect)
                        y_offset += 40
                    for button in self.settings_buttons:
                        button.draw()
                    for line in self.settings_text_2:
                        self.image2 = pygame.transform.scale(self.image2, (550, 50))
                        text_surface = self.settings_font.render(line, True, (255, 230, 60))
                        text_rect = text_surface.get_rect(center=(self.SCREENW // 2, y_offset + 350))
                        text_rect_back1 = text_surface.get_rect(center=(self.SCREENW // 2 - 45, y_offset + 340))

                        self.screen.blit(self.image2, (130, 515))
                        self.screen.blit(text_surface, text_rect)
                        y_offset += 40

                if self.screen_state == "play":
                    self.image2 = pygame.transform.scale(self.image2, (770, 50))
                    self.title_font = pygame.font.Font("Fonts/Bubblegum.ttf", 38)  # Ensure you have a bubble-style font
                    self.title_text = self.title_font.render("Choose between the three levels below:", True,
                                                             (255, 230, 60))  # Bold bubble font
                    self.title_rect = self.title_text.get_rect(center=(self.SCREENW // 2, 175))
                    self.title_rect_back1 = self.title_text.get_rect(center=(self.SCREENW // 2 - 5, 170))
                    self.screen.blit(self.image2, self.title_rect_back1)
                    self.screen.blit(self.title_text, self.title_rect)
                    for button in self.levels:
                        button.draw()
                    if pygame.mouse.get_pressed()[0] and self.levels[0].rect.collidepoint(pygame.mouse.get_pos()):
                        level1 = Level1(self.UP, self.DOWN, self.LEFT, self.RIGHT)
                        level1.run()
                    if pygame.mouse.get_pressed()[0] and self.levels[1].rect.collidepoint(pygame.mouse.get_pos()):
                        level2 = Level2(self.UP, self.DOWN, self.LEFT, self.RIGHT)
                        level2.run()
                    if pygame.mouse.get_pressed()[0] and self.levels[2].rect.collidepoint(pygame.mouse.get_pos()):
                        level3 = Level3(self.UP, self.DOWN, self.LEFT, self.RIGHT)
                        level3.run()
                #Sets title text when on home screen
                self.title_text = self.title_font.render("Welcome to Diddy Kong Island!", True, (255, 230, 60))
                self.title_rect = self.title_text.get_rect(center=(self.SCREENW // 2, 150))
                # Handle back button click
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if back.rect.collidepoint(pygame.mouse.get_pos()):
                            self.screen_state = "home"  # Go back to home screen
                        if self.settings_buttons[0].rect.collidepoint(pygame.mouse.get_pos()) and self.screen_state == "settings":
                            self.UP = K_w
                            self.DOWN = K_s
                            self.LEFT = K_a
                            self.RIGHT = K_d
                            self.settings_text_2 = ["You are using the WASD preset"]
                        elif self.settings_buttons[1].rect.collidepoint(pygame.mouse.get_pos()) and self.screen_state == "settings":
                            self.UP = K_i
                            self.DOWN = K_k
                            self.LEFT = K_j
                            self.RIGHT = K_l
                            self.settings_text_2 = ["You are using the IJKL preset"]
                        elif self.settings_buttons[2].rect.collidepoint(pygame.mouse.get_pos()) and self.screen_state == "settings":
                            self.UP = K_UP
                            self.DOWN = K_DOWN
                            self.LEFT = K_LEFT
                            self.RIGHT = K_RIGHT
                            self.settings_text_2 = ["You are using the ARROWS preset"]

            pygame.display.update()

        pygame.quit()
        sys.exit() #

if __name__ == "__main__":
    # print(pygame.font.get_fonts())
    Main().run()