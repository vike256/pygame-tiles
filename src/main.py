import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 960
TILE_WIDTH = SCREEN_WIDTH // 4
TILE_HEIGHT = TILE_WIDTH // 2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    pygame.draw.rect(screen, (0, 255, 0), (0, 0, TILE_WIDTH, TILE_HEIGHT))

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()