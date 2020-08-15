from pathlib import PurePath

import pygame as pg


# Game general config
CAPTION = '2048'
HEIGHT = 480
WIDTH = 640
FPS = 30
TILESIZE = 16
FONT_PATH = str(PurePath('assets', 'fonts', 'redalert_inet.ttf'))
LIST_NUM = [2, 4]
LIST_PROB = [0.8, 0.2]


# Logging config
LEVEL = 'DEBUG'


# define some colors (R, G, B)
WHITE = pg.Vector3(255, 255, 255)
BLACK = pg.Vector3(0, 0, 0)
DARKGREY = pg.Vector3(40, 40, 40)
LIGHTGREY = pg.Vector3(100, 100, 100)
GREEN = pg.Vector3(102, 255, 102)
LIGHTGREEN = pg.Vector3(51, 255, 51)
DARKGREEN = pg.Vector3(0, 128, 0)
RED = pg.Vector3(255, 0, 0)
YELLOW = pg.Vector3(255, 255, 0)
LIGHTBLUE = pg.Vector3(133, 180, 255)
BLUE = pg.Vector3(28, 115, 255)
LIGHTPURPLE = pg.Vector3(195, 171, 255)
