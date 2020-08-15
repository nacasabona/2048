from typing import Union, Tuple

import pygame as pg

import src.settings as s
from src.events.overseer import Overseer
from src.events.events import CustomEvents
from src.utils.math import lerp, clamp
from src.utils.typewriter import TypewriterConfig, write


class Button(pg.sprite.Sprite):
    on_hover_in_time = 0.3
    on_hover_out_time = 0.5

    def __init__(
            self, size: pg.Vector2, pos: pg.Vector2,
            text: str, on_click: Union[CustomEvents, int],
            parent_surface: pg.Surface,
            text_cfg: TypewriterConfig = TypewriterConfig(),
            color: pg.Vector3 = s.BLACK,
            hover_color: pg.Vector3 = s.DARKGREEN,
            parent_transform: pg.Vector2 = pg.Vector2(0, 0)
    ):
        super().__init__()
        self._register_listeners()
        self.pos = pos
        self.text = text
        self.text_cfg = text_cfg
        self.color = color
        self.hover_color = hover_color
        self.parent_surface = parent_surface
        self.parent_transform = parent_transform
        self.image = pg.Surface(size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.hover = False
        self.lerp_t = 0
        self.on_click = on_click
        self.draw_text()

    def draw_text(self):
        write(
            surface=self.image,
            text=self.text,
            config=self.text_cfg,
        )

    def _register_listeners(self):
        Overseer.add_listener(pg.MOUSEMOTION, self)
        Overseer.add_listener(pg.MOUSEBUTTONUP, self)

    def update(self, dt):
        if self.hover:
            self.lerp_t = clamp(0, 1, self.lerp_t + dt / self.on_hover_in_time)
        else:
            self.lerp_t = clamp(0, 1, self.lerp_t - dt / self.on_hover_out_time)
        color = lerp(
            self.color,
            self.hover_color,
            self.lerp_t
        )
        self.image.fill(color)
        self.draw_text()
        self.parent_surface.blit(self.image, self.rect)

    def on_notify(self, event):
        # we can test collisions this way because we are only subscribed for
        # mouse events, otherwise "event" might have no attr "pos".
        if self.rect.collidepoint(event.pos - self.parent_transform):
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
