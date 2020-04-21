import pygame as pg


class Game:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        running = True
        while running:
            clock.tick(s.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            pg.display.flip()

