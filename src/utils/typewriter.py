import logging
from pathlib import Path
from dataclasses import dataclass
from typing import List, ClassVar

import pygame as pg

import src.settings as s
from src.utils.coords import Coords

logger = logging.getLogger(Path(__file__).stem)


@dataclass
class TypewriterConfig:
    size: int = 16
    color: tuple = s.GREEN
    surface_color: tuple = s.BLACK
    pos: str = 'topleft'
    padding: int = 10
    bold: int = 2
    positions: ClassVar[List[str]] = [
        'topleft', 'midtop', 'topright',
        'midleft', 'center', 'midright',
        'bottomleft', 'midbottom', 'bottomright'
    ]

    def __post_init__(self):
        if self.pos not in self.positions:
            raise ValueError(f'"{self.pos}" is not a valid pos value. '
                             f'Should be {self.positions!r}')


@dataclass
class Typewriter:
    surface: 'pg.Surface'
    config: TypewriterConfig = TypewriterConfig()

    def type(self, text: str, coords: Coords = None,
             config: TypewriterConfig = None
             ) -> None:
        # TODO: override method signature to make it static by
        # passing it a display surface.
        conf = config if config else self.config
        font = self.get_font(conf.size, conf.bold)

        text_surf = font.render(
            # this function takes no keyword args...
            text,  # text
            False,  # antialias
            conf.color  # color
        )
        text_rect = self.position(text_surf.get_rect(), conf.pos, coords)
        self.surface.blit(text_surf, text_rect)

    def position(self, text_rect, pos, coords):
        s_rect = self.surface.get_rect()
        if coords:
            text_rect.topleft = coords
        elif pos == 'center':
            text_rect.center = s_rect.center
        elif pos == 'topleft':
            padding = Coords(x=self.config.padding, y=self.config.padding)
            text_rect.topleft = s_rect.topleft + padding
        elif pos == 'midtop':
            padding = Coords(x=0, y=self.config.padding)
            text_rect.midtop = s_rect.midtop + padding
        elif pos == 'topright':
            padding = Coords(x=-self.config.padding, y=self.config.padding)
            text_rect.topright = s_rect.topright + padding
        elif pos == 'midleft':
            padding = Coords(x=self.config.padding, y=0)
            text_rect.midleft = s_rect.midleft + padding
        elif pos == 'midright':
            padding = Coords(x=-self.config.padding, y=0)
            text_rect.midright = s_rect.midright + padding
        elif pos == 'bottomleft':
            padding = Coords(x=self.config.padding, y=-self.config.padding)
            text_rect.bottomleft = s_rect.bottomleft + padding
        elif pos == 'midbottom':
            padding = Coords(x=0, y=-self.config.padding)
            text_rect.midbottom = s_rect.midbottom + padding
        elif pos == 'bottomright':
            padding = Coords(x=-self.config.padding, y=-self.config.padding)
            text_rect.bottomright = s_rect.bottomright + padding
        return text_rect

    @staticmethod
    def get_font(size, bold):
        font = pg.font.Font(s.FONT_PATH, size)
        font.set_bold(bold)
        return font
