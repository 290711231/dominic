__author__ = 'dominic'

import pygame as pg
from .. import constants as c
from .. import setup


class Powerup(pg.sprite.Sprite):
    """Base class for all powerup_group
    所有powerup_group类的基类"""
    def __init__(self, x, y):
        super(Powerup, self).__init__()


    def setup_powerup(self, x, y, name, setup_frames):
        """This separate setup function allows me to pass a different
        setup_frames method depending on what the powerup is
        这个单独的setup函数，允许我根据powerup是什么来判断传递不同的setup_frames方法。"""
        # self.sprite_sheet 指向图片材质集字典中'item_objects'键指向的值（即：item_objects,png）
        self.sprite_sheet = setup.GFX['item_objects']
        # 定义帧列表
        self.frames = []
        # 定义帧索引
        self.frame_index = 0
        # 调用setup_frames()来添加帧列表里的内容
        setup_frames()
        # 将帧列表中帧索引指向的值赋给self.image
        self.image = self.frames[self.frame_index]
        # 获取image的坐标和位置信息
        self.rect = self.image.get_rect()
        # 重新赋值给self.rect.centerx 和self.rect
        self.rect.centerx = x
        self.rect.y = y
        # 当前状态为'reveal'
        self.state = c.REVEAL
        # 设置xy的速度
        self.y_vel = -1
        self.x_vel = 0
        # 移动朝向self.direction为'right'
        self.direction = c.RIGHT
        # 定义变量
        self.box_height = y
        self.gravity = 1
        self.max_y_vel = 8
        self.animate_timer = 0
        self.name = name


    def get_image(self, x, y, width, height):
        """Get the image frames from the sprite sheet
        从sprite材质集中获取图片帧"""

        # 向pygeme.Surface传入参数,来实例化对象image，且没有alpha通道
        image = pg.Surface([width, height]).convert()
        # 获取image的位置和宽高信息
        rect = image.get_rect()

        # 绘制image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # 将image中rgb为（0,0,0）的颜色（即：黑色）设置成透明
        image.set_colorkey(c.BLACK)

        # 将image缩放成原来的c.SIZE_MULTIPLIER倍（即：2.5倍），并重新赋值给image对象
        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        # 返回image对象
        return image


    def update(self, game_info, *args):
        """Updates powerup behavior
        更新powerup行为"""
        # 当前时间 = 字典game_info中c.CURRENT_TIME（即：'current time'）指向的值
        self.current_time = game_info[c.CURRENT_TIME]
        # 调用self.handle_state()函数
        self.handle_state()


    def handle_state(self):
        pass


    def revealing(self, *args):
        """Action when powerup leaves the coin box or brick
        当powerup离开盒子或者砖块时候的行为"""
        # y轴的坐标位置 + 速度的结果重新赋值给 y轴坐标
        self.rect.y += self.y_vel

        # 判断底部位置是否小于等于盒子的高
        if self.rect.bottom <= self.box_height:
            # 底部位置 = 盒子的高
            self.rect.bottom = self.box_height
            # y轴速度 = 0
            self.y_vel = 0
            # 当前状态为'slide'
            self.state = c.SLIDE


    def sliding(self):
        """Action for when powerup slides along the ground
        当powerup沿着地面滑行时候的动作"""
        # 判断朝向self.direction是否为'right'
        if self.direction == c.RIGHT:
            # x速度 = 3
            self.x_vel = 3
        # 否则
        else:
            # x速度 = -3
            self.x_vel = -3


    def falling(self):
        """When powerups fall of a ledge
        当powerup从台子上掉下来的时候"""
        # 判断y轴的速度是否小于8
        if self.y_vel < self.max_y_vel:
            # y轴的速度 + 重力（即：1）的结果重新赋值给y轴速度，即加速
            self.y_vel += self.gravity


class Mushroom(Powerup):
    """Powerup that makes Mario become bigger"""
    def __init__(self, x, y, name='mushroom'):
        super(Mushroom, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)


    def setup_frames(self):
        """Sets up frame list"""
        self.frames.append(self.get_image(0, 0, 16, 16))


    def handle_state(self):
        """Handles behavior based on state"""
        if self.state == c.REVEAL:
            self.revealing()
        elif self.state == c.SLIDE:
            self.sliding()
        elif self.state == c.FALL:
            self.falling()


class LifeMushroom(Mushroom):
    """1up mushroom"""
    def __init__(self, x, y, name='1up_mushroom'):
        super(LifeMushroom, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)

    def setup_frames(self):
        self.frames.append(self.get_image(16, 0, 16, 16))


class FireFlower(Powerup):
    """Powerup that allows Mario to throw fire balls"""
    def __init__(self, x, y, name=c.FIREFLOWER):
        super(FireFlower, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)


    def setup_frames(self):
        """Sets up frame list"""
        self.frames.append(
            self.get_image(0, 32, 16, 16))
        self.frames.append(
            self.get_image(16, 32, 16, 16))
        self.frames.append(
            self.get_image(32, 32, 16, 16))
        self.frames.append(
            self.get_image(48, 32, 16, 16))


    def handle_state(self):
        """Handle behavior based on state"""
        if self.state == c.REVEAL:
            self.revealing()
        elif self.state == c.RESTING:
            self.resting()


    def revealing(self):
        """Animation of flower coming out of box"""
        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.state = c.RESTING

        self.animation()


    def resting(self):
        """Fire Flower staying still on opened box"""
        self.animation()


    def animation(self):
        """Method to make the Fire Flower blink"""
        if (self.current_time - self.animate_timer) > 30:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 0

            self.image = self.frames[self.frame_index]
            self.animate_timer = self.current_time


class Star(Powerup):
    """A powerup that gives mario invincibility
    一个让马里奥无敌的升级
    继承自 Powerup 类"""
    def __init__(self, x, y, name='star'):
        super(Star, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)
        self.animate_timer = 0
        self.rect.y += 1  #looks more centered offset one pixel
        self.gravity = .4


    def setup_frames(self):
        """Creating the self.frames list where the images for the animation
        are stored"""
        self.frames.append(self.get_image(1, 48, 15, 16))
        self.frames.append(self.get_image(17, 48, 15, 16))
        self.frames.append(self.get_image(33, 48, 15, 16))
        self.frames.append(self.get_image(49, 48, 15, 16))


    def handle_state(self):
        """Handles behavior based on state"""
        if self.state == c.REVEAL:
            self.revealing()
        elif self.state == c.BOUNCE:
            self.bouncing()


    def revealing(self):
        """When the star comes out of the box"""
        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.start_bounce(-2)
            self.state = c.BOUNCE

        self.animation()


    def animation(self):
        """sets image for animation"""
        if (self.current_time - self.animate_timer) > 30:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 0
            self.animate_timer = self.current_time
            self.image = self.frames[self.frame_index]


    def start_bounce(self, vel):
        """Transitions into bouncing state"""
        self.y_vel = vel


    def bouncing(self):
        """Action when the star is bouncing around"""
        self.animation()

        if self.direction == c.LEFT:
            self.x_vel = -5
        else:
            self.x_vel = 5



class FireBall(pg.sprite.Sprite):
    """Shot from Fire Mario"""
    def __init__(self, x, y, facing_right, name=c.FIREBALL):
        super(FireBall, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.setup_frames()
        if facing_right:
            self.direction = c.RIGHT
            self.x_vel = 12
        else:
            self.direction = c.LEFT
            self.x_vel = -12
        self.y_vel = 10
        self.gravity = .9
        self.frame_index = 0
        self.animation_timer = 0
        self.state = c.FLYING
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.y = y
        self.name = name


    def setup_frames(self):
        """Sets up animation frames"""
        self.frames = []

        self.frames.append(
            self.get_image(96, 144, 8, 8)) #Frame 1 of flying
        self.frames.append(
            self.get_image(104, 144, 8, 8))  #Frame 2 of Flying
        self.frames.append(
            self.get_image(96, 152, 8, 8))   #Frame 3 of Flying
        self.frames.append(
            self.get_image(104, 152, 8, 8))  #Frame 4 of flying
        self.frames.append(
            self.get_image(112, 144, 16, 16))   #frame 1 of exploding
        self.frames.append(
            self.get_image(112, 160, 16, 16))  #frame 2 of exploding
        self.frames.append(
            self.get_image(112, 176, 16, 16))  #frame 3 of exploding


    def get_image(self, x, y, width, height):
        """Get the image frames from the sprite sheet"""

        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)


        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image


    def update(self, game_info, viewport):
        """Updates fireball behavior"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state()
        self.check_if_off_screen(viewport)


    def handle_state(self):
        """Handles behavior based on state"""
        if self.state == c.FLYING:
            self.animation()
        elif self.state == c.BOUNCING:
            self.animation()
        elif self.state == c.EXPLODING:
            self.animation()


    def animation(self):
        """adjusts frame for animation"""
        if self.state == c.FLYING or self.state == c.BOUNCING:
            if (self.current_time - self.animation_timer) > 200:
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 0
                self.animation_timer = self.current_time
                self.image = self.frames[self.frame_index]


        elif self.state == c.EXPLODING:
            if (self.current_time - self.animation_timer) > 50:
                if self.frame_index < 6:
                    self.frame_index += 1
                    self.image = self.frames[self.frame_index]
                    self.animation_timer = self.current_time
                else:
                    self.kill()


    def explode_transition(self):
        """Transitions fireball to EXPLODING state"""
        self.frame_index = 4
        centerx = self.rect.centerx
        self.image = self.frames[self.frame_index]
        self.rect.centerx = centerx
        self.state = c.EXPLODING


    def check_if_off_screen(self, viewport):
        """Removes from sprite group if off screen"""
        if (self.rect.x > viewport.right) or (self.rect.y > viewport.bottom) \
            or (self.rect.right < viewport.x):
            self.kill()










