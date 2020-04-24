import logging
from pathlib import Path

import pygame as pg

import src.settings as s


logger = logging.getLogger(Path(__file__).stem)


class Game:
    def __init__(self):
        # después van a venir los ruiditos
        pg.mixer.init()
        self.screen = pg.display.set_mode((s.WIDTH, s.HEIGHT))
        self.clock = pg.time.Clock()

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

    def update(self):
        # para cuando metamos las sprites
        # self.all_sprites.update()
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        # self.all_sprites.draw(self.screen)
        pg.display.flip()
