import copy
import logging
from pathlib import Path

import pygame as pg

import src.settings as s
from src.grid import Grid
from src.ui.tile import Tile
from src.ui.panel import Panel
from src.events.overseer import Overseer
from src.events.events import CustomEvents


logger = logging.getLogger(Path(__file__).stem)


class Board(pg.sprite.Sprite):
    backdrop_size = pg.Vector2(28*s.TILESIZE, 28*s.TILESIZE)
    backdrop_pos = pg.Vector2(s.TILESIZE, s.TILESIZE)
    tile_size = pg.Vector2(6*s.TILESIZE, 6*s.TILESIZE)
    margin = s.TILESIZE // 4
    padding = s.TILESIZE * 1.5

    def __str__(self):
        return "\n".join([str(row) for row in self.matrix])

    def __len__(self):
        return len(self.matrix)

    def __getitem__(self, item):
        return self.matrix[item]

    def __init__(self, sprite_group):
        self.sprite_group = sprite_group
        super().__init__(self.sprite_group)
        self.playing = False
        self.grid = None
        self._register_listeners()
        self._draw_backdrop()
        self.matrix = [[2] * 4 for i in range(4)]

    def _draw_backdrop(self):
        self.image = pg.Surface(self.backdrop_size)
        self.image.fill(s.DARKGREY)
        self.rect = self.image.get_rect(topleft=self.backdrop_pos)

    def _register_listeners(self):
        Overseer.add_listener(pg.KEYDOWN, self)
        Overseer.add_listener(CustomEvents.START_GAME, self)

    def new(self):
        self.grid = Grid()
        self.playing = True

    def update(self, dt):
        if not self.playing:
            return
        for i in range(len(self)):
            x_pos = self.padding + i * (self.tile_size.x + self.margin)
            for j in range(len(self[i])):
                y_pos = self.padding + j * (self.tile_size.y + self.margin)
                tile = Tile(
                    pos=pg.Vector2(x_pos, y_pos),
                    size=self.tile_size,
                    value=self[j][i]
                )
                self.image.blit(tile.image, tile.rect)

    def move(self, direction):
        old_matrix = copy.deepcopy(self.matrix)
        if direction == pg.K_UP:
            self.matrix = self.grid.move_up(self.matrix)
        elif direction == pg.K_DOWN:
            self.matrix = self.grid.move_down(self.matrix)
        elif direction == pg.K_LEFT:
            self.matrix = self.grid.move_left(self.matrix)
        elif direction == pg.K_RIGHT:
            self.matrix = self.grid.move_right(self.matrix)
        if old_matrix != self.matrix:
            self.matrix = self.grid.add_rdm_tile(self.matrix)

    def on_notify(self, event):
        if event.type == pg.KEYDOWN:
            self.move(event.key)
        if event.type == pg.USEREVENT:
            if event.custom_type == CustomEvents.START_GAME:
                self.new()
