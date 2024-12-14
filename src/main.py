import pygame

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 960
TILE_WIDTH = SCREEN_WIDTH // 4
TILE_HEIGHT = TILE_WIDTH // 2
HIT_POS = SCREEN_HEIGHT - TILE_HEIGHT * 2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

hit_surface = pygame.Surface((SCREEN_WIDTH, TILE_HEIGHT))
hit_surface.set_alpha(128)
hit_surface.fill('white')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('#2B2B2B')

    pygame.draw.rect(screen, 'green', (0, 0, TILE_WIDTH, TILE_HEIGHT))
    #pygame.draw.rect(screen, pygame.Color(255, 255, 255, 0), (0, HIT_POS, SCREEN_WIDTH, TILE_HEIGHT))

    screen.blit(hit_surface, (0, HIT_POS))
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()