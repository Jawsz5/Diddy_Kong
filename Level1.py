import pygame
import time

from Button import Button
from Platform import Platform
from Player import Player
from HealthBar import HealthBar
from Level import Level
from Treasure import Treasure
from Hitbox_Conversion import jungle_conversion
SCREENW = 800
SCREENH = 800

class Level1(Level):
    def __init__(self, up, down, left, right):
        super().__init__(up, down, left, right)
        pygame.display.set_caption("Level 1")
        self.image = pygame.image.load("Backgrounds/Background_level1.png")
        self.image = pygame.transform.scale(self.image, (SCREENW, SCREENH))
        self.image_end = pygame.image.load("End_Game_Screens/Game_Over1.png")
        self.image_end = pygame.transform.scale(self.image_end, (SCREENW, SCREENH))
        self.Game_Over_Buttons = Button(self.screen, "Play Again", SCREENW // 2 - 130, 475, 200, 50)
        self.Game_Over_Buttons1 = Button(self.screen, "Menu", SCREENW // 2 - 130, 550, 200, 50)
        self.image1 = pygame.image.load("Characters/treasure.png")
        self.image1 = pygame.transform.scale(self.image1, (200, 200))
        self.image2 = pygame.image.load("Characters/treasure_open.png")
        self.image2 = pygame.transform.scale(self.image2, (240, 200))
        self.screen.blit(self.image, (0, 0))
        self.screen.blit(self.image1, (0,0))
        self.screen_state = True #set to True if playing the game
        self.won = False


    def add_sprite(self):
        all_sprites_list = pygame.sprite.Group()
        jungle = pygame.image.load("Textures/jungle.png")

        # Horizontal Platforms (20% smaller than original)
        img_coords = [(100, 590, 80, 70), (400, 540, 80, 70), (300, 400, 80, 70), (50, 300, 80, 70), (200, 100, 80, 70), (500, 300, 80, 70)]

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



    def run(self):
        # Create the platforms group once outside the loop
        platforms = self.add_sprite()

        running = True
        while running:
            # Draw the background
            if self.screen_state:
                self.won = False
                self.screen.blit(self.image, (0, 0))
                # Draw platforms
                platforms.draw(self.screen)
                self.screen.blit(self.treasure.get_surface(), self.treasure.get_rect())
                self.screen.blit(self.image1, (620, -20))

                # Draw the player
                self.screen.blit(self.player.get_surface(), self.player.get_rect())

                HealthBar(self.screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                # Update player with keys and platform group
                self.player.update([self.up, self.down, self.left, self.right], platforms)
                if self.player.rect.colliderect(self.treasure.rect):
                    self.screen.blit(self.image2, (600, -20))
                    self.won = True
                    self.screen_state = False

            else:
                if self.won:
                    time.sleep(1)
                    self.won = False
                self.screen.blit(self.image_end, (0, 0))
                self.Game_Over_Buttons.draw()
                self.Game_Over_Buttons1.draw()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0] and self.Game_Over_Buttons.rect.collidepoint(pygame.mouse.get_pos()):
                            self.screen_state = True
                        if pygame.mouse.get_pressed()[0] and self.Game_Over_Buttons1.rect.collidepoint(pygame.mouse.get_pos()):
                            running = False
                    if self.screen_state:
                        self.player = Player(SCREENW, SCREENH, 150, 700)
                        break



            pygame.display.flip()
            self.clock.tick(90)

