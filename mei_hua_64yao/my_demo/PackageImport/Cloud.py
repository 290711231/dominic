#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pygame
import random

class Cloud(object):
    def __init__(self, screen_temp, x, y):
        self.screen = screen_temp
        self.x = x
        self.y = y
        self.cloudnum = random.randrange(1,4)
        self.image = pygame.image.load('./image/cloud-%d.png'%self.cloudnum).convert_alpha()
        self.random_size = random.uniform(0.4, 0.7)
        self.cloud_speed = 10-int(10 * self.random_size) - 2
        self.tempNum = self.random_size
        self.transform = pygame.transform.smoothscale(self.image, (int(562 * self.tempNum), int(432 * self.tempNum)))
        self.cloud_list = []

    def display(self):
        self.screen.blit(self.transform, (self.x, self.y))
        #print('cloud be display')

    def move(self):
        self.x -= self.cloud_speed
        #print('cloud x=%d  y=%d' % (self.x, self.y))

    def judge(self):
        #判断云的越界
        if self.x < -360:
            return True
        else:
            return False