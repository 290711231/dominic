__author__ = 'dominic'

from . import setup,tools
from .states import main_menu,load_screen,level1
from . import constants as c


def main():
    """
    Add states to control here.
    添加属性来控制这里
    """
    #用tools中的Control类初始化，用于控制游戏，传入caption参数并在窗口名称显示
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    #创造字典state_dict
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.TIME_OUT: load_screen.TimeOut(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.LEVEL1: level1.Level1()}

    #调用run_it中Control类中setup_states方法，传入strate_dict字典和'main menu'字符串
    run_it.setup_states(state_dict, c.MAIN_MENU)
    #调用run_it.main方法，运行游戏
    run_it.main()



