__author__ = 'dominic'

import pygame as pg
from .. import setup
from .. import constants as c
from . import powerups
from . import coin


class Brick(pg.sprite.Sprite):
    """Bricks that can be destroyed
    可被摧毁的砖块
    继承自pygame.sprite.Sprite类"""

    def __init__(self, x, y, contents=None, powerup_group=None, name='brick'):
        """Initialize the object
        初始化对象
        默认金币和能量都是 None"""
        pg.sprite.Sprite.__init__(self)
        # self.sprite_sheet指向图片列表setup.GFX中'tile_set'键的值（即：tile_set.png）
        self.sprite_sheet = setup.GFX['tile_set']

        # 建立帧列表，和帧索引
        self.frames = []
        self.frame_index = 0
        # 调用self.setup_frames()方法,将图片信息添加到帧列表self.frames中
        self.setup_frames()
        # self.image指向帧字典self.frames中帧索引self.frame_index的值
        self.image = self.frames[self.frame_index]
        # 获取帧图片self.image的坐标和宽高信息，并赋值给self.rect
        self.rect = self.image.get_rect()

        # 获取self.rect的坐标值
        self.rect.x = x
        self.rect.y = y

        # 从self.image中返回一个遮罩对象
        self.mask = pg.mask.from_surface(self.image)
        #
        self.bumped_up = False
        # 把y值赋给self.rest_height
        self.rest_height = y
        # 当前场景为'resting'
        self.state = c.RESTING
        # 定义变量
        self.y_vel = 0
        self.gravity = 1.2
        self.name = name
        self.contents = contents
        self.setup_contents()
        self.group = powerup_group
        self.powerup_in_box = True

    def get_image(self, x, y, width, height):
        """Extracts the image from the sprite sheet
        从动画列表中提取图片"""
        # 用宽高参数实例化一个不到透明通道的图片
        image = pg.Surface([width, height]).convert()
        # 获取该图片的位置
        rect = image.get_rect()

        # 根据坐标和宽高在tile_set.png上获取图片，并在坐标位置绘制出来
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # 图片中RGB为 (0, 0, 0)的部分设置成透明的
        image.set_colorkey(c.BLACK)
        # 缩放图片的宽高为原来的c.BRICK_SIZE_MULTIPLIER倍，即2.69倍，并传给image
        image = pg.transform.scale(image,
                                   (int(rect.width * c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height * c.BRICK_SIZE_MULTIPLIER)))
        # 返回image值
        return image

    def setup_frames(self):
        """Set the frames to a list
        将所有的帧放进一个列表"""
        # 调用self.get_image方法并传入坐标和宽高信息，来的到两个图片，并添加到帧列表
        self.frames.append(self.get_image(16, 0, 16, 16))
        self.frames.append(self.get_image(432, 0, 16, 16))

    def setup_contents(self):
        """Put 6 coins in contents if needed
        如果需要的话放6个金币进去"""
        # 判断self.contents 是否是'6coins'
        if self.contents == '6coins':
            # self.coin_total属性 = 6
            self.coin_total = 6
        else:
            # self.coin_total属性 = 0
            self.coin_total = 0

    def update(self):
        """Updates the brick
        更新砖块状态"""
        # 调用self.handle_states方法
        self.handle_states()

    def handle_states(self):
        """Determines brick behavior based on state
        根据状态来确定砖块的行为"""
        # 判断当前状态是否为'resting'
        if self.state == c.RESTING:
            # 调用self.resting方法
            self.resting()
        elif self.state == c.BUMPED:
            self.bumped()
        elif self.state == c.OPENED:
            self.opened()

    def resting(self):
        """State when not moving
        当不移动时候的状态"""
        # 判断self.contents是否是'6coins'
        if self.contents == '6coins':
            # 判断if self.coin_total 是否是 0
            if self.coin_total == 0:
                # 当前状态为'opened'
                self.state = c.OPENED

    def bumped(self):
        """Action during a BUMPED state
        在碰撞状态中的操作"""
        # 对象的y轴位置 + 运动速度的结果，重新赋值给对象的y轴坐标
        self.rect.y += self.y_vel
        # 对象的运动速度 + 重力值（1.2）的结果，重新赋值给运动速度（即：形成加速度）
        self.y_vel += self.gravity

        # 判断对象的y轴坐标是否大于self.rest_height+5
        if self.rect.y >= (self.rest_height + 5):
            # 将self.rest_height赋值给对象的y轴坐标
            self.rect.y = self.rest_height
            # 判断对象的内容self.contents是否是'star'（即：砖块里是否隐藏着星星）
            if self.contents == 'star':
                # 当前状态变成'opened'
                self.state = c.OPENED
            # 判断对象的内容self.contents是否是'6coins'（即：砖块里是否隐藏着6个金币）
            elif self.contents == '6coins':
                # 判断金币数self.coin_total是否为 0
                if self.coin_total == 0:
                    # 当前状态变成'opened'
                    self.state = c.OPENED
                # 否则
                else:
                    # 当前状态为'resting'
                    self.state = c.RESTING
            # 否则
            else:
                # 当前状态为'resting'
                self.state = c.RESTING

    def start_bump(self, score_group):
        """Transitions brick into BUMPED state
        转换砖块进入碰撞状态"""
        # 设置速度为 -6
        self.y_vel = -6

        # 判断对象的内容self.contents是否为'6coins'
        if self.contents == '6coins':
            # 播放声音合集字典里'coin'键指向的值（即：coin.ogg）
            setup.SFX['coin'].play()

            # 判断金币数self.coin_total 是否大于0
            if self.coin_total > 0:
                # 将位置，内容，y轴坐标和分数列表传入coin.Coin，将实例化后的对象添加到self.group中
                self.group.add(coin.Coin(self.rect.centerx, self.rect.y, score_group))
                # 金币数self.coin_total -1
                self.coin_total -= 1
                # 判断金币数self.coin_total 是否为0
                if self.coin_total == 0:
                    # 帧索引 =1
                    self.frame_index = 1
                    # 将帧中这索引指向的图片赋值给self.image
                    self.image = self.frames[self.frame_index]
        # 判断内容self.contents 是否是'star'（即：砖头里是否是星星）
        elif self.contents == 'star':
            # 播放音乐合集中'powerup_appears'指向的值（即：powerup_appears.ogg）
            setup.SFX['powerup_appears'].play()
            # 帧索引 = 1
            self.frame_index = 1
            # 将帧中这索引指向的图片赋值给self.image
            self.image = self.frames[self.frame_index]

        # 当前状态变成c.BUMPED 即：'bumped'
        self.state = c.BUMPED

    def opened(self):
        """Action during OPENED state
        opened状态下的行为"""
        # 帧索引 = 1
        self.frame_index = 1
        # 将帧中这索引指向的图片赋值给self.image
        self.image = self.frames[self.frame_index]

        # 判断内容self.contents是否为'star' 并且self.powerup_in_box是否为 True
        if self.contents == 'star' and self.powerup_in_box:
            # 将参数（中心位置的x坐标和self.rect_height）传入powerups.Star类，并将实例化的对象添加到self.group中
            self.group.add(powerups.Star(self.rect.centerx, self.rest_height))
            # self.powerup_in_box 变成 False
            self.powerup_in_box = False


class BrickPiece(pg.sprite.Sprite):
    """Pieces that appear when bricks are broken"""

    def __init__(self, x, y, xvel, yvel):
        super(BrickPiece, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_vel = xvel
        self.y_vel = yvel
        self.gravity = .8

    def setup_frames(self):
        """create the frame list"""
        self.frames = []

        image = self.get_image(68, 20, 8, 8)
        reversed_image = pg.transform.flip(image, True, False)

        self.frames.append(image)
        self.frames.append(reversed_image)

    def get_image(self, x, y, width, height):
        """Extract image from sprite sheet"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width * c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height * c.BRICK_SIZE_MULTIPLIER)))
        return image

    def update(self):
        """Update brick piece"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.y_vel += self.gravity
        self.check_if_off_screen()

    def check_if_off_screen(self):
        """Remove from sprite groups if off screen"""
        if self.rect.y > c.SCREEN_HEIGHT:
            self.kill()
