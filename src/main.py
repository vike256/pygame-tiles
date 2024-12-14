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
    font = pygame.Font(None, 64)

    hit_surface = pygame.Surface((g.SCREEN_WIDTH, g.TILE_HEIGHT))
    hit_surface.set_alpha(128)
    hit_surface.fill('white')

    tiles = []
    tiles.append(Tile())

    tiles_on_screen = 1
    POINTS_POS = (16, 16)
    HIGHSCORE_POS = (320, 16)
    highscore = 0

    while running:
        keys = pygame.key.get_just_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill('#2B2B2B')

        if len(tiles) < tiles_on_screen:
            tiles.append(Tile())

        for tile in tiles:
            tile.update(dt, keys)
            if not tile.alive:
                tiles.remove(tile)
            pygame.draw.rect(screen, 'green', (g.COLUMNS[tile.column], tile.y, g.TILE_WIDTH, g.TILE_HEIGHT))

        g.speed += dt * 4
        print(g.speed)

        if g.points > highscore:
            highscore = g.points

        if g.reset:
            g.points = 0
            g.speed = g.START_SPEED
            g.reset = False

        # Render
        points_text = font.render(str(g.points), True, 'white')
        highscore_text = font.render(str(highscore), True, 'red')

        screen.blit(points_text, POINTS_POS)
        screen.blit(highscore_text, HIGHSCORE_POS)
        screen.blit(hit_surface, (0, g.HIT_POS))
        pygame.display.flip()
        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == '__main__':
    main()