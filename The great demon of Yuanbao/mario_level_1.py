#!/usr/bin/env python
__author__ = 'dominic'

"""
This is an attempt to recreate the first level of
Super Mario Bros for the NES.
"""

import sys
import pygame as pg
from data.main import main
import cProfile


if __name__=='__main__':
    #调用data下的main函数
    main()
    #调用pygame下quit函数
    pg.quit()
    #调用sys下的exit函数退出
    sys.exit()