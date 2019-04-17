__author__ = 'dominic'

import pygame as pg
from .. import setup, tools
from .. import constants as c
from .. components import info, mario


class Menu(tools._State): #继承自tool._State类
    def __init__(self):
        """Initializes the state
        初始化属性"""
        tools._State.__init__(self)
        persist = {c.COIN_TOTAL: 0, #金币数量 : 0
                   c.SCORE: 0, #分数 : 0
                   c.LIVES: 3, #声明 : 3
                   c.TOP_SCORE: 0, #最高分 : 0
                   c.CURRENT_TIME: 0.0, #当前时间 : 0.0
                   c.LEVEL_STATE: None, #等级属性:None
                   c.CAMERA_START_X: 0, #摄像机的x:0
                   c.MARIO_DEAD: False} #MARIO_DEAD :False

        self.startup(0.0, persist)

    def startup(self, current_time, persist):
        """Called every time the game's state becomes this one.  Initializes certain values.
        游戏状态每次变成这个时调用，初始化一些值"""
        #self.next = 'loading screen'
        self.next = c.LOAD_SCREEN
        #self.presist = 传入的参数presist
        self.persist = persist
        #self.game_info = 传入的参数presist
        self.game_info = persist
        #self.overhead_info = info.OverheadInfo 并传入persist和'main menu'
        self.overhead_info = info.OverheadInfo(self.game_info, c.MAIN_MENU)
        #self.sprite_sheet = 素材序列图集中的title_screen键指向的值（即：title_screen.png）
        self.sprite_sheet = setup.GFX['title_screen']
        #调用setup_backgroud方法
        self.setup_background()
        #调用setup_mario方法
        self.setup_mario()
        #调用setup_cursor方法
        self.setup_cursor()


    def setup_cursor(self):
        """Creates the mushroom cursor to select 1 or 2 player game
        创建一个蘑菇光标来选择1个或者2个玩家"""
        #用pygame.sprite.Sprite类实例化一个cursor对象
        self.cursor = pg.sprite.Sprite()
        #位置dest为（220,358）
        dest = (220, 358)
        #将参数传给self.get_image方法，创建一个image对象，使在当前区域的（0,0）点上，显示取item_objects.png中的坐标为（24,166）宽高为（8，8）范围的图片切片（即：选择光标小蘑菇）的图片
        #将返回image对象和image对象区域的信息(220,358,8*3,8*3)分别赋值给self.cursor.image 和 self.cursor.rect
        #将返回的值传递给self.cursor.image和self.cursor.rect
        self.cursor.image, self.cursor.rect = self.get_image(
            24, 160, 8, 8, dest, setup.GFX['item_objects'])
        #将c.PLAYER1的值（即：'1 player'）赋值给self.cursor.state
        self.cursor.state = c.PLAYER1


    def setup_mario(self):
        """Places Mario at the beginning of the level
        在刚开始时马里奥的位置"""
        #用mario.Mario类实例化一个mario对象
        self.mario = mario.Mario()
        #马里奥的初始坐标的x为110
        self.mario.rect.x = 110
        #马里奥的区域的底部 = c.GROUND_HEIGHT(即：SCREEN_HEIGHT - 62，即：600-62 = 538 )
        self.mario.rect.bottom = c.GROUND_HEIGHT


    def setup_background(self):
        """Setup the background image to blit
        设置背景图片显示"""
        #self.backgropud = 图集字典中‘level_1’键指向的值（即：level_1.png）
        self.background = setup.GFX['level_1']
        #获取background的矩形区域（x，y，宽，高）
        self.background_rect = self.background.get_rect()
        #将background缩放c.BACKGROUND_MULTIPLER倍（即：2.679倍），并取整。。。为什么倍数有零有整。。。
        self.background = pg.transform.scale(self.background,
                                   (int(self.background_rect.width*c.BACKGROUND_MULTIPLER),
                                    int(self.background_rect.height*c.BACKGROUND_MULTIPLER)))
        #获取背景视窗的矩形区域（x,y,宽,高），且限定视窗是以窗体底部对齐的
        self.viewport = setup.SCREEN.get_rect(bottom=setup.SCREEN_RECT.bottom)
        #定义字典image_dict
        self.image_dict = {}
        #image_dict字典中'GAME_NAME_BOX'键指向的值，是调用self.get_image方法，并传入参数，得到的结果
        #即：创建一个image对象，使在当前区域的（0,0）点上，显示取title_screen.png中的坐标为（0,0）宽高为（176，88）范围的图片切片（即：super mario bros.的标题）的图片
        #将返回image对象和image对象区域的信息（170,100,176*2.5,100*2.5）赋值给 image_dict字典中的‘GAME_NAME_BOX’键
        self.image_dict['GAME_NAME_BOX'] = self.get_image(
            1, 60, 176, 88, (170, 100), setup.GFX['title_screen'])



    def get_image(self, x, y, width, height, dest, sprite_sheet):
        """Returns images and rects to blit onto the screen
        返回图片序列并且将矩形区域切割显示在屏幕上"""
        #用pyagme.Surface类实例化一个宽高为（width，height）的image对象
        image = pg.Surface([width, height])
        #recr = image对象的矩形区域
        rect = image.get_rect()
        #将所传图片参数中的坐标为（x,y）宽高为（width，height）范围的图片切片显示在当前区域的（0,0）点上
        image.blit(sprite_sheet, (0, 0), (x, y, width, height))
        #判断所传参数中的图片是否是图集字典中'title_screen'键指向的值（即：title_screen,png）上
        if sprite_sheet == setup.GFX['title_screen']:
            #设置图片中rgb为（255，0，255）的颜色现实的时候为透明
            image.set_colorkey((255, 0, 220))
            #将image的显示范围缩放至原大小的c.SIZE_MULTIPLIER倍大（即：2.5倍），并取整
            image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        else:   #否则
            #设置图片中黑色区域为透明
            image.set_colorkey(c.BLACK)
            #将image的显示范围缩放至原大小的三倍，并取整
            image = pg.transform.scale(image,
                                   (int(rect.width*3),
                                    int(rect.height*3)))
        #获取image区域（x，y，宽，高）
        rect = image.get_rect()
        #设置image区域的x坐标为dest的第一个值
        rect.x = dest[0]
        # 设置image区域的y坐标为dest的第一个值
        rect.y = dest[1]
        #返回image对象和rect的结果（即：image对象的（x，y，宽，高））
        return (image, rect)


    def update(self, surface, keys, current_time):
        """Updates the state every refresh
        每次刷新时更新状态"""
        #接收当前时间
        self.current_time = current_time

        self.game_info[c.CURRENT_TIME] = self.current_time
        self.update_cursor(keys)
        self.overhead_info.update(self.game_info)

        surface.blit(self.background, self.viewport, self.viewport)
        surface.blit(self.image_dict['GAME_NAME_BOX'][0],
                     self.image_dict['GAME_NAME_BOX'][1])
        surface.blit(self.mario.image, self.mario.rect)
        surface.blit(self.cursor.image, self.cursor.rect)
        self.overhead_info.draw(surface)


    def update_cursor(self, keys):
        """Update the position of the cursor"""
        input_list = [pg.K_RETURN, pg.K_a, pg.K_s]

        if self.cursor.state == c.PLAYER1:
            self.cursor.rect.y = 358
            if keys[pg.K_DOWN]:
                self.cursor.state = c.PLAYER2
            for input in input_list:
                if keys[input]:
                    self.reset_game_info()
                    self.done = True
        elif self.cursor.state == c.PLAYER2:
            self.cursor.rect.y = 403
            if keys[pg.K_UP]:
                self.cursor.state = c.PLAYER1


    def reset_game_info(self):
        """Resets the game info in case of a Game Over and restart"""
        self.game_info[c.COIN_TOTAL] = 0
        self.game_info[c.SCORE] = 0
        self.game_info[c.LIVES] = 3
        self.game_info[c.CURRENT_TIME] = 0.0
        self.game_info[c.LEVEL_STATE] = None

        self.persist = self.game_info
















