import pygame
# Citation: https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/

class Button(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        # white color
        self.color = (255, 0, 255)

        # shade of the button when hovering over
        self.color_text = (0, 200, 0)

        # shade of the button background
        self.color_back = (200, 200, 0)

        # defining a font
        smallfont = pygame.font.SysFont('Corbel', 35)

        # rendering a text written in
        # this font
        text = smallfont.render('quit', True, self.color)

        # stores the width of the
        # screen into a variable
        width = screen.get_width()

        # stores the height of the
        # screen into a variable
        height = screen.get_height()

        while True:

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()

                    # checks if a mouse is clicked
                if ev.type == pygame.MOUSEBUTTONDOWN:

                    # if the mouse is clicked on the
                    # button the game is terminated
                    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                        pygame.quit()

            # stores the (x,y) coordinates into
            # the variable as a tuple
            mouse = pygame.mouse.get_pos()

            # if mouse is hovered on a button it
            # changes to lighter shade
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.draw.rect(screen, self.color_text, [width / 2, height / 2, 140, 40])

            else:
                pygame.draw.rect(screen, self.color_back, [width / 2, height / 2, 140, 40])

                # superimposing the text onto our button
            screen.blit(text, (width / 2 + 50, height / 2))

            # updates the frames of the game
            pygame.display.update()