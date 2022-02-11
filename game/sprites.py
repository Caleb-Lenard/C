import pygame as pg
from settings import *

class Units(pg.sprite.Sprite):
    def __init__(self, game, units):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.units = 0

    def add_unit(self):
        self.units = self.units + 1