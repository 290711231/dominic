__author__ = 'dominic'

import pygame as pg
from .. import setup
from .. import constants as c


class Coin(pg.sprite.Sprite):
    """Flashing coin next to coin total info
    闪烁硬币旁边的硬币总信息"""
    def __init__(self, x, y):
        super(Coin, self).__init__()
        #用setup.GFX方法传入‘item_objects’来实例化图片item_objects.png
        self.sprite_sheet = setup.GFX['item_objects']
        self.create_frames()
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.timer = 0
        self.first_half = True
        self.frame_index = 0


    def create_frames(self):
        """Extract coin images from sprite sheet and assign them to a list
        从sprite工作表中提取硬币图像并将其分配到一个列表中"""
        #定义帧列表self.frames，并将帧索引设为0
        self.frames = []
        self.frame_index = 0

        # 给帧列表添加三个元素
        self.frames.append(self.get_image(1, 160, 5, 8))
        self.frames.append(self.get_image(9, 160, 5, 8))
        self.frames.append(self.get_image(17, 160, 5, 8))


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet
        从sprite sheet中提取图像"""
        #根据参数（width，height）定义image图片
        image = pg.Surface([width, height])
        #获取图片信息
        rect = image.get_rect()

        #根据参数在屏幕上将image对象显示出来
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        #rgb值为（0,0,0）的颜色变成透明的
        image.set_colorkey(c.BLACK)
        #将image缩放，宽和高都变成原先的 2.69 倍，并取整，再重新赋值给image
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        #返回image
        return image


    def update(self, current_time):
        """Animates flashing coin
        动画闪烁的金币"""
        if self.first_half: #判断self.first_half是否为真
            if self.frame_index == 0:   #判断帧索引是否为0
                if (current_time - self.timer) > 375:   #判断当前时间减去self.time是否大于375
                    #帧索引 += 1
                    self.frame_index += 1
                    #self.time = 当前时间
                    self.timer = current_time
            elif self.frame_index < 2:  #判断帧索引是否小于2
                if (current_time - self.timer) > 125:   #判断当前时间减去self.timer是否大于125
                    #帧索引 += 1
                    self.frame_index += 1
                    self.timer = current_time
            elif self.frame_index == 2:
                if (current_time - self.timer) > 125:
                    self.frame_index -= 1
                    self.first_half = False
                    self.timer = current_time
        else:
            if self.frame_index == 1:
                if (current_time - self.timer) > 125:
                    self.frame_index -= 1
                    self.first_half = True
                    self.timer = current_time

        self.image = self.frames[self.frame_index]