__author__ = 'justinarmstrong'

import pygame as pg
from .. import setup
from .. import constants as c
from . import flashing_coin


class Character(pg.sprite.Sprite):
    """Parent class for all characters used for the overhead level info
    所有用于顶部等级信息的字符的父类"""

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

        self.create_image_dict()
        self.create_score_group()
        self.create_info_labels()
        self.create_load_screen_labels()
        self.create_countdown_clock()
        self.create_coin_counter()
        self.create_flashing_coin()
        self.create_mario_image()
        self.create_game_over_label()
        self.create_time_out_label()
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
        # 调用self.create_label方法获取‘000000’的美术字图集
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
        #定义金币收集数量的图片列表
        self.coin_count_images = []
        # 调用self.create_label方法获取金币数的美术字图集
        self.create_label(self.coin_count_images, '*00', 300, 55)

    def create_flashing_coin(self):
        """Creates the flashing coin next to the coin total
        在硬币总数旁边创建闪烁的硬币"""
        #调用flashing_coin.Coin方法来实例化一个self.flashing_coin
        self.flashing_coin = flashing_coin.Coin(280, 53)

    def create_mario_image(self):
        """Get the mario image"""
        self.life_times_image = self.get_image(75, 247, 6, 6)
        self.life_times_rect = self.life_times_image.get_rect(center=(378, 295))
        self.life_total_label = []
        self.create_label(self.life_total_label, str(self.total_lives),
                          450, 285)

        self.sprite_sheet = setup.GFX['mario_bros']
        self.mario_image = self.get_image(178, 32, 12, 16)
        self.mario_rect = self.mario_image.get_rect(center=(320, 290))

    def create_game_over_label(self):
        """Create the label for the GAME OVER screen"""
        game_label = []
        over_label = []

        self.create_label(game_label, 'GAME', 280, 300)
        self.create_label(over_label, 'OVER', 400, 300)

        self.game_over_label = [game_label, over_label]

    def create_time_out_label(self):
        """Create the label for the time out screen"""
        time_out_label = []

        self.create_label(time_out_label, 'TIME OUT', 290, 310)
        self.time_out_label = [time_out_label]

    def create_main_menu_labels(self):
        """Create labels for the MAIN MENU screen"""
        player_one_game = []
        player_two_game = []
        top = []
        top_score = []

        self.create_label(player_one_game, '1 PLAYER GAME', 272, 360)
        self.create_label(player_two_game, '2 PLAYER GAME', 272, 405)
        self.create_label(top, 'TOP - ', 290, 465)
        self.create_label(top_score, '000000', 400, 465)

        self.main_menu_labels = [player_one_game, player_two_game,
                                 top, top_score]

    def update(self, level_info, mario=None):
        """Updates all overhead info"""
        self.mario = mario
        self.handle_level_state(level_info)

    def handle_level_state(self, level_info):
        """Updates info based on what state the game is in"""
        if self.state == c.MAIN_MENU:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_score_images(self.main_menu_labels[3], self.top_score)
            self.update_coin_total(level_info)
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

        elif self.state == c.LOAD_SCREEN:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)

        elif self.state == c.LEVEL:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            if level_info[c.LEVEL_STATE] != c.FROZEN \
                    and self.mario.state != c.WALKING_TO_CASTLE \
                    and self.mario.state != c.END_OF_LEVEL_FALL \
                    and not self.mario.dead:
                self.update_count_down_clock(level_info)
            self.update_coin_total(level_info)
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

        elif self.state == c.TIME_OUT:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)

        elif self.state == c.GAME_OVER:
            self.score = level_info[c.SCORE]
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)

        elif self.state == c.FAST_COUNT_DOWN:
            level_info[c.SCORE] += 50
            self.score = level_info[c.SCORE]
            self.update_count_down_clock(level_info)
            self.update_score_images(self.score_images, self.score)
            self.update_coin_total(level_info)
            self.flashing_coin.update(level_info[c.CURRENT_TIME])
            if self.time == 0:
                self.state = c.END_OF_LEVEL

        elif self.state == c.END_OF_LEVEL:
            self.flashing_coin.update(level_info[c.CURRENT_TIME])

    def update_score_images(self, images, score):
        """Updates what numbers are to be blitted for the score"""
        index = len(images) - 1

        for digit in reversed(str(score)):
            rect = images[index].rect
            images[index] = Character(self.image_dict[digit])
            images[index].rect = rect
            index -= 1

    def update_count_down_clock(self, level_info):
        """Updates current time"""
        if self.state == c.FAST_COUNT_DOWN:
            self.time -= 1

        elif (level_info[c.CURRENT_TIME] - self.current_time) > 400:
            self.current_time = level_info[c.CURRENT_TIME]
            self.time -= 1
        self.count_down_images = []
        self.create_label(self.count_down_images, str(self.time), 645, 55)
        if len(self.count_down_images) < 2:
            for i in range(2):
                self.count_down_images.insert(0, Character(self.image_dict['0']))
            self.set_label_rects(self.count_down_images, 645, 55)
        elif len(self.count_down_images) < 3:
            self.count_down_images.insert(0, Character(self.image_dict['0']))
            self.set_label_rects(self.count_down_images, 645, 55)

    def update_coin_total(self, level_info):
        """Updates the coin total and adjusts label accordingly"""
        self.coin_total = level_info[c.COIN_TOTAL]

        coin_string = str(self.coin_total)
        if len(coin_string) < 2:
            coin_string = '*0' + coin_string
        elif len(coin_string) > 2:
            coin_string = '*00'
        else:
            coin_string = '*' + coin_string

        x = self.coin_count_images[0].rect.x
        y = self.coin_count_images[0].rect.y

        self.coin_count_images = []

        self.create_label(self.coin_count_images, coin_string, x, y)

    def draw(self, surface):
        """Draws overhead info based on state"""
        if self.state == c.MAIN_MENU:
            self.draw_main_menu_info(surface)
        elif self.state == c.LOAD_SCREEN:
            self.draw_loading_screen_info(surface)
        elif self.state == c.LEVEL:
            self.draw_level_screen_info(surface)
        elif self.state == c.GAME_OVER:
            self.draw_game_over_screen_info(surface)
        elif self.state == c.FAST_COUNT_DOWN:
            self.draw_level_screen_info(surface)
        elif self.state == c.END_OF_LEVEL:
            self.draw_level_screen_info(surface)
        elif self.state == c.TIME_OUT:
            self.draw_time_out_screen_info(surface)
        else:
            pass

    def draw_main_menu_info(self, surface):
        """Draws info for main menu"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for label in self.main_menu_labels:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)

    def draw_loading_screen_info(self, surface):
        """Draws info for loading screen"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.center_labels:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for word in self.life_total_label:
            surface.blit(word.image, word.rect)

        surface.blit(self.mario_image, self.mario_rect)
        surface.blit(self.life_times_image, self.life_times_rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)

    def draw_level_screen_info(self, surface):
        """Draws info during regular game play"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for digit in self.count_down_images:
            surface.blit(digit.image, digit.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)

    def draw_game_over_screen_info(self, surface):
        """Draws info when game over"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.game_over_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)

    def draw_time_out_screen_info(self, surface):
        """Draws info when on the time out screen"""
        for info in self.score_images:
            surface.blit(info.image, info.rect)

        for word in self.time_out_label:
            for letter in word:
                surface.blit(letter.image, letter.rect)

        for character in self.coin_count_images:
            surface.blit(character.image, character.rect)

        for label in self.label_list:
            for letter in label:
                surface.blit(letter.image, letter.rect)

        surface.blit(self.flashing_coin.image, self.flashing_coin.rect)
