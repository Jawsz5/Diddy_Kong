import pygame

SCREENW, SCREENH = 800, 600

#https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
class Button:
    def __init__(self, screen, text, x, y, width=200, height=50, color=(200, 200, 0), hover_color=(0, 200, 0)):
        self.screen = screen
        self.text = text
        self.x = x #Top left corner of the button
        self.y = y #Top left corner of the button
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color#

        self.font = pygame.font.Font("Fonts/PixelifySans-VariableFont_wght.ttf", 35) #font for the buttons
        self.rendered_text = self.font.render(self.text, True, (255, 255, 20))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(pygame.image.load('Backgrounds/Button_Background.png'), (200, 50))
        self.image2 = pygame.transform.scale(pygame.image.load('Backgrounds/Button_Hover.png'), (200, 50))

    def draw(self):
        mouse = pygame.mouse.get_pos() # Gets mouse cursor position -> (x,y)
        t = True
        if (self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height):
            t = False #If mouse is on the button, change the color
        else:
            t = True

        rect = (self.x, self.y)

        pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.width, self.height])
        if t:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.image2, rect)
        text_x = self.x + (self.width - self.rendered_text.get_width()) // 2
        text_y = self.y + (self.height - self.rendered_text.get_height()) // 2
        self.screen.blit(self.rendered_text, (text_x, text_y)) #Draws the text on the button


