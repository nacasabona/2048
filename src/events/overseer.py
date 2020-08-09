import logging
from typing import Any
from collections import defaultdict

import pygame as pg

from src.events.events import CustomEvents


class CustomEventHasNoName(Exception):
    pass


class CustomEventIsNotDefined(Exception):
    pass


class Overseer:
    _instance = None
    listeners = defaultdict(list)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    @classmethod
    def add_listener(cls, event_type, entity: Any):
        if event_type in CustomEvents:
            name = event_type.name
        else:
            name = pg.event.event_name(event_type)
        logging.debug(
            'Registering listener: %r for event %r',
            entity, name
        )
        cls.listeners[event_type].append(entity)

    @classmethod
    def broadcast(cls, event):
        logging.debug('Broadcasting: %r', event)
        name = event.type
        if event.type == pg.USEREVENT:
            sanitize_user_event(event)
            name = event.custom_type

        for listener in cls.listeners[name]:
            listener.on_notify(event)


def sanitize_user_event(event):
    if not hasattr(event, 'custom_type'):
        raise CustomEventHasNoName((
            f'User handled event "{event!r}" needs '
            'a "custom_type" attribute'
        ))
    if not isinstance(event.custom_type, CustomEvents):
        raise CustomEventIsNotDefined((
            f'User handled event "{event!r}" is not a member of '
            'CustomEvents(Enum)'
        ))
