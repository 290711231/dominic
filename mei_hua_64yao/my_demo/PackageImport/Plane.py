#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Bullet import *
import pygame
from Curve import enemycurve
import numpy as np
import time

class Plane(object):
    def __init__(self,screen_temp,image_temp):
        self.screen =screen_temp
        self.image =pygame.image.load('./image/%s.png'%image_temp)

class HeroPlane(Plane):
    def __init__(self, screen_temp):
        Plane.__init__(self,screen_temp,'myplane-1')
        self.x = 0
        self.speed = 5
        self.y = 200
        self.Herobullet = Bullet(screen_temp, self.x, self.y)
        self.bullet_list = [Bullet(self.screen, self.x, self.y)] * 10

    #def animate(self):
    #    rangenum(22)
    #    self.image =pygame.image.load('./image/myplane-%d.png'%self.image_temp)

    def moveleft(self):
        print('left     %d' % self.x)
        self.x -= self.speed

    def moveright(self):
        #print('right    %d' % self.x)
        self.x += self.speed

    def moveup(self):
        #print('up   %d' % self.y)
        self.y -= self.speed

    def movedown(self):
        #print('down     %d' % self.y)
        self.y += self.speed

    def fire(self):
        #开火
        #print('fire  x=%d   y=%d' % (self.x, self.y))
        #print(self.bullet_list)
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

    def dispaly(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullettemp in self.bullet_list:
            bullettemp.dispaly()
            bullettemp.move()
            if bullettemp.judge():
                self.bullet_list.remove(bullettemp)

class EnemyPlane(Plane):

    def __init__(self, screen_temp):
        Plane.__init__(self,screen_temp,'enemy_1_1')
        self.x = 800
        self.y = random.randint(40,240)
        self.xlist = np.arange(789,800,0.1)
        self.ylist = np.sin(self.xlist) * 40
        self.enemycoordinate = enemycurve()
        self.speed = random.uniform(1.5, 2.2)
        #self.enemybullet = Bullet(screen_temp, self.x, self.y)
        #self.enemybullet_list = [Bullet(self.screen, self.x, self.y)] * 10


    def move(self):
        for x in self.xlist:
            for y in self.ylist:
                self.x -= x
                self.y += y
                self.screen.blit(self.image, (self.x, self.y))



    #def fire(self):
    #    for enemybulletnum in random.randrange(1,200):
    #        if enemybulletnum == 40 or enemybulletnum == 50:
    #            #print('enemy fire  x=%d   y=%d' % (self.x-66, self.y+44))
    #            #print(self.enemybullet_list)
    #            self.enemybullet_list.append(Bullet(self.screen, self.x, self.y))

    #def dispaly(self):
    #    #enemycurve.num(self)
    #    self.screen.blit(self.image, (self.x,self.y))
    #    #for add_enemybulletnum in range(1,501):
    #    #    if add_enemybulletnum%50 == 0:
    #    #        for bullettemp in self.enemybullet_list:
    #    #            bullettemp.dispaly()
    #    #            bullettemp.enemymove()
    #    #            if bullettemp.enemyjudge():
    #    #                self.enemybullet_list.remove(bullettemp)

