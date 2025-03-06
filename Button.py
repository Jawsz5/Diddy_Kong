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
        self.hover_color = hover_color
        self.font = pygame.font.SysFont('Corbel', 35)
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))

    def draw(self):
        mouse = pygame.mouse.get_pos() # Gets mouse cursor position -> (x,y)
        if (self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height):
            rect_color = self.hover_color #If mouse is on the button, change the color
        else:
            rect_color = self.color


        pygame.draw.rect(self.screen, rect_color, [self.x, self.y, self.width, self.height])
        text_x = self.x + (self.width - self.rendered_text.get_width()) // 2
        text_y = self.y + (self.height - self.rendered_text.get_height()) // 2
        self.screen.blit(self.rendered_text, (text_x, text_y)) #Draws the text on the button


