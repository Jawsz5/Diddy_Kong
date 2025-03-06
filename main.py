import pygame
import sys
from Button import Button

class Main:
    def __init__(self):
        # initializing the constructor
        pygame.init()

        # screen resolution
        res = (720, 720)

        # opens up a window
        screen = pygame.display.set_mode(res)

        self.image = pygame.image.load("Backgrounds/Background_level1.png")
        self.image = pygame.transform.scale(self.image, res)


        screen.blit(self.image, (0, 0))

        b = Button(screen)


if __name__ == "__main__":
   pygame.init()
   playing = True
   while playing:
       Main()



