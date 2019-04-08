#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Cloud import *
import pygame
import random

class Backgroud(object):
    def __init__(self, screen_temp):
        self.cloud_x = 800
        self.cloud_y = random.randrange(80,160)
        self.screen = screen_temp
        self.image = pygame.image.load("./image/backgroud.jpg").convert()
        self.bgimage_1 = BackgroudImage(self.screen,'backgroud_1',0,238,0.3)
        self.bgimage_2 = BackgroudImage(self.screen,'backgroud_2',0,0,0.1)
        self.cloud = Cloud(screen_temp, self.cloud_x, self.cloud_y)
        self.cloud_list = []
        self.backgroudlist_1 = []
        self.backgroudlist_2 = []


    def display(self):
        #载入背景
        self.screen.blit(self.image, (0, 0))
        #self.screen.blit(self.bgimage_1.image,(0,47))
        #self.bgimage_1.move()

        #载入后面的天空
        self.backgroudlist_2.append(BackgroudImage(self.screen,'backgroud_2',1020,0,0.3))
        #elif len(self.backgroudlist_2)==1:
        #    self.backgroudlist_2.append(BackgroudImage(self.screen, 'backgroud_2', 0, 0, 0.3))
        self.bgimage_2.display()
        self.bgimage_2.move()
        self.bgimage_2.judge()

        #for baimage2 in self.backgroudlist_2:
        #    baimage2.display()
        #    baimage2.move()
        #    baimage2.judge()


        #载入天空中的云
        i = random.randrange(1, 300)
        if i == 40 or i == 80 or i == 120:
            self.cloud_list.append(Cloud(self.screen, self.cloud_x, self.cloud_y))

        for cloud_i in self.cloud_list:
            cloud_i.display()
            cloud_i.move()
            if cloud_i.judge():
                self.cloud_list.remove(cloud_i)
                print('____________cloud be remove____________')

        #载入后面的大树背景
        self.bgimage_1.display()
        self.bgimage_1.move()

class BackgroudImage(object):
    def __init__(self, screen_temp,temp_image,temp_x,temp_y,temp_speed):
        self.screen = screen_temp
        self.bgimage = temp_image
        self.x = temp_x
        self.y = temp_y
        self.image = pygame.image.load('./image/%s.png'%self.bgimage).convert_alpha()
        self.speed = temp_speed

    def display(self):

        self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.image,(self.x+510,self.y))

        print('%s be display'%self.bgimage)

    def move(self):
        self.x -= self.speed
        #print('now x is %d'%self.x)

    def judge(self):
        #判断越界
        if self.x < -510:
            return True
        else:
            return False