import pygame as pg
import src.settings as s

pg.init()
screen = pg.display.set_mode((s.WT, s.HT))
pg.display.set_caption("2048")
clock = pg.time.Clock()


# main loop
class Loop:
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
