import pygame
import time
from Button import Button
from Platform import Platform
from Player import Player
from HealthBar import HealthBar
from Level1 import Level1
from Level import Level
from Helper import jungle_conversion
from Banana import Banana
SCREENW = 800
SCREENH = 800

class Level2(Level1):
    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        pygame.display.set_caption("Level 2")
        self.image = pygame.image.load("Backgrounds/Background_level2.png")
        self.image = pygame.transform.scale(self.image, (SCREENW, SCREENH))
        self.image_end = pygame.image.load("End_Game_Screens/Game_Over2.png")
        self.image_end = pygame.transform.scale(self.image_end, (SCREENW, SCREENH))



    def Platform(self):
        all_sprites_list = pygame.sprite.Group()
        jungle = pygame.image.load("Textures/jungle.png")

        # Horizontal Platforms (20% smaller than original)
        img_coords = [(100, 590, 80, 70), (400, 540, 80, 70), (300, 400, 80, 70), (50, 300, 80, 70), (200, 100, 80, 70),
                      (500, 300, 80, 70)]

        plat_1 = Platform(jungle_conversion(img_coords[0]), img_coords[0], jungle)  # originally (150, 200)
        all_sprites_list.add(plat_1)

        plat_2 = Platform(jungle_conversion(img_coords[1]), img_coords[1], jungle)  # originally (200, 200)
        all_sprites_list.add(plat_2)

        plat_3 = Platform(jungle_conversion(img_coords[2]), img_coords[2], jungle)
        all_sprites_list.add(plat_3)

        plat_4 = Platform(jungle_conversion(img_coords[3]), img_coords[3], jungle)
        all_sprites_list.add(plat_4)

        plat_5 = Platform(jungle_conversion(img_coords[4]), img_coords[4], jungle)
        all_sprites_list.add(plat_5)

        plat_6 = Platform(jungle_conversion(img_coords[5]), img_coords[5], jungle)
        all_sprites_list.add(plat_6)

        return all_sprites_list

    def Bananas(self):
        all_sprites_list = pygame.sprite.Group()

        Banana1 = Banana(520, 280, 50, 50)
        all_sprites_list.add(Banana1)

        Banana2 = Banana(220, 80, 50, 50)
        all_sprites_list.add(Banana2)

        Banana3 = Banana(120, 570, 50, 50)
        all_sprites_list.add(Banana3)

        Banana4 = Banana(320, 380, 50, 50)
        all_sprites_list.add(Banana4)

        return all_sprites_list

