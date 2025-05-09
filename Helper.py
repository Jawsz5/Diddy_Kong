# platform hit-box conversions
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
