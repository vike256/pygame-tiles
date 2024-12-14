import pygame
from tile import Tile

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 960
TILE_WIDTH = SCREEN_WIDTH // 4
TILE_HEIGHT = TILE_WIDTH // 2
HIT_POS = SCREEN_HEIGHT - TILE_HEIGHT * 2
COLUMNS = (0, 0 + TILE_WIDTH, 0 + TILE_WIDTH * 2, 0 + TILE_WIDTH * 3)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

hit_surface = pygame.Surface((SCREEN_WIDTH, TILE_HEIGHT))
hit_surface.set_alpha(128)
hit_surface.fill('white')

tiles = []
tiles.append(Tile())

speed = 250

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('#2B2B2B')

    for tile in tiles:
        tile.update(dt, speed)
        pygame.draw.rect(screen, 'green', (COLUMNS[tile.column], tile.y, TILE_WIDTH, TILE_HEIGHT))
    #pygame.draw.rect(screen, pygame.Color(255, 255, 255, 0), (0, HIT_POS, SCREEN_WIDTH, TILE_HEIGHT))

    screen.blit(hit_surface, (0, HIT_POS))
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()