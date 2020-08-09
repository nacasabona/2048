from enum import Enum

import pygame as pg


class CustomEvents(Enum):
    StartGame = pg.event.custom_type()
