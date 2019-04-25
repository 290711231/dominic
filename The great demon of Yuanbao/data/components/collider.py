__author__ = 'dominic'

import pygame as pg
from .. import constants as c


class Collider(pg.sprite.Sprite):
    """Invisible sprites placed overtop background parts that can be collided with (pipes, steps, ground, etc.
    放置在背景部分的，可与之（管道，台阶，地面等）碰撞的不可见的sprites动画"""

    def __init__(self, x, y, width, height, name='collider'):
        pg.sprite.Sprite.__init__(self)
        # self.image =创建一个Surface对象，且不含透明通道
        self.image = pg.Surface((width, height)).convert()
        # self.image.fill(c.RED)
        # 获取self.image的矩形信息
        self.rect = self.image.get_rect()

        # 重新赋予rect坐标
        self.rect.x = x
        self.rect.y = y

        self.state = None
