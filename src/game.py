import logging
from pathlib import Path

import pygame as pg

import src.settings as s
from src.events.overseer import Overseer
from src.events.events import CustomEvents
from src.utils.coords import Coords
from src.utils.typewriter import TypewriterConfig, write


logger = logging.getLogger(Path(__file__).stem)


class Game:
    def __init__(self):
        self._register_listeners()
        self.screen = pg.display.set_mode((s.WIDTH, s.HEIGHT))
        self.clock = pg.time.Clock()
        self.running = False
        self.debug = False

    def _register_listeners(self):
        Overseer.add_listener(pg.QUIT, self)
        Overseer.add_listener(pg.KEYDOWN, self)

    def new(self):
        # esto estaba en el modelo. después veo cómo meterlo cuando funcione el resto bien
        # self.all_sprites = pg.sprite.Group()
        pass

    def run(self):
        logger.info('Starting main loop')
        self.running = True
        while self.running:
            self.clock.tick(s.FPS)
            self.update()
            self.draw()

    def update(self):
        for event in pg.event.get():
            Overseer.broadcast(event)
        self.screen.fill((0, 0, 0))
        if self.debug:
            self.draw_grid(self.screen)
            self.draw_mouse_pos(self.screen)

    def draw(self):
        # self.all_sprites.draw(self.screen)
        pg.display.flip()

    def on_notify(self, event):
        if event.type == pg.QUIT:
            self.running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_v:
                self.debug = not self.debug
                logger.info('Debug mode enabled: %s', self.debug)

    def draw_mouse_pos(self, screen):
        mx, my = pg.mouse.get_pos()
        write(
            surface=screen,
            text=str(Coords(x=mx, y=my)),
            config=TypewriterConfig(size=12, pos='bottomright', padding=0)
        )

    def draw_grid(self, screen):
        for x in range(0, s.WIDTH, s.TILESIZE):
            pg.draw.line(screen, s.LIGHTGREY, (x, 0), (x, s.HEIGHT))
        for y in range(0, s.HEIGHT, s.TILESIZE):
            pg.draw.line(screen, s.LIGHTGREY, (0, y), (s.WIDTH, y))
