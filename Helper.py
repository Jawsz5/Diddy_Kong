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

def move(sprite, velX, velY, path, rate=20):
    # jumping up
    if velY > 0:
        sprite.surf.fill("Red")
    # falling
    if velY < 0:
        sprite.surf.fill("Pink")
    # stationary
    if velY == 0 and velX == 0:
        sprite.surf.fill("Blue")
    # moving right
    p = True  # boolean that ensures only one animation is used per frame
    if velX > 0 and velY == 0:
        if not self.R and p:
            sprite.surf.fill("Green")
            self.R = True
            p = False
        if self.R and p:
            sprite.surf.fill("Yellow")
            self.R = False
            p = False
    # moving left - repeat of right, but with different animations
    p = True
    if velX < 0 and velY == 0:
        if not self.R and p:
            sprite.surf.fill("Purple")
            self.R = True
            p = False
        if self.R and p:
            sprite.surf.fill("Yellow")
            self.R = False
            p = False