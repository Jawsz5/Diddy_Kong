# platform hit-box conversions
def jungle_conversion(coords):
    # X coordinates stay the same
    return coords[0], coords[1] + 35, coords[2], coords[3] - 55


#Movement animation

"""
pass in a folder that contains a sprite sheet for animations
Order should be:

1. jump
2. fall
3. stationary
4. right 1
5. right 2
6. left 1
7. left 2
8. shoot
"""
switch = True
rate = 15
r_final = 15
def move(sprite, vel_x, vel_y, path):
    #the rate of the animation should be handled outside of this function. Set a rate and subtract an integer, Once r < i, call this function. Reset r
    global switch, rate
    # jumping up
    if vel_y > 0:
        sprite.surf.fill("Red")
    # falling
    if vel_y < 0:
        sprite.surf.fill("Pink")
    # stationary
    if vel_y == 0 and vel_x == 0:
        sprite.surf.fill("Blue")
    # moving right
    rate -= 1
    if rate <= 1:
        p = True  # boolean that ensures only one animation is used per frame
        if vel_x > 0 and vel_y == 0:
            if not switch and p:
                sprite.surf.fill("Green")
                switch = True
                p = False
            if switch and p:
                sprite.surf.fill("Yellow")
                switch = False
                p = False
        # moving left - repeat of right, but with different animations
        p = True
        if vel_x < 0 and vel_y == 0:
            if not switch and p:
                sprite.surf.fill("Purple")
                switch = True
                p = False
            if switch and p:
                sprite.surf.fill("Yellow")
                switch = False
                p = False
        rate = r_final