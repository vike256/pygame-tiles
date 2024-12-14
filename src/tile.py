from random import randint

class Tile:
    def __init__(self):
        self.column = randint(0, 3)
        self.y = 0

    def update(self, dt, speed):
        self.y += speed * dt