__author__ = 'dominic'

"""
This module initializes the display and creates dictionaries of resources.
此模块初始化显示并创建资源字典。
"""

import os
import pygame as pg
from . import tools
from .import constants as c

ORIGINAL_CAPTION = c.ORIGINAL_CAPTION

#强制静态位置
os.environ['SDL_VIDEO_CENTERED'] = '1'
#将pg（pygame）初始化
pg.init()
#KEYDOWN、KEYUP和QUIT是被允许的时间
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
#窗体的名字被设定为 :c.ORIGINAL_CAPTION(即：Super Mario Bros 1-1)
pg.display.set_caption(c.ORIGINAL_CAPTION)
#设置窗体大小为：c,SCREEN_SIZE
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)
#获取SCREEN的矩形区域范围
SCREEN_RECT = SCREEN.get_rect()

#FONTS 通过函数得到resources/fonts目录下的字体字典
FONTS = tools.load_all_fonts(os.path.join("resources","fonts"))
#MUSIC 通过函数得到resources/music目录下的背景音乐字典
MUSIC = tools.load_all_music(os.path.join("resources","music"))
#GFX 通过函数得到resources/graphics目录下的图集字典
GFX   = tools.load_all_gfx(os.path.join("resources","graphics"))
#SFX 通过函数的到resources/sound目录下的音效字典
SFX   = tools.load_all_sfx(os.path.join("resources","sound"))