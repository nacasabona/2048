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


def write(
    surface: pg.Surface, text: str, pos: pg.Vector2 = None,
    config: TypewriterConfig = TypewriterConfig()
) -> pg.Rect:
    font = get_font(config.size, config.bold)

    text_surf = font.render(
        # this function takes no keyword args...
        text,  # text
        False,  # antialias
        config.color  # color
    )
    text_rect = position(surface, text_surf.get_rect(), config, pos)
    surface.blit(text_surf, text_rect)
    return text_rect


def position(surface, text_rect, config, pos=None):
    s_rect = surface.get_rect()
    if pos:
        text_rect.topleft = pos
    elif config.pos == 'center':
        text_rect.center = s_rect.center
    elif config.pos == 'topleft':
        padding = Coords(x=config.padding, y=config.padding)
        text_rect.topleft = s_rect.topleft + padding
    elif config.pos == 'midtop':
        padding = Coords(x=0, y=config.padding)
        text_rect.midtop = s_rect.midtop + padding
    elif config.pos == 'topright':
        padding = Coords(x=-config.padding, y=config.padding)
        text_rect.topright = s_rect.topright + padding
    elif config.pos == 'midleft':
        padding = Coords(x=config.padding, y=0)
        text_rect.midleft = s_rect.midleft + padding
    elif config.pos == 'midright':
        padding = Coords(x=-config.padding, y=0)
        text_rect.midright = s_rect.midright + padding
    elif config.pos == 'bottomleft':
        padding = Coords(x=config.padding, y=-config.padding)
        text_rect.bottomleft = s_rect.bottomleft + padding
    elif config.pos == 'midbottom':
        padding = Coords(x=0, y=-config.padding)
        text_rect.midbottom = s_rect.midbottom + padding
    elif config.pos == 'bottomright':
        padding = Coords(x=-config.padding, y=-config.padding)
        text_rect.bottomright = s_rect.bottomright + padding
    return text_rect


def get_font(size, bold):
    font = pg.font.Font(s.FONT_PATH, size)
    font.set_bold(bold)
    return font
