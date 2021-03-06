__author__ = 'dominic'

from .. import setup, tools
from .. import constants as c
from .. import game_sound
from ..components import info


class LoadScreen(tools._State):
    #创建LoadScreen类，继承自tool._State
    def __init__(self):
        #继承tool._State全部__init__属性
        tools._State.__init__(self)

    def startup(self, current_time, persist):
        #self.start_time = 传入的参数current_time
        self.start_time = current_time
        #self.persist = 传入的参数persist
        self.persist = persist
        #将self.persist赋值给self.game_info
        self.game_info = self.persist
        #self.next = 方法self.set_next_state的返回值（即： 'level1'）
        self.next = self.set_next_state()
        #info_state = 方法self.set_overhead_info_state的返回值（即：'load screen'）
        info_state = self.set_overhead_info_state()
        #传入参数（self.game_info,info_state）并用info.OverheadInfo实例化一个对象self.overhead_info
        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        #传入参数（self.overhead_info）并用game_sound.Sound实例化一个对象self.sound_manager
        self.sound_manager = game_sound.Sound(self.overhead_info)


    def set_next_state(self):
        """Sets the next state
        设置下一个状态"""
        return c.LEVEL1

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.LOAD_SCREEN


    def update(self, surface, keys, current_time):
        """Updates the loading screen"""
        if (current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)

        elif (current_time - self.start_time) < 2600:
            surface.fill(c.BLACK)

        elif (current_time - self.start_time) < 2635:
            surface.fill((106, 150, 252))

        else:
            self.done = True




class GameOver(LoadScreen):
    """A loading screen with Game Over"""
    def __init__(self):
        super(GameOver, self).__init__()


    def set_next_state(self):
        """Sets next state"""
        return c.MAIN_MENU

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        return c.GAME_OVER

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.sound_manager.update(self.persist, None)

        if (self.current_time - self.start_time) < 7000:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        elif (self.current_time - self.start_time) < 7200:
            surface.fill(c.BLACK)
        elif (self.current_time - self.start_time) < 7235:
            surface.fill((106, 150, 252))
        else:
            self.done = True


class TimeOut(LoadScreen):
    """Loading Screen with Time Out"""
    def __init__(self):
        super(TimeOut, self).__init__()

    def set_next_state(self):
        """Sets next state"""
        if self.persist[c.LIVES] == 0:
            return c.GAME_OVER
        else:
            return c.LOAD_SCREEN

    def set_overhead_info_state(self):
        """Sets the state to send to the overhead info object"""
        return c.TIME_OUT

    def update(self, surface, keys, current_time):
        self.current_time = current_time

        if (self.current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        else:
            self.done = True









