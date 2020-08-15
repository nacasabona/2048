import pygame as pg

import src.settings as s
from src.ui.button import Button
from src.events.events import CustomEvents
from src.utils.typewriter import TypewriterConfig


class Menu(pg.sprite.Sprite):
    size = pg.Vector2(
        x=9 * s.TILESIZE,
        y=7 * s.TILESIZE
    )
    pos = pg.Vector2(
        x=30 * s.TILESIZE,
        y=s.TILESIZE
    )
    text_buttons_cfg = TypewriterConfig(
        pos='center',
        color=s.GREEN,
        size=22
    )

    def __init__(self, sprite_group):
        self.sprite_group = sprite_group
        super().__init__(self.sprite_group)
        self.image = pg.Surface(self.size)
        self.image.fill(s.DARKGREY)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.buttons = pg.sprite.Group(*self._create_buttons())

    def _create_buttons(self):
        size = pg.Vector2(
            x=7 * s.TILESIZE,
            y=2 * s.TILESIZE
        )
        return [
            Button(
                size=size,
                pos=pg.Vector2(s.TILESIZE, s.TILESIZE),
                text='New',
                on_click=CustomEvents.START_GAME,
                text_cfg=self.text_buttons_cfg,
                parent_transform=self.pos,
                parent_surface=self.image
            ),
            Button(
                size=size,
                pos=pg.Vector2(s.TILESIZE, s.TILESIZE * 2 + size.y),
                text='Quit',
                on_click=pg.QUIT,
                text_cfg=self.text_buttons_cfg,
                parent_transform=self.pos,
                parent_surface=self.image
            )
        ]

    def update(self, dt):
        self.buttons.update(dt)
