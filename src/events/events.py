import pygame as pg


class CustomEvents:
    START_GAME = pg.event.custom_type()
    PLAY_ANIMATION = pg.event.custom_type()
    PAUSE_ANIMATION = pg.event.custom_type()
    RESTART_ANIMATION = pg.event.custom_type()
    W_ALIGN_CHANGE_ANIMATION = pg.event.custom_type()
    W_COHESION_CHANGE_ANIMATION = pg.event.custom_type()
    W_SEP_CHANGE_ANIMATION = pg.event.custom_type()
    VIEW_RADIUS_CHANGE_ANIMATION = pg.event.custom_type()
    MAX_STEER_FORCE_ANIMATION = pg.event.custom_type()
