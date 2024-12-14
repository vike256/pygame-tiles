import pygame
import globals as g
from tile import Tile

def main():
    # initialize pygame and related variables
    pygame.init()
    screen = pygame.display.set_mode((g.SCREEN_WIDTH, g.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    hit_surface = pygame.Surface((g.SCREEN_WIDTH, g.TILE_HEIGHT))
    hit_surface.set_alpha(128)
    hit_surface.fill('white')

    tiles = []
    tiles.append(Tile())

    speed = 250
    tiles_on_screen = 1
    points = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('#2B2B2B')

        if len(tiles) < tiles_on_screen:
            tiles.append(Tile())

        for tile in tiles:
            tile.update(dt, speed)
            if not tile.alive:
                tiles.remove(tile)
            pygame.draw.rect(screen, 'green', (g.COLUMNS[tile.column], tile.y, g.TILE_WIDTH, g.TILE_HEIGHT))
        print(tiles)

        screen.blit(hit_surface, (0, g.HIT_POS))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == '__main__':
    main()