#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
import random


class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.screen = screen_temp
        self.x = x + 70 - 8
        self.y = y + 15
        self.image = pygame.image.load("./image/bullet_7.png")
        self.enemyimage = pygame.image.load('./image/bullet_2.png')

    def dispaly(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        #英雄的子弹移动
        self.x += 10

    def enemymove(self):
        #敌人的子弹移动
        self.x -= 10

    def judge(self):
        #判断英雄的子弹越界
        if self.x > 850:
            return True
        else:
            return False

    def enemyjudge(self):
        #判断敌人的子弹越界
        if self.x < -50:
            return True
        else:
            return False


