import pygame

class HealthBar:
    def __init__(self, screen, max, current):
        self.max = max
        self.current = current
        ratio = float(current/max)
        pygame.draw.rect(screen, "red", (10, 70, 200, 20), 0, 10)
        pygame.draw.rect(screen, "Green", (10, 70, 200*ratio, 20), 0 ,10)

