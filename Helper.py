# platform hit-box conversions
import pygame


def jungle_conversion(coords):
    # X coordinates stay the same
    return coords[0] + 20 , coords[1] + 35, coords[2] - 20, coords[3] - 90


#Movement animation

"""
pass in a folder that contains a sprite sheet for animations
Order should be:

1. stationary
2. jump
3. fall
4. right 1
5. right 2
6. left 1
7. left 2
8. shoot
"""
switch = True
rate = 15
r_final = 10
def animate(sprite, vel_x, vel_y, path):
    # stationary
    if vel_y == 0 and vel_x == 0:
        sprite.image = path[0]
    # jumping up
    elif vel_y > 0:
        sprite.image = path[1]
    # falling
    elif vel_y < 0:
        sprite.image = path[2]

    sprite.rate -= 1
    if sprite.rate <= 1:
        # moving right
        if vel_x > 0 and vel_y == 0:
            sprite.image = path[3] if not sprite.switch else path[4]
            sprite.switch = not sprite.switch
        # moving left
        elif vel_x < 0 and vel_y == 0:
            sprite.image = path[5] if not sprite.switch else path[6]
            sprite.switch = not sprite.switch

        sprite.rate = sprite.r_final


#pass in 2 sprite groups, first group is the one that "hits" the other. add a value for damage done. Select a value for type of aftermath (bounce, stationary, travel through), pass in health too. Death animation
def shot(bullet_group, sprite_group):
    for bullet in bullet_group:
        for sprite in sprite_group:
            if bullet.rect.colliderect(sprite.rect):
                sprite.hp -= 30
                bullet_group.remove(bullet)
            if sprite.hp <= 0:
                sprite_group.remove(sprite)

def player_hit(player, object, v):
    if player.rect.colliderect(object.rect):
        player.hp -= v
