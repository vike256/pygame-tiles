import pygame
import globals as g
from random import randint

COLUMN_KEYS = (pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k)

class Tile:
    def __init__(self):
        self.column = randint(0, 3)
        self.y = 0 - g.TILE_HEIGHT
        self.alive = True

    def update(self, dt, speed, keys):
        self.y += speed * dt
        if self.y > g.SCREEN_HEIGHT:
            self.alive = False
    
        if keys[COLUMN_KEYS[self.column]]:
            print('pressed')
            if abs(self.y - g.HIT_POS) <= 25:
                g.points += 1
                self.alive = False