import logging
from pathlib import Path

import pygame as pg

import src.settings as s
from src.utils.coords import Coords
from src.utils.typewriter import Typewriter, TypewriterConfig


logger = logging.getLogger(Path(__file__).stem)


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((s.WIDTH, s.HEIGHT))
        self.clock = pg.time.Clock()
        self.running = False
        self.debug = False

    def new(self):
        # esto estaba en el modelo. después veo cómo meterlo cuando funcione el resto bien
        # self.all_sprites = pg.sprite.Group()
        pass

    def run(self):
        logger.info('Starting main loop')
        self.running = True
        while self.running:
            self.clock.tick(s.FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_v:
                    self.debug = not self.debug
                    logger.info('Debug mode enabled: %s', self.debug)

    def update(self):
        self.screen.fill((0, 0, 0))
        if self.debug:
            self.draw_grid(self.screen)
            self.draw_mouse_pos(self.screen)

    def draw(self):
        # self.all_sprites.draw(self.screen)
        pg.display.flip()

    def draw_mouse_pos(self, screen):
        mx, my = pg.mouse.get_pos()
        tp = Typewriter(
            screen,
            TypewriterConfig(size=12, pos='bottomright', padding=0)
        )
        tp.type(str(Coords(x=mx, y=my)))

    def draw_grid(self, screen):
        for x in range(0, s.WIDTH, s.TILESIZE):
            pg.draw.line(screen, s.LIGHTGREY, (x, 0), (x, s.HEIGHT))
        for y in range(0, s.HEIGHT, s.TILESIZE):
            pg.draw.line(screen, s.LIGHTGREY, (0, y), (s.WIDTH, y))
