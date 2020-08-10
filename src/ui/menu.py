import pygame as pg

import src.settings as s
from src.events.events import CustomEvents
from src.ui.button import Button


class Menu(pg.sprite.Sprite):
    size = pg.Vector2(
        x=9 * s.TILESIZE,
        y=7 * s.TILESIZE
    )
    pos = pg.Vector2(
        x=30 * s.TILESIZE,
        y=2 * s.TILESIZE
    )

    def __init__(self, sprite_group):
        self.sprite_group = sprite_group
        super().__init__(self.sprite_group)
        self.sprite_group.add(*self._create_buttons())
        self.image = pg.Surface(self.size)
        self.image.fill(s.DARKGREY)
        self.rect = self.image.get_rect(topleft=self.pos)

    def _create_buttons(self):
        size = pg.Vector2(
            x=7 * s.TILESIZE,
            y=2 * s.TILESIZE
        )
        return [
            Button(
                size=size,
                pos=self.pos + pg.Vector2(s.TILESIZE, s.TILESIZE),
                text='New',
                on_click=CustomEvents.START_GAME
            ),
            Button(
                size=size,
                pos=self.pos + pg.Vector2(s.TILESIZE, s.TILESIZE * 2 + size.y),
                text='Quit',
                on_click=pg.QUIT
            )
        ]
