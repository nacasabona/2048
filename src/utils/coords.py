from math import ceil

import pygame as pg

import src.settings as s


class Coords(pg.math.Vector2):

    @property
    def row(self):
        return ceil(self.y / s.TILESIZE)

    @property
    def col(self):
        return ceil(self.x / s.TILESIZE)

    def __str__(self):
        return (
            f'(x={int(self.x)}, y={int(self.y)}) -> '
            f'(row={self.row}, col={self.col})'
        )
