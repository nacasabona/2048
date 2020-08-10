import random as r
from src.grid import Grid
import pygame as pg
from src.events.overseer import Overseer
import logging
from pathlib import Path

logger = logging.getLogger(Path(__file__).stem)

class Board:

    def __init__(self):
        self.score = 0
        self.game_over = False
        self.grid = Grid()
        self._register_listeners()

    def move(self, direction):
        pass

    # esto estaría en el loop principal fichando si ya terminó el juego
    def is_game_over(self):
        if self.game_over:
            pass

    def _register_listeners(self):
        Overseer.add_listener(pg.KEYDOWN, self)

    #esto es para que registre las teclas y las mande a grid
    def on_notify(self,event):
        logger.debug(event)


