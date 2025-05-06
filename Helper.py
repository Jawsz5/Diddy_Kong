# platform hit-box conversions
def jungle_conversion(coords):
    # X coordinates stay the same
    return coords[0] + 20 , coords[1] + 35, coords[2] - 20, coords[3] - 55


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
    #the rate of the animation should be handled outside of this function. Set a rate and subtract an integer, Once r < i, call this function. Reset r
    global switch, rate
    # stationary
    if vel_y == 0 and vel_x == 0:
        sprite.image = path[0]
    # jumping up
    if vel_y > 0:
        sprite.image = path[1]
    # falling
    if vel_y < 0:
        sprite.image = path[2]
    rate -= 1
    if rate <= 1:
        p = True  # boolean that ensures only one animation is used per frame
        # moving right
        if vel_x > 0 and vel_y == 0:
            if not switch and p:
                sprite.image = path[3]
                switch = True
                p = False
            if switch and p:
                sprite.image = path[4]
                switch = False
                p = False
        # moving left - repeat of right, but with different animations
        p = True
        if vel_x < 0 and vel_y == 0:
            if not switch and p:
                sprite.image = path[5]
                switch = True
                p = False
            if switch and p:
                sprite.image = path[6]
                switch = False
                p = False
        rate = r_final