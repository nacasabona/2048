import pygame as pg

import src.settings as s
from src.game import Game


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((s.WIDTH, s.HEIGHT))
    pg.display.set_caption('2048')
    clock = pg.time.Clock()
    game = Game(screen)
    game.run()

