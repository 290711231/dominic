__author__ = 'dominic'

import os
import pygame as pg

keybinding = {
    'action': pg.K_s,
    'jump': pg.K_a,
    'left': pg.K_LEFT,
    'right': pg.K_RIGHT,
    'down': pg.K_DOWN
}


class Control(object):
    """整个项目的控制类。
    包含游戏循环，并包含事件循环，根据需要将事件传递到状态。
    翻转状态的逻辑在这里也能找到。
    Control class for entire project. Contains the game loop, and contains
    the event_loop which passes events to States as needed. Logic for flipping
    states is also found here."""

    def __init__(self, caption):
        # 获取对当前设置的显示表面的引用
        self.screen = pg.display.get_surface()
        self.done = False
        # 创造游戏时钟
        self.clock = pg.time.Clock()
        # caption属性
        self.caption = caption
        # fps属性，赋值60
        self.fps = 60
        self.show_fps = False
        # 定义当前时间current_time属性为0.0
        self.current_time = 0.0
        # key属性获取所有键盘的状态
        self.keys = pg.key.get_pressed()
        self.state_dict = {}
        # 定义state_name属性
        self.state_name = None
        # 定义state属性
        self.state = None

    def setup_states(self, state_dict, start_state):  # 定义setup states方法
        # 用参数给state_dict赋值
        self.state_dict = state_dict
        # 给state_name赋值
        self.state_name = start_state
        # self.state 指向 字典state_dict中state_name
        self.state = self.state_dict[self.state_name]

    def update(self):  # 定义update方法
        # 得到以毫秒为间隔的当前时间
        self.current_time = pg.time.get_ticks()
        if self.state.quit:  # 判断state.quit是否为True
            self.done = True
        elif self.state.done:  # 判断state.done是否为True
            # 调用flip_state方法
            self.flip_state()
        # 调用state.update方法(即main_menu.Menu.update方法，并传入显示平面，按钮和当前时间参数)
        self.state.update(self.screen, self.keys, self.current_time)

    def flip_state(self):
        # previous = self.state_name,self.state_name = self.state.next
        previous, self.state_name = self.state_name, self.state.next
        # 调用state.cleanup方法（）
        persist = self.state.cleanup()
        # self.state 指向 字典state_dict中state_name中的值
        self.state = self.state_dict[self.state_name]
        # 调用state.startup方法，传入当前时间和persist
        self.state.startup(self.current_time, persist)
        # 给state_previous 赋值为self.state_name
        self.state.previous = previous

    def event_loop(self):  # 循环事件，监测键盘状态
        # 遍历待处理事件列表
        for event in pg.event.get():
            # 判断是否按下关闭
            if event.type == pg.QUIT:
                self.done = True
            # 判断是否按下键盘
            elif event.type == pg.KEYDOWN:
                # 获取输入键盘
                self.keys = pg.key.get_pressed()
                # 调用toggle_show_fps方法
                self.toggle_show_fps(event.key)
            # 判断是否抬起键盘
            elif event.type == pg.KEYUP:
                # 获取输入键盘
                self.keys = pg.key.get_pressed()
            self.state.get_event(event)

    def toggle_show_fps(self, key):  # 按下F5，在窗口标题显示帧率
        # 判断是否按下F5
        if key == pg.K_F5:
            # self.show_fps为反
            self.show_fps = not self.show_fps
            # 如果为不是self.show_fps为Flase
            if not self.show_fps:
                # 设置当前窗体标题为self.caption
                pg.display.set_caption(self.caption)

    def main(self):
        """Main loop for entire program
        他是整个主程序循环使用
        """
        while not self.done:  # 是否done为空
            # 调用循环处理方法，监测键盘状态
            self.event_loop()
            # 调用update方法
            self.update()
            # 更新画面
            pg.display.update()
            # 每秒钟设置60次更新，即帧率为60
            self.clock.tick(self.fps)
            # 判断是否显示帧率
            if self.show_fps:
                # 获取当前帧率
                fps = self.clock.get_fps()
                # with_fps为窗体名称：caption - fps值
                with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
                # 把with_fps显示在窗体标题上
                pg.display.set_caption(with_fps)


class _State(object):
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None
        self.persist = {}

    def get_event(self, event):
        pass

    def startup(self, current_time, persistant):
        self.persist = persistant
        self.start_time = current_time

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):
        pass


def load_all_gfx(directory, colorkey=(255, 0, 255), accept=('.png', 'jpg', 'bmp')):
    '''

    :param 文件夹名:
    :param 色值rgb:
    :param 文件类型:
    :return:set_colorkey
    '''
    graphics = {}  # 声明图集字典
    for pic in os.listdir(directory):
        # 遍历文件名下的所有文件
        name, ext = os.path.splitext(pic)  # 拆分成文件名和扩展名
        if ext.lower() in accept:  # 判断扩展名（小写）是否在文件类型中
            img = pg.image.load(os.path.join(directory, pic))
            # 变量img = 载入图片函数（连接目录名和遍历到的图片文件名）
            if img.get_alpha():  # 判断图片的是否有alpha通道
                img = img.convert_alpha()
                # img = 保留alpha通道的图
            else:
                img = img.convert()  # img = 不保留alpaa通道的图
                img.set_colorkey(colorkey)
                # 将与colorkey（255,0,255）相同的颜色变成透明
            graphics[name] = img
            # 添加字典元素[name名称：遍历到的图片img]
    return graphics  # 返回遍历得到的图片合集


def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    '''
    :param 文件夹名:
    :param 文件类型:
    :return: 返回遍历到的歌名

    '''
    songs = {}  # 建立歌名字典
    for song in os.listdir(directory):  # 遍历参数文件夹中的文件
        name, ext = os.path.splitext(song)  # 将遍历来的文件名和扩展名分离
        if ext.lower() in accept:  # 判断扩展名（小写）在不在accept里
            songs[name] = os.path.join(directory, song)
            # 添加字典元素[name名称：将参数文件夹名和遍历到的文件名合并后的名字]
    return songs  # 返回遍历到的歌名字典


def load_all_fonts(directory, accept=('.ttf')):
    '''

    :param 文件夹名:
    :param 文件类型:
    :return:返回字体名

    '''
    return load_all_music(directory, accept)
    # 继承返回遍历歌名的操作，来建立字体字典


def load_all_sfx(directory, accept=('.wav', '.mpe', '.ogg', '.mdi')):
    '''

    :param 文件夹名:
    :param 文件类型:
    :return:返回音效集合
    '''
    effects = {}  # 建立音效字典
    for fx in os.listdir(directory):  # 遍历参数文件夹中的文件
        name, ext = os.path.splitext(fx)  # 分离文件名和扩展名
        if ext.lower() in accept:  # 检测扩展名是否在文件类型里
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
            # 建立effects字典[name名称：遍历到的文件的音效对象]
    return effects  # 返回音效字典
