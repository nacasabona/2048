import logging
from pathlib import Path

import pygame as pg

import src.settings as s


logger = logging.getLogger(Path(__file__).stem)


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((s.WIDTH, s.HEIGHT))
        self.clock = pg.time.Clock()

    def run(self):
        logger.info('Starting main loop')
        running = True
        while running:
            self.clock.tick(s.FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            self.screen.fill((0, 0, 0))
            pg.display.flip()
