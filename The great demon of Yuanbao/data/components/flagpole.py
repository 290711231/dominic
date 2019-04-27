__author__ = 'dominic'

import pygame as pg
from .. import setup
from .. import constants as c

class Flag(pg.sprite.Sprite):
    """Flag on top of the flag pole at the end of the level
    关卡结束处旗杆上的旗子
    继承自pygame.sprite.Sprite类"""
    def __init__(self, x, y):
        super(Flag, self).__init__()
        # self.sprite_sheet指向图片材质集中的'item_objects'键指向的值（即：item_objects.png）
        self.sprite_sheet = setup.GFX['item_objects']
        # 调用self.setup.images()类设置一个图片帧的列表
        self.setup_images()
        # 将真列表中第一个对象赋值给self.image
        self.image = self.frames[0]
        # 获取image的坐标和宽高信息赋值给self.rect
        self.rect = self.image.get_rect()
        # 将传入的x值赋给self.rect.right
        self.rect.right = x
        # 将传入的y值赋给self.rect.y
        self.rect.y = y
        # 当前状态为'top of pole'
        self.state = c.TOP_OF_POLE


    def setup_images(self):
        """Sets up a list of image frames
        设置一个图片帧的列表"""
        # 定义帧列表
        self.frames = []

        # 将坐标为（128,32）宽高为16,16传入self.get_image方法，进行实例化并缩放
        # 将返回的image对象添加到帧列表self.frames中
        self.frames.append(
            self.get_image(128, 32, 16, 16))


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet
        图片材质集中提取图片"""
        # 用pg.Surface类实例化image
        image = pg.Surface([width, height])
        # 获取image的坐标和宽高信息
        rect = image.get_rect()

        # 将image绘制出来
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # 将image中rgb为(0, 0, 0)，即黑色的部分设置成透明
        image.set_colorkey(c.BLACK)
        # 将image缩放成原来的c.BRICK_SIZE_MULTIPLIER倍（即：2.69倍）并取整，将结果重新赋值给image对象
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        # 将image返回
        return image


    def update(self, *args):
        """Updates behavior
        更新旗子状态"""
        # 调用self.handle_state()方法
        self.handle_state()


    def handle_state(self):
        """Determines behavior based on state
        根据状态来确定行为"""
        # 判断当前状态是否为'top of pole'
        if self.state == c.TOP_OF_POLE:
            # self.image指向帧列表self.frames的第一个值
            self.image = self.frames[0]
        # 判断当前状态是否为'slide down'
        elif self.state == c.SLIDE_DOWN:
            # 调用self.sliding_down()方法，让旗子降下来
            self.sliding_down()
        # 判断当前状态是否为'bottom of pole'
        elif self.state == c.BOTTOM_OF_POLE:
            # self.image指向帧列表self.frames的第一个值
            self.image = self.frames[0]


    def sliding_down(self):
        """State when Mario reaches flag pole
        当马里奥碰到旗杆时候的状态"""
        # 设置降旗的速度为5
        self.y_vel = 5
        # 将旗子的y坐标 + 降旗速度的结果 重新赋值给旗子的y坐标
        self.rect.y += self.y_vel

        # 判断旗子的位置的底部是否为 485
        if self.rect.bottom >= 485:
            # 当前状态变为'bottom of pole'
            self.state = c.BOTTOM_OF_POLE


class Pole(pg.sprite.Sprite):
    """Pole that the flag is on top of
    旗子所在旗杆
    继承自 pygeme.sprite.Sprite类"""
    def __init__(self, x, y):
        super(Pole, self).__init__()
        # self.sprite_sheet指向图片集字典中'tile_set'键的值（即：tile_set.png）
        self.sprite_sheet = setup.GFX['tile_set']
        # 调用self.setup_frames()设置一个图片帧列表
        self.setup_frames()
        # 将帧列表中的第一个值赋给self.image
        self.image = self.frames[0]
        # 获取self.image的坐标和宽高信息，并赋值给self.rect
        self.rect = self.image.get_rect()
        # 重新给rect的坐标赋值
        self.rect.x = x
        self.rect.y = y


    def setup_frames(self):
        """Create the frame list
        创建帧列表"""
        self.frames = []

        # 将坐标为（263,144）宽高为2,16传入self.get_image方法，进行实例化并缩放
        # 将返回的image对象添加到帧列表self.frames中
        self.frames.append(
            self.get_image(263, 144, 2, 16))


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet
        从图片材质集（即：tile_set.png）中提取图片"""
        # 用pg.Surface类实例化image
        image = pg.Surface([width, height])
        # 获取image的坐标和宽高信息，并赋值给rect
        rect = image.get_rect()

        # 将image绘制出来
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # 将rgb为（0,0,0）的颜色设置成透明
        image.set_colorkey(c.BLACK)
        # 将image的宽高缩放成原来的c.BRICK_SIZE_MULTIPLIER倍（即：2.69倍）再取整，并重新赋值给image
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        # 返回image对象
        return image


    def update(self, *args):
        """Placeholder for update, since there is nothing to update
        用于更新的占位符，因为没有更新。。。。。"""
        pass


class Finial(pg.sprite.Sprite):
    """The top of the flag pole
    旗杆的顶部
    继承自 pygeme.sprite.Sprite类"""
    def __init__(self, x, y):
        super(Finial, self).__init__()
        # self.sprite_sheet指向图片集字典中'tile_set'键的值（即：tile_set.png）
        self.sprite_sheet = setup.GFX['tile_set']
        # 调用self.setup_frames类创建帧列表
        self.setup_frames()
        # 将帧列表self.frames的第一个元素，赋值给self.image
        self.image = self.frames[0]
        # 获取self.image的坐标和宽高信息
        self.rect = self.image.get_rect()
        # 重新给rect的坐标赋值
        self.rect.centerx = x
        self.rect.bottom = y


    def setup_frames(self):
        """Creates the self.frames list
        创建帧列表"""
        self.frames = []

        # 将坐标为（228,120）宽高为8,8传入self.get_image方法，进行实例化并缩放
        # 将返回的image对象添加到帧列表self.frames中
        self.frames.append(
            self.get_image(228, 120, 8, 8))


    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet
        从帧列表中提取图片"""
        # 用pg.Surface类实例化image
        image = pg.Surface([width, height])
        # 获取image的坐标和宽高信息，并赋值给rect
        rect = image.get_rect()

        # 绘制image对象
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # 将rgb为（0,0,0）的颜色（即：黑色）设置成透明
        image.set_colorkey(c.BLACK)
        # 将image的宽高缩放成原来的c.SIZE_MULTIPLIER倍（即：2.5倍），再取整，并重新赋值给image
        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        # 返回image对象
        return image


    def update(self, *args):
        '''还是没啥用，占个坑把。。。。'''
        pass



