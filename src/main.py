import logging

import pygame as pg

import src.settings as s
from src.game import Game


def configure_pygame():
    pg.init()
    # después van a venir los ruiditos
    pg.mixer.init()
    pg.display.set_caption(s.CAPTION)


def configure_logging():
    logging.basicConfig(
        format='[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s',
        datefmt='%I:%M:%S %p',
        level=getattr(logging, s.LEVEL)
    )


if __name__ == '__main__':
    configure_logging()
    configure_pygame()
    game = Game()
    game.run()
