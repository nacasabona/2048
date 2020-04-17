import pygame

HT = 480
WT = 600
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WT, HT))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()

# main loop
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()

