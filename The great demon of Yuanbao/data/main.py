__author__ = 'dominic'

from . import setup,tools
from .states import main_menu,load_screen,level1
from . import constants as c


def main():
    """
    Add states to control here.
    添加属性来控制这里
    """
    #用tools中的Control类初始化，用于控制游戏
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    #创造字典state_dict
    state_dict = {c.MAIN_MENU: main_menu.Menu(),
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.TIME_OUT: load_screen.TimeOut(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.LEVEL1: level1.Level1()}

    #调用run_it中Control类中setup_states方法
    #让run_itde states属性 = state_dict字典里的MAIN_MENU对应的值(main_menu.Menu())
    run_it.setup_states(state_dict, c.MAIN_MENU)

    run_it.main()



