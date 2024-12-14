import globals as g
from random import randint

class Tile:
    def __init__(self):
        self.column = randint(0, 3)
        self.y = 0 - g.TILE_HEIGHT
        self.alive = True

    def update(self, dt, speed):
        self.y += speed * dt
        if self.y > g.SCREEN_HEIGHT:
            self.alive = False