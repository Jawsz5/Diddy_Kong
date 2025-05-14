import pygame
import time

from Button import Button
from Platform import Platform
from Player import Player
from HealthBar import HealthBar
from Level import Level
from Treasure import Treasure
from Helper import jungle_conversion, shot, player_hit
from Banana import Banana
from Enemies import Enemy
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
        self.count = 1
        self.banana_count = 0
        self.banana_shot = False
        self.prev_velo = 0

    def Platform(self):
        all_sprites_list = pygame.sprite.Group()
        jungle = pygame.image.load("Textures/jungle.png")

        # Horizontal Platforms (20% smaller than original)
        img_coords = [(100, 540, 150, 150), (400, 540, 150, 150), (300, 400, 150, 150), (50, 300, 150, 150), (200, 100, 150, 150), (500, 300, 150, 150)]
        Hit_Box = [(120, 580, 100, 100), (420, 590, 100, 100), (320, 440, 100, 100), (70, 340, 100, 100), (220, 140, 100, 100), (520, 340, 100, 100)]

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
            pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy1/Enemy_Stationary.png").convert_alpha(), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/jump.png").convert_alpha(), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/DIDDY_KONG/fall.png").convert_alpha(), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy1/Enemy_Moving_Right1.png").convert_alpha(), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy1/Enemy_Moving_Right2.png").convert_alpha(), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy1/Enemy_Moving_Left1.png").convert_alpha(), (100,100)),
            pygame.transform.scale(pygame.image.load("Characters/Enemy/Enemy1/Enemy_Moving_Left2.png").convert_alpha(), (100,100)),
        ]
        all_sprites_list = pygame.sprite.Group()

        Enemy1 = Enemy(320, 380, 100, 100, self.Platform(), animations)
        all_sprites_list.add(Enemy1)

        Enemy2 = Enemy(220, 80, 100, 100, self.Platform(), animations)
        all_sprites_list.add(Enemy2)

        Enemy3 = Enemy(520, 280, 100, 100, self.Platform(), animations)
        all_sprites_list.add(Enemy3)
        return all_sprites_list




    def Bananas2(self):
        all_sprites_list = pygame.sprite.Group()
        return all_sprites_list


    def run(self):
        # Create the platforms group once outside the loop
        platforms = self.Platform()
        bananas = self.Bananas()
        bananas2 = self.Bananas2()
        Enemy = self.Enemy()
        start_time = time.time()

        running = True
        while running:
            # Draw the background
            if self.screen_state:
                self.won = False
                self.screen.blit(self.image, (0, 0))
                # Draw platforms
                platforms.draw(self.screen)
                bananas.draw(self.screen)
                bananas2.draw(self.screen)
                Enemy.draw(self.screen)
                self.screen.blit(self.treasure.get_surface(), self.treasure.get_rect())
                self.screen.blit(self.image1, (620, -20))

                # Draw the player
                self.screen.blit(self.player.get_surface(), self.player.get_rect())

                Health = HealthBar(self.screen, 100, 100*self.count)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                # shooting

                for i in Enemy:
                    i.update()
                self.player.update([self.up, self.down, self.left, self.right], platforms)
                for banana in bananas:
                    if self.player.rect.colliderect(banana.rect) and banana.rect.y != 10:
                            b = Banana(20 + self.banana_count, 10, 50, 50)
                            bananas2.add(b)
                            bananas.remove(banana)
                            self.banana_count += 25

                shoot = pygame.key.get_pressed()[pygame.K_SPACE]
                if shoot:
                    self.banana_shot = True
                for banana in bananas2:
                    banana.update()
                    if shoot and banana.rect.y == 10 and self.banana_shot:
                        banana.rect.y = self.player.rect.y
                        # right shot
                        if self.player.velX > 0:
                            banana.rect.x = self.player.rect.x + 15
                            banana.update_velX(5)
                        # left shot
                        elif self.player.velX < 0:
                                banana.rect.x = self.player.rect.x - 15
                                banana.update_velX(-5)
                        #stationary left
                        elif self.prev_velo > 0:
                            banana.rect.x = self.player.rect.x
                            banana.update_velX(5)
                        #stationary right
                        else:
                            banana.rect.x = self.player.rect.x
                            banana.update_velX(-5)

                    if banana.rect.right > SCREENW:
                        bananas2.remove(banana)
                        break
                    if banana.rect.left < 0:
                        bananas2.remove(banana)
                        break

                    self.banana_shot = False

                shot(bananas2, Enemy)
                for enemy in Enemy:
                    #player_hit(self.player, enemy, 5)
                    if self.player.rect.colliderect(enemy):
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        if elapsed_time > 2:
                            self.player.hp -= 10
                            start_time = time.time()
                Health = HealthBar(self.screen, 100, self.player.hp * self.count)

                if self.player.rect.colliderect(self.treasure.rect):
                    self.screen.blit(self.image2, (600, -20))
                    self.won = True
                    self.screen_state = False

                if self.player.velX != 0:
                    self.prev_velo = self.player.velX

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

