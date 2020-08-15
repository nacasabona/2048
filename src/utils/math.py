from typing import Union

import pygame as pg


def clamp(
    min_: Union[float, int],
    max_: Union[float, int],
    val: Union[float, int]
) -> Union[float, int]:
    if val < min_:
        return min_
    if val > max_:
        return max_
    return val


def lerp(
    a: Union[float, int, pg.Vector2, pg.Vector3],
    b: Union[float, int, pg.Vector2, pg.Vector3],
    t: float
) -> Union[float, int, pg.Vector2, pg.Vector3]:
    return a * (1 - t) + b * t
