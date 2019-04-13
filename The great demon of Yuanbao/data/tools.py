__author__ = 'dominic'

import os
import pygame as pg

keybinding = {
    'action':pg.K_s,
    'jump':pg.K_a,
    'left':pg.K_LEFT,
    'right':pg.K_RIGHT,
    'down':pg.K_DOWN
}

class Control(object):
    """整个项目的控制类。
    包含游戏循环，并包含事件循环，根据需要将事件传递到状态。
    翻转状态的逻辑在这里也能找到。
    Control class for entire project. Contains the game loop, and contains
    the event_loop which passes events to States as needed. Logic for flipping
    states is also found here."""
    def __init__(self, caption):
        self.screen = pg.display.get_surface()#获取对当前设置的显示表面的引用
        self.done = False
        self.clock = pg.time.Clock()#刷新率
        self.caption = caption
        self.fps = 60
        self.show_fps = False
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()#获取所有键盘的状态
        self.state_dict = {}
        self.state_name = None
        self.state = None

    def setup_states(self, state_dict, start_state): #定义setup states方法
        self.state_dict = state_dict #用参数给dict赋值
        self.state_name = start_state
        self.state = self.state_dict[self.state_name] #self.state = 字典state_dict中state_name中的值

    def update(self):
        self.current_time = pg.time.get_ticks()
        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(self.screen, self.keys, self.current_time)

    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)
        self.state.previous = previous


    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
                self.toggle_show_fps(event.key)
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
            self.state.get_event(event)


    def toggle_show_fps(self, key):
        if key == pg.K_F5:
            self.show_fps = not self.show_fps
            if not self.show_fps:
                pg.display.set_caption(self.caption)


    def main(self):
        """Main loop for entire program
        他是整个主程序循环使用
        """
        while not self.done: #是否done为空
            self.event_loop()
            self.update()
            pg.display.update()
            self.clock.tick(self.fps)
            if self.show_fps:
                fps = self.clock.get_fps()
                with_fps = "{} - {:.2f} FPS".format(self.caption, fps)
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



def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', 'jpg', 'bmp')):
    '''

    :param 文件夹名:
    :param 色值rgb:
    :param 文件类型:
    :return:
    '''
    graphics = {}#声明图集字典
    for pic in os.listdir(directory):
        #遍历文件名下的所有文件
        name, ext = os.path.splitext(pic)#拆分成文件名和扩展名
        if ext.lower() in accept:#判断扩展名（小写）是否在文件类型中
            img = pg.image.load(os.path.join(directory, pic))
            #变量img = 载入图片函数（连接目录名和遍历到的图片文件名）
            if img.get_alpha():#判断图片的是否有alpha通道
                img = img.convert_alpha()
                #img = 保留alpha通道的图
            else:
                img = img.convert()#img = 不保留alpaa通道的图
                img.set_colorkey(colorkey)
                #将与colorkey（255,0,255）相同的颜色变成alpha
            graphics[name]=img
            #添加字典元素[name名称：遍历到的图片img]
    return graphics #返回遍历得到的图片合集


def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    '''
    :param 文件夹名:
    :param 文件类型:
    :return: 返回遍历到的歌名

    '''
    songs = {}#建立歌名字典
    for song in os.listdir(directory):#遍历参数文件夹中的文件
        name,ext = os.path.splitext(song)#将遍历来的文件名和扩展名分离
        if ext.lower() in accept:#判断扩展名（小写）在不在accept里
            songs[name] = os.path.join(directory, song)
            #添加字典元素[name名称：将参数文件夹名和遍历到的文件名合并后的名字]
    return songs#返回遍历到的歌名字典


def load_all_fonts(directory, accept=('.ttf')):
    '''

    :param 文件夹名:
    :param 文件类型:
    :return:返回字体名

    '''
    return load_all_music(directory, accept)
    #继承返回遍历歌名的操作，来建立字体字典


def load_all_sfx(directory, accept=('.wav','.mpe','.ogg','.mdi')):
    '''

    :param 文件夹名:
    :param 文件类型:
    :return:返回音效集合
    '''
    effects = {}#建立音效字典
    for fx in os.listdir(directory):#遍历参数文件夹中的文件
        name, ext = os.path.splitext(fx)#分离文件名和扩展名
        if ext.lower() in accept:#检测扩展名是否在文件类型里
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
            #建立effects字典[name名称：遍历到的文件的音效对象]
    return effects #返回音效字典











