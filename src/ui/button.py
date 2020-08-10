from typing import Union

import pygame as pg

import src.settings as s
from src.events.overseer import Overseer
from src.events.events import CustomEvents
from src.utils.typewriter import TypewriterConfig, write


class Button(pg.sprite.Sprite):
    color = s.BLACK
    hover_color = s.DARKGREEN
    text = s.GREEN

    def __init__(
            self, size: pg.Vector2, pos: pg.Vector2,
            text: str, on_click: Union[CustomEvents, int]
    ):
        super().__init__()
        self._register_listeners()
        self.text = text
        self.image = pg.Surface(size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=pos)
        self.hover = False
        self.on_click = on_click

    def draw_text(self):
        cfg = TypewriterConfig(
            pos='center',
            color=s.GREEN,
            size=22
        )
        write(self.image, self.text, config=cfg)

    def _register_listeners(self):
        Overseer.add_listener(pg.MOUSEMOTION, self)
        Overseer.add_listener(pg.MOUSEBUTTONUP, self)

    def update(self):
        if self.hover:
            self.image.fill(self.hover_color)
        else:
            self.image.fill(self.color)
        self.draw_text()

    def on_notify(self, event):
        # we can test collisions this way because we are only subscribed for
        # mouse events, otherwise "event" might have no attr "pos".
        if self.rect.collidepoint(event.pos):
            self.hover = True
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                dispatch = pg.event.Event(
                    # FIXME: this is not very pretty, we want the button to be
                    #        able to broadcast not only a CustomEvent but also
                    #        a pygame native event.
                    pg.USEREVENT if self.on_click in CustomEvents
                    else self.on_click,
                    {'custom_type': self.on_click}
                )
                pg.event.post(dispatch)
        else:
            self.hover = False
