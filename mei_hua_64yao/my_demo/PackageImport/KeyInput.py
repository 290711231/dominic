#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
from sys import exit

def keyControl(HeroPlane):
    #键盘控制
    for event in pygame.event.get():
        if event.type == QUIT:
            print('quit')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                HeroPlane.fire()

    key = pygame.key.get_pressed()

    if key[K_LEFT] or key[K_a]:
        HeroPlane.moveleft()
    elif key[K_RIGHT] or key[K_d]:
        HeroPlane.moveright()
    elif key[K_DOWN] or key[K_s]:
        HeroPlane.movedown()
    elif key[K_UP] or key[K_w]:
        HeroPlane.moveup()
    # elif key[K_SPACE]:
    #    HeroPlane.fire()

    if HeroPlane.x < 0:
        HeroPlane.x = 0
    elif HeroPlane.x > 690:
        HeroPlane.x = 690

    elif HeroPlane.y < 0:
        HeroPlane.y = 0  #
    elif HeroPlane.y > 450:
        HeroPlane.y = 450