import logging
from pathlib import Path
from typing import Any
from collections import defaultdict

import pygame as pg


logger = logging.getLogger(Path(__file__).stem)


class Overseer:
    _instance = None
    listeners = defaultdict(list)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def add_listener(cls, event_type, entity: Any):
        name = pg.event.event_name(event_type)
        logger.debug(
            'Registering listener: %r for event %r',
            entity, name
        )
        cls.listeners[event_type].append(entity)

    @classmethod
    def broadcast(cls, event):
        logger.debug('Broadcasting: %r', event)
        name = event.type

        for listener in cls.listeners[name]:
            listener.on_notify(event)
