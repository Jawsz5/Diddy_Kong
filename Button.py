import pygame

#https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
class Button(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        # Colors
        self.color_text = (0, 200, 0)  # Hover color
        self.color_back = (200, 200, 0)  # Default color

        # Font
        smallfont = pygame.font.SysFont('Corbel', 35)
        self.text = smallfont.render('Quit', True, (255, 255, 255))

        # Screen dimensions
        self.width = screen.get_width()
        self.height = screen.get_height()

        # Button dimensions
        self.button_width = 140
        self.button_height = 40

        # Button position (centered)
        self.x = (self.width - self.button_width) // 2
        self.y = (self.height - self.button_height) // 2

    def draw(self):
        mouse = pygame.mouse.get_pos()

        # Check if the mouse is hovering over the button
        if self.x <= mouse[0] <= self.x + self.button_width and self.y <= mouse[1] <= self.y + self.button_height:
            pygame.draw.rect(self.screen, self.color_text, [self.x, self.y, self.button_width, self.button_height])
        else:
            pygame.draw.rect(self.screen, self.color_back, [self.x, self.y, self.button_width, self.button_height])

        # Draw text onto the button
        text_x = self.x + (self.button_width - self.text.get_width()) // 2
        text_y = self.y + (self.button_height - self.text.get_height()) // 2
        self.screen.blit(self.text, (text_x, text_y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if self.x <= mouse[0] <= self.x + self.button_width and self.y <= mouse[1] <= self.y + self.button_height:
                pygame.quit()
                quit()
