from enum import Enum

import pygame as pg


class CustomEventHasNoName(Exception):
    pass


class CustomEventIsNotDefined(Exception):
    pass


class CustomEvents(Enum):
    START_GAME = pg.event.custom_type()
