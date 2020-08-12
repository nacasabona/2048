from enum import Enum, EnumMeta

import pygame as pg


class CustomEventHasNoName(Exception):
    pass


class CustomEventIsNotDefined(Exception):
    pass


class CustomEnumMeta(EnumMeta):
    def __contains__(self, item):
        try:
            return super().__contains__(item)
        except TypeError:
            return False


class CustomEvents(Enum, metaclass=CustomEnumMeta):
    START_GAME = pg.event.custom_type()
