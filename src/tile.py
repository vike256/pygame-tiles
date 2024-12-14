import pygame
import globals as g
from random import randint

COLUMN_KEYS = (pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k)

class Tile:
    def __init__(self):
        self.column = randint(0, 3)
        self.y = 0 - g.TILE_HEIGHT
        self.alive = True

    def update(self, dt, keys):        
        self.y += g.speed * dt
        if self.y > g.SCREEN_HEIGHT:
            g.reset = True
            self.alive = False
    
        if keys[COLUMN_KEYS[self.column]]:
            if abs(self.y - g.HIT_POS) <= g.TILE_HEIGHT:
                g.points += 1
                self.alive = False
            elif abs(self.y - g.HIT_POS) <= g.TILE_HEIGHT * 2:
                g.reset = True
                self.alive = False