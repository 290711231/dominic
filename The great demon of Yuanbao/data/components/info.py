__author__ = 'dominic'

import pygame as pg
from .. import setup
from .. import constants as c
from . import flashing_coin


class Character(pg.sprite.Sprite):
    """Parent class for all characters used for the overhead level info
    所有用于开销等级信息的字符的父类"""

    def __init__(self, image):
        super(Character, self).__init__()
        # 将传入的图片信息image传给self.image
        self.image = image
        # 获取图片的信息（x，y，宽，高）并赋值给self.rect
        self.rect = self.image.get_rect()


class OverheadInfo(object):
    """Class for level information like score, coin total,and time remaining
        类获取级别信息，如分数、硬币总数和剩余时间"""

    def __init__(self, game_info, state):
        # self.sprite_sheet = setup.GFX动画字典图集中的text_images.png
        self.sprite_sheet = setup.GFX['text_images']
        # self.coin_total = game_info字典中'coin total'的值
        self.coin_total = game_info[c.COIN_TOTAL]
        self.time = 401
        self.current_time = 0
        # self.coin_total = game_info字典中'lives'的值
        self.total_lives = game_info[c.LIVES]
        # self.coin_total = game_info字典中'top score'的值
        self.top_score = game_info[c.TOP_SCORE]
        self.state = state
        self.special_state = None
        self.game_info = game_info

        # 调用self.create_image_dict()方法创建数字和文字的图集字典
        self.create_image_dict()
        # 调用self.create_score_group()方法创建初始化分数
        self.create_score_group()
        # 调用self.create_info_labels()方法创建屏幕上方的文字信息
        self.create_info_labels()
        # 调用self.create_load_screen_labels()方法创建关卡开始时屏幕中心的关卡信息
        self.create_load_screen_labels()
        # 调用self.create_countdown_clock()方法创建一个倒计时时钟
        self.create_countdown_clock()
        # 调用self.create_coin_counter()方法创建屏幕上方收集金币的信息（*00）
        self.create_coin_counter()
        # 调用self.create_flashing_coin()方法创建屏幕上方金币闪烁的动画
        self.create_flashing_coin()
        # 调用self.create_mario_image()方法来创建屏幕上方的马里奥
        self.create_mario_image()
        # 调用self.create_game_over_label()方法来创建游戏结束标签
        self.create_game_over_label()
        # 调用self.create_time_out_label()方法来创建游戏超时标签
        self.create_time_out_label()
        # 调用self.create_main_menu_labels()方法来创建主菜单标签
        self.create_main_menu_labels()

    def create_image_dict(self):
        """Creates the initial images for the score
        为分数创建初始图像"""
        self.image_dict = {}
        # 生成分数图集列表
        image_list = []
        # 调用get_image方法给image_list添加元素
        image_list.append(self.get_image(3, 230, 7, 7))
        image_list.append(self.get_image(12, 230, 7, 7))
        image_list.append(self.get_image(19, 230, 7, 7))
        image_list.append(self.get_image(27, 230, 7, 7))
        image_list.append(self.get_image(35, 230, 7, 7))
        image_list.append(self.get_image(43, 230, 7, 7))
        image_list.append(self.get_image(51, 230, 7, 7))
        image_list.append(self.get_image(59, 230, 7, 7))
        image_list.append(self.get_image(67, 230, 7, 7))
        image_list.append(self.get_image(75, 230, 7, 7))

        image_list.append(self.get_image(83, 230, 7, 7))
        image_list.append(self.get_image(91, 230, 7, 7))
        image_list.append(self.get_image(99, 230, 7, 7))
        image_list.append(self.get_image(107, 230, 7, 7))
        image_list.append(self.get_image(115, 230, 7, 7))
        image_list.append(self.get_image(123, 230, 7, 7))
        image_list.append(self.get_image(3, 238, 7, 7))
        image_list.append(self.get_image(11, 238, 7, 7))
        image_list.append(self.get_image(20, 238, 7, 7))
        image_list.append(self.get_image(27, 238, 7, 7))
        image_list.append(self.get_image(35, 238, 7, 7))
        image_list.append(self.get_image(44, 238, 7, 7))
        image_list.append(self.get_image(51, 238, 7, 7))
        image_list.append(self.get_image(59, 238, 7, 7))
        image_list.append(self.get_image(67, 238, 7, 7))
        image_list.append(self.get_image(75, 238, 7, 7))
        image_list.append(self.get_image(83, 238, 7, 7))
        image_list.append(self.get_image(91, 238, 7, 7))
        image_list.append(self.get_image(99, 238, 7, 7))
        image_list.append(self.get_image(108, 238, 7, 7))
        image_list.append(self.get_image(115, 238, 7, 7))
        image_list.append(self.get_image(123, 238, 7, 7))
        image_list.append(self.get_image(3, 246, 7, 7))
        image_list.append(self.get_image(11, 246, 7, 7))
        image_list.append(self.get_image(20, 246, 7, 7))
        image_list.append(self.get_image(27, 246, 7, 7))
        image_list.append(self.get_image(48, 248, 7, 7))

        image_list.append(self.get_image(68, 249, 6, 2))
        image_list.append(self.get_image(75, 247, 6, 6))

        # 给字符串character_string赋值
        character_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ -*'

        # character遍历character_string，image遍历image_list
        for character, image in zip(character_string, image_list):
            # 将遍历的结果组成新的键值对，并添加到image_dict列表中
            self.image_dict[character] = image

    def get_image(self, x, y, width, height):
        """Extracts image from sprite sheet
        从sprite sheet中提取图像元素"""
        # image 根据宽高实例化一个surface对象
        image = pg.Surface([width, height])
        # 获取image的矩形区域
        rect = image.get_rect()
        # 把这个image中x，y坐标上裁切宽高为width，height的图片，并画在self.sprite_sheet舞台的0,0点上
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # 将image里rgb为（92,148,252）的颜色变成透明的
        image.set_colorkey((92, 148, 252))
        # 对surfacer对象变形，宽高各放大2.9倍，并重新赋值给image对象
        image = pg.transform.scale(image,
                                   (int(rect.width * 2.9),
                                    int(rect.height * 2.9)))
        # 返回image对象
        return image

    def create_score_group(self):
        """Creates the initial empty score (000000)
        创建一个初始化的分数：000000"""
        # 创造分数图片列表score_images
        self.score_images = []
        # 调用self.create_label方法获取‘000000’的美术字图集并添加到self.score_images列表中
        self.create_label(self.score_images, '000000', 75, 55)

    def create_info_labels(self):
        """Creates the labels that describe each info
        创建描述每个信息的标签"""
        # 定义每个标签的美术字图片列表
        self.mario_label = []
        self.world_label = []
        self.time_label = []
        self.stage_label = []

        # 调用self.create_label方法获取‘MARIO’的美术字图集
        self.create_label(self.mario_label, 'MARIO', 75, 30)
        # 调用self.create_label方法获取‘WORLD’的美术字图集
        self.create_label(self.world_label, 'WORLD', 450, 30)
        # 调用self.create_label方法获取‘TIME’的美术字图集
        self.create_label(self.time_label, 'TIME', 625, 30)
        # 调用self.create_label方法获取‘1-1’的美术字图集
        self.create_label(self.stage_label, '1-1', 472, 55)
        # 将'MARIO','WORLD','TIME','1-1'的美术字图集组成一个列表，并赋值给self.label_list
        self.label_list = [self.mario_label,
                           self.world_label,
                           self.time_label,
                           self.stage_label]

    def create_load_screen_labels(self):
        """Creates labels for the center info of a load screen
        为一个屏幕的中心信息创建标签"""
        world_label = []
        number_label = []
        # 调用self.create_label方法获取‘WORLD’的美术字图集
        self.create_label(world_label, 'WORLD', 280, 200)
        # 调用self.create_label方法获取‘1-1’的美术字图集
        self.create_label(number_label, '1-1', 430, 200)
        # 将'WORLD'和'1-1'的美术字图集组成一个列表，并赋值给self.center_labels
        self.center_labels = [world_label, number_label]

    def create_countdown_clock(self):
        """Creates the count down clock for the level
        给关卡创建一个倒计时时钟"""
        # 定义一个倒计时的美术字图集列表
        self.count_down_images = []
        # 调用self.create_label方法获取self.time的美术字图集(即：初始401的倒计时)
        self.create_label(self.count_down_images, str(self.time), 645, 55)

    def create_label(self, label_list, string, x, y):
        """Creates a label (WORLD, TIME, MARIO)
        创建一个标签用于显示（世界名，时间，马里奥）的信息"""
        for letter in string:  # 遍历string中的元素
            # 给Character传参：self.image_dict[letter]来实例化一个对象，并添加到图片列表self.image_dicr里
            # 即：给传入的string创造美术字的图片材质集
            label_list.append(Character(self.image_dict[letter]))
        # 调用self.set_label_rects方法并传入参数（label_list，x，y）
        self.set_label_rects(label_list, x, y)

    def set_label_rects(self, label_list, x, y):
        """Set the location of each individual character
        设置每个单独的字符的位置"""
        # 用enumerate将label_list中的元素和他的索引数组成一个新的元素及[(索引数，元素)，（索引数，元素），...]
        # 遍历label_list并将索引值赋给i，将元素赋值给letter
        for i, letter in enumerate(label_list):
            # letter的x值为： x+ （(宽+3)*索引值）
            letter.rect.x = x + ((letter.rect.width + 3) * i)
            # letter的y值为： y
            letter.rect.y = y
            # 判断letter的图片是不是字符‘-’对应的图片
            if letter.image == self.image_dict['-']:
                # letter元素的y = y+7
                letter.rect.y += 7
                # letter元素的x = x+2
                letter.rect.x += 2

    def create_coin_counter(self):
        """Creates the info that tracks the number of coins Mario collects
        创建一个追踪马里奥收集金币数量的信息"""
        # 定义金币收集数量的图片列表
        self.coin_count_images = []
        # 调用self.create_label方法获取金币数的美术字图集
        self.create_label(self.coin_count_images, '*00', 300, 55)

    def create_flashing_coin(self):
        """Creates the flashing coin next to the coin total
        在硬币总数旁边创建闪烁的硬币"""
        # 调用flashing_coin.Coin方法来实例化一个self.flashing_coin
        self.flashing_coin = flashing_coin.Coin(280, 53)

    def create_mario_image(self):
        """Get the mario image
        获取马里奥的图片"""
        # 传参数给self.get_image方法来实例化一个生命数的图片
        self.life_times_image = self.get_image(75, 247, 6, 6)
        # 获取life_times_image的矩形绘制范围，且中心坐标为（378,295）
        self.life_times_rect = self.life_times_image.get_rect(center=(378, 295))
        # 创建屏幕上方的生命值标签列表
        self.life_total_label = []
        # 遍历self.total_lives（即：字典geme_info中‘LIVE’键对应的值）中的字符，并赋予坐标（450,285）
        self.create_label(self.life_total_label, str(self.total_lives),
                          450, 285)

        # self.sprite_sheet = 图片集字典中的‘mario_bros’键对应的值（即：mario_bros.png）
        self.sprite_sheet = setup.GFX['mario_bros']
        # self.mario_image = 裁取mario_bros.png中坐标为（178,32）宽高为（12,16）的部分（即：站立的马里奥）
        self.mario_image = self.get_image(178, 32, 12, 16)
        # 获取self.mario_image的矩形绘制范围，且中心坐标为（320,290）
        self.mario_rect = self.mario_image.get_rect(center=(320, 290))

    def create_game_over_label(self):
        """Create the label for the GAME OVER screen
        为 GAME OVER 在屏幕上创建标签"""
        # 定义 geme 和over 的列表
        game_label = []
        over_label = []

        # 遍历 GAME 和 OVER 的字符，添加到列表中，并分别赋予坐标（280,300）和（400,300）
        self.create_label(game_label, 'GAME', 280, 300)
        self.create_label(over_label, 'OVER', 400, 300)

        # 用 game 和 over 的列表创建一个列表self.game_over_label
        self.game_over_label = [game_label, over_label]

    def create_time_out_label(self):
        """Create the label for the time out screen
        为游戏超时创建一个列表"""
        # 定义time_out_label列表
        time_out_label = []

        # 遍历‘TIME OUT’中的字符，添加到time_out_label列表中，并赋予坐标（290,310）
        self.create_label(time_out_label, 'TIME OUT', 290, 310)
        # 用列表time_out_label创建一个新列表self.time_out_label
        self.time_out_label = [time_out_label]

    def create_main_menu_labels(self):
        """Create labels for the MAIN MENU screen
        为主菜单创建标签"""
        # 定义主菜单需要的列表
        player_one_game = []
        player_two_game = []
        top = []
        top_score = []

        # 遍历‘1 PLAYER GAME’中的字符，添加到player_one_game列表中，并赋予坐标（272,360）
        self.create_label(player_one_game, '1 PLAYER GAME', 272, 360)
        # 遍历‘2 PLAYER GAME’中的字符，添加到player_two_game列表中，并赋予坐标（272,405）
        self.create_label(player_two_game, '2 PLAYER GAME', 272, 405)
        # 遍历‘TOP - ’中的字符，添加到top列表中，并赋予坐标（290,465）
        self.create_label(top, 'TOP - ', 290, 465)
        # 遍历‘000000’中的字符，添加到top_score列表中，并赋予坐标（400,465）
        self.create_label(top_score, '000000', 400, 465)

        # 用player_one_game,player_two_geme,top和top_score创建一个新的列表self.main_menu_labels
        self.main_menu_labels = [player_one_game, player_two_game,
                                 top, top_score]

    def update(self, level_info, mario=None):
        """Updates all overhead info
        更新全部系统开销信息？"""
        self.mario = mario
        # 调用self.handle_level_state方法
        self.handle_level_state(level_info)

    def handle_level_state(self, level_info):
        """Updates info based on what state the game is in
        根据游戏的状况更新信息"""
        if self.state == c.MAIN_MENU:  # 判断self.state是否为'main menu'
            # self.score = 等级信息字典level_info中的'score'键指向的值
            self.score = level_info[c.SCORE]
            # 调用self.update_score_images方法来更新self.score的分数信息
            self.update_score_images(self.score_images, self.score)
            # 调用self.update_score_images方法来更新self.main_menu_labels列表中下标为3的信息（即：top_score）
            self.update_score_images(self.main_menu_labels[3], self.top_score)
            # 调用self.update_coin_total方法更新金币数 并 相应的调整标签
            self.update_coin_total(level_info)
            # 传入level_info字典中'current time'键指向的值，调用self.flashing_coin.update方法
            # 创造闪烁的金币的动画
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

        elif self.state == c.LOAD_SCREEN:  # 判断self.state是否为'load screen'
            # 将level_info字典中 'score'键指向的值赋值给self.score
            self.score = level_info[c.SCORE]
            # 调用self.update_score_images方法来更新分数的图片信息
            self.update_score_images(self.score_images, self.score)
            # 调用self.update_coin_total方法更新金币数 并 相应的调整标签
            self.update_coin_total(level_info)

        elif self.state == c.LEVEL:  # 判断self.state是否为'level'
            # 将level_info字典中 'score'键指向的值赋值给self.score
            self.score = level_info[c.SCORE]
            # 调用self.update_score_images方法来更新分数的图片信息
            self.update_score_images(self.score_images, self.score)

            # 判断level_info字典中 'level state'键指向的值是否不是'frozen'
            # 并且self.mario.state 不是 'walking to castle'
            # 并且and self.mario.state 不是 'end of level fall'
            if level_info[c.LEVEL_STATE] != c.FROZEN \
                    and self.mario.state != c.WALKING_TO_CASTLE \
                    and self.mario.state != c.END_OF_LEVEL_FALL \
                    and not self.mario.dead:
                # 调用self.update_count_down_clock方法来更新倒计时时间
                self.update_count_down_clock(level_info)

            # 调用self.update_coin_total方法更新金币数 并 相应的调整标签
            self.update_coin_total(level_info)
            # 把字典level_info中 'current time'键指向的值传入self.flashing_coin.update方法来创建一个金币闪烁动画
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

        # 判断当前场景是否是'time out'
        elif self.state == c.TIME_OUT:
            # self.score = 字典level_info中'score'键指向的值
            self.score = level_info[c.SCORE]
            # 将分数图片列表self.score_images和self.score传给方法self.update_score_images，来更新分数的图片信息
            self.update_score_images(self.score_images, self.score)
            # 调用self.update_coin_total方法更新金币数 并 相应的调整标签
            self.update_coin_total(level_info)

        # 判断当前场景是否是'game over'
        elif self.state == c.GAME_OVER:
            # self.score = 字典level_info中'score'键指向的值
            self.score = level_info[c.SCORE]
            # 将分数图片列表self.score_images和self.score传给方法self.update_score_images，来更新分数的图片信息
            self.update_score_images(self.score_images, self.score)
            # 调用self.update_coin_total方法更新金币数 并 相应的调整标签
            self.update_coin_total(level_info)

        # 判断当前场景是否是'fast count down'
        elif self.state == c.FAST_COUNT_DOWN:
            # 字典level_info中 'score'指向的值每次增加50（即：每次增加50分）
            level_info[c.SCORE] += 50
            # self.score = 字典level_info中'score'键指向的值
            self.score = level_info[c.SCORE]
            # 更新倒计时时间
            self.update_count_down_clock(level_info)
            # 将分数图片列表self.score_images和self.score传给方法self.update_score_images，来更新分数的图片信息
            self.update_score_images(self.score_images, self.score)
            # 调用self.update_coin_total方法更新金币数 并 相应的调整标签
            self.update_coin_total(level_info)
            # 把字典level_info中 'current time'键指向的值传入self.flashing_coin.update方法，来创建金币闪烁动画
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

            #判断self.tiom 是否为 0
            if self.time == 0:
                # 当前场景变成'end of level'
                self.state = c.END_OF_LEVEL


        # 判断当前场景是否是'end of level'
        elif self.state == c.END_OF_LEVEL:
            # 把字典level_info中 'current time'键指向的值传入self.flashing_coin.update方法，来创建金币闪烁动画
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

    def update_score_images(self, images, score):
        """Updates what numbers are to be blitted for the score
        更新那些将要为分数传递的数字"""
        index = len(images) - 1

        # 将分数转换成字符串，并倒序排列，在遍历以下
        for digit in reversed(str(score)):
            # 获取images图集中最后一个元素的信息
            rect = images[index].rect
            # 给Character传入参数self，image_dict字典中'digit'键所指向的值，来实例化对象images[index]
            images[index] = Character(self.image_dict[digit])
            # 将rect重新赋值给images[index]
            images[index].rect = rect
            # index递减
            index -= 1

    def update_count_down_clock(self, level_info):
        """Updates current time
        更新倒计时时间"""
        if self.state == c.FAST_COUNT_DOWN:  # 判断当前场景是否是'fast count down'（快速倒计时）
            # self,time - = 1
            self.time -= 1

        # 判断字典level_info中'current time'键指向的值减去当前时间是否大于400
        elif (level_info[c.CURRENT_TIME] - self.current_time) > 400:
            # 当前时间等于字典level_info中'current time'键指向的值
            self.current_time = level_info[c.CURRENT_TIME]
            # slef.time -= 1
            self.time -= 1

        # 初始化倒计时图片列表self.count_down_images
        self.count_down_images = []
        # 调用self.create_label方法将需要的图片信息添加到列表self.count_down_images中
        self.create_label(self.count_down_images, str(self.time), 645, 55)

        if len(self.count_down_images) < 2:  # 判断self.count_down_images是否小于2
            # 创建生成0到1的列表，并且遍历

            for i in range(2):
                # 给Character类传入字典self.image_dict中'0'键指向的值，获取图片的信息
                # 并把这个信息添加到列表self.count_down_images的第一个值
                self.count_down_images.insert(0, Character(self.image_dict['0']))

            # 将列表self.count_down_images、x值和y值传入self.set_label_rects方法
            # 来设置列表中每个数字的位置
            self.set_label_rects(self.count_down_images, 645, 55)

        elif len(self.count_down_images) < 3:  # 判断self.count_down_images的长度是否小于3

            # 给Character类传入字典self.image_dict中'0'键指向的值，获取图片的信息
            # 并把这个信息添加到列表self.count_down_images的第一个值
            self.count_down_images.insert(0, Character(self.image_dict['0']))

            # 将列表self.count_down_images、x值和y值传入self.set_label_rects方法
            # 来设置列表中每个数字的位置
            self.set_label_rects(self.count_down_images, 645, 55)

    def update_coin_total(self, level_info):
        """Updates the coin total and adjusts label accordingly
        更新金币数 并 相应的调整标签"""
        # 把level_info字典中'coin total'键对应的值赋给self.coin_total
        self.coin_total = level_info[c.COIN_TOTAL]

        # 将金币数转换成字符串，并赋给变量coin_string
        coin_string = str(self.coin_total)

        if len(coin_string) < 2:  # 判断金币数的字符串是否小于2
            # 金币数前加字符串'*0'再重新赋值给coin_string
            coin_string = '*0' + coin_string
        elif len(coin_string) > 2:  # 判断金币数的字符串是够大于2
            # 金币数等于字符串'*00'
            coin_string = '*00'
        else:
            # 金币数前加字符串'*'再重新赋值给coin_string
            coin_string = '*' + coin_string

        # 获取coin_count_images[0]位置信息的 x轴 和 y轴
        x = self.coin_count_images[0].rect.x
        y = self.coin_count_images[0].rect.y

        # 将self.coin_count_images清空
        self.coin_count_images = []

        # 调用self.create_label方法将金币数指向的图片信息添加到self.coin_count_images字典中
        self.create_label(self.coin_count_images, coin_string, x, y)

    def draw(self, surface):
        """Draws overhead info based on state
        根据当前状态绘制开销信息"""

        # 判断当前场景是否是'main menu'
        if self.state == c.MAIN_MENU:
            # 调用self.draw_main_meny_info方法来绘制main munu的信息
            self.draw_main_menu_info(surface)

        # 判断当前场景是否是'load screen'
        elif self.state == c.LOAD_SCREEN:
            # 调用self.draw_loading_screen_info方法来绘制载入屏幕的信息
            self.draw_loading_screen_info(surface)

        # 判断当前场景是否是'level'
        elif self.state == c.LEVEL:
            # 调用self.draw_level_screen_info方法在常规游戏中绘制信息
            self.draw_level_screen_info(surface)

        # 判断当前场景是否是'game over'
        elif self.state == c.GAME_OVER:
            # 调用self.draw_game_over_screen_info方法来绘制游戏结束时的信息
            self.draw_game_over_screen_info(surface)

        # 判断当前场景是否是'fast count down'
        elif self.state == c.FAST_COUNT_DOWN:
            # 调用self.draw_level_screen_info方法来绘制倒计时时的信息
            self.draw_level_screen_info(surface)

        # 判断当前场景是否是'end of level'
        elif self.state == c.END_OF_LEVEL:
            # 调用self.draw_level_screen_info方法在常规游戏中绘制信息
            self.draw_level_screen_info(surface)

        # 判断当前场景是否是'time out'
        elif self.state == c.TIME_OUT:
            # 调用self.draw_time_out_screen_info方法来绘制游戏超时时的信息
            self.draw_time_out_screen_info(surface)

        # 否则，跳过
        else:
            pass

    def draw_main_menu_info(self, surface):
        """Draws info for main menu
        绘制main munu的信息"""
        # 遍历分数图片信息列表
        for info in self.score_images:
            # 在info.rect位置绘制info.image分数图片
            surface.blit(info.image, info.rect)

        # 遍历菜单标签图片信息列表
        for label in self.main_menu_labels:
            # 遍历label列表
            for letter in label:
                # 在letter.rect位置绘制letter.iamge字符图片
                surface.blit(letter.image, letter.rect)

        # 遍历金币收集的图片信息列表
        for character in self.coin_count_images:
            # 在character.rect位置绘制character.image图片
            surface.blit(character.image, character.rect)

        # 遍历标签图片信息列表
        for label in self.label_list:
            # 遍历label列表
            for letter in label:
                # 在letter.rect位置绘制letter.image字符图片
                surface.blit(letter.image, letter.rect)

        # 在self.flashing_coin.rect位置绘制self.flashing_coin.image闪烁金币图片
        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)

    def draw_loading_screen_info(self, surface):
        """Draws info for loading screen
        绘制载入屏幕的信息"""
        # 遍历self.score_images分数图片列表
        for info in self.score_images:
            # 在info.rect位置绘制info.image分数图片
            surface.blit(info.image, info.rect)

        # 遍历self.center_labels美术字图片列表
        for word in self.center_labels:
            # 遍历每一个字符串中的每一个字符
            for letter in word:
                # 在letter.rect位置绘制letter.image图片
                surface.blit(letter.image, letter.rect)

        # 遍历self.life_total_label生命列表
        for word in self.life_total_label:
            # 在word.rect位置绘制word.image图片
            surface.blit(word.image, word.rect)

        # 在self.mario_rect位置绘制self.mario_image马里奥图片
        surface.blit(self.mario_image, self.mario_rect)
        # 在self.life_time_rect位置绘制self.life_time_image生命数图片
        surface.blit(self.life_times_image, self.life_times_rect)

        # 遍历self.coin_count_images金币收集图片列表
        for character in self.coin_count_images:
            # 在character.rect位置绘制charater.image图片
            surface.blit(character.image, character.rect)

        # 遍历self.label_list标签图片信息列表
        for label in self.label_list:
            # 遍历每个信息中的字符的图片列表
            for letter in label:
                # 在letter.rect位置绘制letter.image图片
                surface.blit(letter.image, letter.rect)

        # 在self.flashing_coin.rect位置绘制self.flashing_coin.image闪烁金币图片
        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)

    def draw_level_screen_info(self, surface):
        """Draws info during regular game play
        在常规游戏中绘制信息"""
        # 遍历分数图片信息列表self.score_images
        for info in self.score_images:
            # 在info.rect位置绘制info.image
            surface.blit(info.image, info.rect)

        # 遍历倒计时图片信息列表self.count_down_images
        for digit in self.count_down_images:
            # 在digit.rect位置绘制digit.image
            surface.blit(digit.image, digit.rect)

        # 遍历金币图片信息列表self.coin_count_images
        for character in self.coin_count_images:
            # 在character.rect位置绘制character.image
            surface.blit(character.image, character.rect)

        # 遍历标签列表图片信息列表self.label_list
        for label in self.label_list:
            # 遍历每个标签中的字符
            for letter in label:
                # 在letter.rect位置绘制letter.image
                surface.blit(letter.image, letter.rect)

        # 在self.flashing_coin.rect位置绘制self.flashing_coin.image
        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)

    def draw_game_over_screen_info(self, surface):
        """Draws info when game over
        绘制游戏结束时候的信息"""
        # 遍历分数图片信息列表self.score_images
        for info in self.score_images:
            # 在info.rect位置绘制info.image
            surface.blit(info.image, info.rect)

        # 遍历游戏结束标签图片信息列表self.game_over_label
        for word in self.game_over_label:
            # 遍历每个信息里的字符
            for letter in word:
                # 在letter.rect位置绘制letter.image
                surface.blit(letter.image, letter.rect)

        # 遍历金币图片信息列表self.coin_count_images
        for character in self.coin_count_images:
            # 在character.rect位置绘制character.image
            surface.blit(character.image, character.rect)

        # 遍历标签列表图片信息列表self.label_list
        for label in self.label_list:
            # 遍历每个列表中的字符
            for letter in label:
                # 在letter.rect位置绘制letter.image
                surface.blit(letter.image, letter.rect)

        # 在self.flashing_coin.rect位置绘制金币闪烁动画self.flashing_coin.image
        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)

    def draw_time_out_screen_info(self, surface):
        """Draws info when on the time out screen
        绘制超时是屏幕上的信息"""
        # 遍历分数图片信息列表self.score_images
        for info in self.score_images:
            # 在info.rect位置绘制info.image
            surface.blit(info.image, info.rect)

        # 遍历超时标签图片信息列表
        for word in self.time_out_label:
            # 遍历每一个列表中的字符
            for letter in word:
                # 在letter.rect位置绘制letter.image
                surface.blit(letter.image, letter.rect)

        # 遍历金币图片信息列表
        for character in self.coin_count_images:
            # 在character.rect位置绘制character.image
            surface.blit(character.image, character.rect)

        # 遍历标签图片信息列表
        for label in self.label_list:
            # 遍历每一个列表中的字符
            for letter in label:
                # 在letter.rect位置绘制letter.image
                surface.blit(letter.image, letter.rect)

        # 在self.flashing_coin.rect位置绘制金币闪烁动画self.flashing_coin.image
        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)
