import pygame as pg

import src.settings as s
from src.utils.typewriter import TypewriterConfig, write


class Tile(pg.sprite.Sprite):
    def __init__(self, size: pg.Vector2, pos: pg.Vector2, value: int):
        super().__init__()
        self.size = size
        self.pos = pos
        self.value = value
        self._draw_backdrop()
        self._draw_value()

    def _draw_backdrop(self):
        self.image = pg.Surface(self.size)
        self.image.fill(s.BLACK)
        self.rect = self.image.get_rect(topleft=self.pos)

    def _draw_value(self):
        cfg = TypewriterConfig(
            color=s.GREEN,
            pos='center',
            size=24
        )
        write(self.image, str(self.value), config=cfg)
