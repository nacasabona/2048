from enum import Enum

import pygame as pg


class CustomEvents(Enum):
    START_GAME = pg.event.custom_type()
