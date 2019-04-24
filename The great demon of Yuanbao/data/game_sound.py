__author__ = 'dominic'

import pygame as pg
from . import setup
from . import constants as c


class Sound(object):
    """Handles all sound for the game
    为游戏处理所有的声音"""

    def __init__(self, overhead_info):
        """Initialize the class
        初始化类"""
        self.sfx_dict = setup.SFX
        self.music_dict = setup.MUSIC
        self.overhead_info = overhead_info
        self.game_info = overhead_info.game_info
        self.set_music_mixer()

    def set_music_mixer(self):
        """Sets music for level
        为等级设置声音"""
        # 判断self.overhead_info.state场景是否为'level'
        if self.overhead_info.state == c.LEVEL:
            # 载入音乐列表字典中'main_theme'键指向的值（即：main_theme.ogg）
            pg.mixer.music.load(self.music_dict['main_theme'])
            # 播放音乐
            pg.mixer.music.play()
            # self.state场景为'normal'
            self.state = c.NORMAL

        # 判断self.overhead_info.state场景是否为 'game over'
        elif self.overhead_info.state == c.GAME_OVER:
            # 载入音乐列表字典中'game_over'键指向的值（即：game_over.ogg）
            pg.mixer.music.load(self.music_dict['game_over'])
            # 播放音乐
            pg.mixer.music.play()
            # self.state场景为'game over'
            self.state = c.GAME_OVER

    def update(self, game_info, mario):
        """Updates sound object with game info
        用游戏信息更新声音对象"""
        self.game_info = game_info
        self.mario = mario
        # 调用self.handle_state()方法
        self.handle_state()

    def handle_state(self):
        """Handles the state of the sound object
        处理声音对象的状态"""
        # 判断self.state是否为 'normal'
        if self.state == c.NORMAL:
            # 判断self.mario.dead是否为 True （即，mario是不是死了）
            if self.mario.dead:
                # 将参数'death'和 'mario dead'传入self.play_music方法，来播放一个新的音乐（即：death.wav）
                # 并且self.state 变成了'mario dead'
                self.play_music('death', c.MARIO_DEAD)

            # 判断self.mario.invincible是否为 True
            # 并且self.mario.losing_invincibility是否为 False
            elif self.mario.invincible \
                    and self.mario.losing_invincibility == False:
                # 将参数'invincible'和'mario invincible'传入self.play_music方法，播放一个新的音乐（即：invincible.ogg）
                # 并且self.state 变成了'mario invincible'
                self.play_music('invincible', c.MARIO_INVINCIBLE)

            # 判断self.mario.state场景是否为'flag pole'
            elif self.mario.state == c.FLAGPOLE:
                # 将参数'flagpole'和'flag pole'传入self.play_music方法，播放一个新的音乐（即：flagpole.wav）
                # 并且self.state 变成了'flag pole'
                self.play_music('flagpole', c.FLAGPOLE)

            # 判断self.overhead_info.time 是否等于 100
            elif self.overhead_info.time == 100:
                # 将参数'out_of_time'和'time warning'传入self.play_music方法，播放一个新的音乐（即：out_of_time.wav）
                # 并且self.state 变成了'time warning'
                self.play_music('out_of_time', c.TIME_WARNING)

        # 判断self.state 是否是'flag pole'
        elif self.state == c.FLAGPOLE:
            # 判读按self.mario.state 是否是'walking to castle'
            if self.mario.state == c.WALKING_TO_CASTLE:
                # 播放音乐stage_clear.wav,并且self.state为'stage clear'
                self.play_music('stage_clear', c.STAGE_CLEAR)

        # 判断self.state是否为'stage clear'
        elif self.state == c.STAGE_CLEAR:
            # 判断self.mario.in_castle是否为'True'
            if self.mario.in_castle:
                # 播放音效字典下'count_down'键对应的音乐（即：count_down.ogg）
                self.sfx_dict['count_down'].play()
                # self.state场景变为'fast count down'
                self.state = c.FAST_COUNT_DOWN

        # 判断self.state是否为'fast count down'
        elif self.state == c.FAST_COUNT_DOWN:
            # 判断self.overhead_info.time是否为 0
            if self.overhead_info.time == 0:
                # 停止播放count_down.ogg
                self.sfx_dict['count_down'].stop()
                # 当前场景变为'world clear'
                self.state = c.WORLD_CLEAR

        # 判断self.state是否为'time warning'
        elif self.state == c.TIME_WARNING:
            # 判断是否没有音乐在播放
            if pg.mixer.music.get_busy() == 0:
                # 调用self.play_music方法播放main_theme_sped_up.ogg，并且self.state变成 'sped up normal'
                self.play_music('main_theme_sped_up', c.SPED_UP_NORMAL)
            # 判断self.mario.dead是否为True
            elif self.mario.dead:
                # 调用self.play_music方法播放death.wav,并且self.state变成 'mario dead'
                self.play_music('death', c.MARIO_DEAD)

        # 判断self.state是否为'sped up normal'
        elif self.state == c.SPED_UP_NORMAL:
            # 判断self.mario.dead是否为True
            if self.mario.dead:
                # 调用self.play_music方法播放death.wav，并且self.state变成'mario dead'
                self.play_music('death', c.MARIO_DEAD)
            # 判断self.mario.state是否为'flag pole'
            elif self.mario.state == c.FLAGPOLE:
                # 调用self.play_music方法播放flagpole.wav，并且self.state变成'flag pole'
                self.play_music('flagpole', c.FLAGPOLE)

        # 判断self.state是否是 'mario invincible'
        elif self.state == c.MARIO_INVINCIBLE:
            # 判断self.mario.current_time减去self.mario.invincible_start_timer是否为11000
            if (self.mario.current_time - self.mario.invincible_start_timer) > 11000:
                # 调用self.play_music方法播放 main_theme.ogg，并且self.state变成 'normal'
                self.play_music('main_theme', c.NORMAL)
            # 判断self.mario.dead是否为True
            elif self.mario.dead:
                # 调用self.play_music方法播放death.wav,并且self.state变成 'mario dead'
                self.play_music('death', c.MARIO_DEAD)

        # 判断self.state是否是 'world clear'
        elif self.state == c.WORLD_CLEAR:
            pass
        # 判断self.state是否是 'mario dead'
        elif self.state == c.MARIO_DEAD:
            pass
        # 判断self.state是否是 'game over'
        elif self.state == c.GAME_OVER:
            pass

    def play_music(self, key, state):
        """Plays new music
        播放一个新的音乐"""
        # 载入字典self.music_dict中参数key键指向的音乐
        pg.mixer.music.load(self.music_dict[key])
        # 播放音乐
        pg.mixer.music.play()
        # self.state场景 = state
        self.state = state

    def stop_music(self):
        """Stops playback
        停止播放"""
        # 音乐停止播放
        pg.mixer.music.stop()
