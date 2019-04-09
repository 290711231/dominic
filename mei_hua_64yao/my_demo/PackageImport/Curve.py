# -*- coding: utf-8 -*-

import numpy as np
import random

class curve(object):
    def __init__(self,start,crestnum,smoothness):
        self.x =x = np.arange(start,crestnum* np.pi,smoothness)*100
        self.y  = y = np.sin(x)


class enemycurve(curve):
    def __init__(self):
        curve.__init__(self,0,8,0.5)
        self.randy = random.randrange(50,450)
        self.enemyx = 800-self.x
        self.enemyy = self.randy -self.y
        self.xlist = []
        self.ylist = []

    #def num(self):
    #    while self.x == -100:
    #        x = np.arange(0, 20 * np.pi / 10, 0.1) * 60
    #        y = np.sin(x) * 40
    #        self.xlist.append(x)
    #        self.ylist.append(y)


