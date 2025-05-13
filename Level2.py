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
from Enemies import Enemy
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
        img_coords = [(100, 540, 150, 150), (400, 540, 150, 150), (300, 400, 150, 150), (50, 300, 150, 150),
                      (200, 100, 150, 150), (500, 300, 150, 150)]
        Hit_Box = [(120, 580, 100, 100), (420, 590, 100, 100), (320, 440, 100, 100), (70, 340, 100, 100),
                   (220, 140, 100, 100), (520, 340, 100, 100)]

        plat_1 = Platform(jungle_conversion(Hit_Box[0]), img_coords[0], jungle)  # originally (150, 200)
        all_sprites_list.add(plat_1)

        plat_2 = Platform(jungle_conversion(Hit_Box[1]), img_coords[1], jungle)  # originally (200, 200)
        all_sprites_list.add(plat_2)

        plat_3 = Platform(jungle_conversion(Hit_Box[2]), img_coords[2], jungle)
        all_sprites_list.add(plat_3)

        plat_4 = Platform(jungle_conversion(Hit_Box[3]), img_coords[3], jungle)
        all_sprites_list.add(plat_4)

        plat_5 = Platform(jungle_conversion(Hit_Box[4]), img_coords[4], jungle)
        all_sprites_list.add(plat_5)

        plat_6 = Platform(jungle_conversion(Hit_Box[5]), img_coords[5], jungle)
        all_sprites_list.add(plat_6)

        return all_sprites_list

    def Bananas(self):
        all_sprites_list = pygame.sprite.Group()

        Banana1 = Banana(520, 320, 50, 50)
        all_sprites_list.add(Banana1)

        Banana2 = Banana(220, 120, 50, 50)
        all_sprites_list.add(Banana2)

        Banana3 = Banana(120, 560, 50, 50)
        all_sprites_list.add(Banana3)

        Banana4 = Banana(320, 420, 50, 50)
        all_sprites_list.add(Banana4)

        return all_sprites_list

    def Enemy(self):
        animations = [
            pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy2/Enemy2_Stationary.png"), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/jump.png"), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/fall.png"), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy2/Enemy2_Moving_Right1.png"), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy2/Enemy2_Moving_Right2.png"), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy2/Enemy2_Moving_Left1.png"), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy2/Enemy2_Moving_Left2.png"), (100,100)),
        ]
        all_sprites_list = pygame.sprite.Group()

        Enemy1 = Enemy(320, 380, 100, 100, self.Platform(), animations)
        all_sprites_list.add(Enemy1)

        Enemy2 = Enemy(220, 80, 100, 100, self.Platform(), animations)
        all_sprites_list.add(Enemy2)

        Enemy3 = Enemy(520, 280, 100, 100, self.Platform(), animations)
        all_sprites_list.add(Enemy3)
        return all_sprites_list

