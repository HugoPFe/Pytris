import pygame as pg
from pygame.locals import *
from pygame.math import Vector2

from constants import *


class ZBlock(pg.sprite.Sprite):
    def __init__(self, x, y, sprite_group):
        super().__init__()

        self.image = pg.Surface((10, 10))
        self.image.fill('red')
        self.pos = Vector2(x, y)
        self.rect = self.image.get_rect(center=self.pos)

        sprite_group.add(self)

    def update(self):
        pass


__all__ = [
    'ZBlock'
]