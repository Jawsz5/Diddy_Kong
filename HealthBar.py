import pygame

class HealthBar:
    def __init__(self, screen):
        max_health = 100
        health = 100
        ratio = float(max_health/health)
        pygame.draw.rect(screen, "red", (50, 50, 300, 40))
        pygame.draw.rect(screen, "Green", (50, 50, 300*ratio, 40))


