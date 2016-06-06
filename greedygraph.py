from point import point
from copy import deepcopy
from random import randrange
import time
import os
# from inputwithoutwait import getch    # getch don't work well on Pycharm

_context = {'GRAPH': None, 'SNAKE': None, 'CONTROLLER': None, 'FRUIT': None, 'BG_LEN': None, 'BG_WID': None,
            'BG_AUTOFILL': None, 'SNAKE_INIT_DIRECTION': None, 'SNAKE_START_FROM_X': None, 'SNAKE_START_FROM_Y': None,
            'SNAKE_PAT': None, 'FRUIT_PAT': None}

class GreedySnake:
    global _context
    '''
    def __init__(self, pos_x, pos_y, bg_length, bg_width, pat='o'):     # 方向是否合法交给controler控制
        self.__len = 1                                                  # snake 需要知道背景大小, 不然碰到边框难以处理
        self.__pat = pat
        self.__head = point(pos_x, pos_y)
        self.__body = [deepcopy(self.__head)]
        self.__bg_wid = bg_width
        self.__bg_len = bg_length
    '''

    def __init__(self):
        self.__head = point(_context['SNAKE_START_FROM_X'], _context['SNAKE_START_FROM_Y'])
        self.__len = 1
        self.__body = [deepcopy(self.__head)]

    @property
    def body(self):
        return self.__body

    def grow(self):    # !need to grow before take step
        self.__body.insert(0, deepcopy(self.__body[0]))

    def move_right(self):
        self.__body.pop()
        self.__head.y += 1
        self.__head.y %= _context['BG_WID']
        self.__body.append(deepcopy(self.__head))

    def move_left(self):
        self.__body.pop()
        self.__head.y += _context['BG_WID'] - 1   # equal to self.__head.y -= 1,
        self.__head.y %= _context['BG_WID']       # but this way will produce negative number
        self.__body.append(deepcopy(self.__head))

    def move_up(self):
        self.__body.pop()
        self.__head.x += _context['BG_LEN'] - 1
        self.__head.x %= _context['BG_LEN']
        self.__body.append(deepcopy(self.__head))

    def move_down(self):
        self.__body.pop()
        self.__head.x += 1
        self.__head.x %= _context['BG_LEN']
        self.__body.append(deepcopy(self.__head))

    def __str__(self):
        body = ''
        for point in self.__body:
            body += str(point)
        return body

class GreedyFruit:
    def __init__(self):
        return None


class GreedyGraph:
    global _context

    '''
    def __init__(self, length=30, width=30, autofill=' '):
        self.__len = length
        self.__wid = width
        self.__autofill = autofill
    '''
    def __init__(self):
        self.__graph = None

    def paint(self):
        self.__graph = [[_context['BG_AUTOFILL'] for i in range(_context['BG_WID'])] for i in range(_context['BG_LEN'])]
        the_snake = _context['SNAKE']
        assert isinstance(the_snake, GreedySnake), print('snake is needed!')
        snake_pat = _context['SNAKE_PAT']
        for p in the_snake.body:
            try:
                self.__graph[p.x][p.y] = snake_pat
            except IndexError as e: # a intersting thing happen!
                pass                # (this happen before i have the dot moded)
                                    # the snake come to bottom after hit the ceiling!don't understand what heppened
                                    # just for now, i will edit it later

        for line in self.__graph:
            for pix in line:
                print(pix, end='')
            print()

class DirectionError(Exception):
    pass


class GreedyController:
    global _context

    direct = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}
    snake_move = {}
    def __init__(self):
        the_snake = _context['SNAKE']
        assert isinstance(the_snake, GreedySnake)
        self.__cur_direction = _context['SNAKE_INIT_DIRECTION']
        GreedyController.snake_move = {'up': the_snake.move_up, 'down': the_snake.move_down,
                                       'left': the_snake.move_left, 'right': the_snake.move_right}

    @property
    def cur_direction(self): # cur_direction: 'up', 'down', 'right', 'left'
        return self.__cur_direction

    @cur_direction.setter
    def cur_direction(self, direct):    # direct is already interpreted to 'up', 'down', 'right', 'left'
        if direct not in GreedyController.direct.values():
            raise DirectionError
        else:
            self.__cur_direction = direct

    def turn(self, direction):      # direction could be 'w', 'a', 's', 'd', so interpret it to cur_direction
        if self.cur_direction == GreedyController.direct.get(direction, None):
            pass
        else:
            try:
                self.cur_direction = GreedyController.direct[direction]
            except DirectionError as e:
                pass
        GreedyController.snake_move[self.cur_direction]()

class GreedyApp:
    '''
    def __init__(self, the_graph=None, the_controller=None, the_snake=None, the_fruit=None): # !fruit未完成
        context['GRAPH'] = the_graph or GreedyGraph()
        context['SNAKE'] = the_snake or GreedySnake()
        context['CONTROLLER'] = the_controller or GreedyController()
        # context['Fruit'] = the_fruit or GreedyFruit()

        self.__len = length
        self.__wid = width
        self.__graph = GreedyGraph(length, width)
        self.__snake = GreedySnake(width//2, length//2, length, width)
        self.__controller = GreedyController(self.__snake)

    '''
    global _context

    def __init__(self, context={}):  # !fruit未完成
        _context['BG_LEN'] = context.get('BG_LEN', None) or 30      # these constants need to be initialized first
        _context['BG_WID'] = context.get('BG_WID', None) or 30      # the snake and others need them
        _context['BG_AUTOFILL'] = context.get('BG_AUTOFILL', None) or ' '
        _context['SNAKE_START_FROM_X'] = context.get('SNAKE_START_FROM_X', None) or _context['BG_WID'] // 2
        _context['SNAKE_START_FROM_Y'] = context.get('SNAKE_START_FROM_Y', None) or _context['BG_LEN'] // 2
        _context['SNAKE_PAT'] = context.get('SNAKE_PAT', None) or 'o'
        _context['SNAKE_INIT_DIRECTION'] = context.get('SNAKE_INIT_DIRECTION', None) or 'right'
        _context['GRAPH'] = context.get('GRAPH', None) or GreedyGraph()
        _context['SNAKE'] = context.get('SNAKE', None) or GreedySnake()
        _context['CONTROLLER'] = context.get('CONTROLLER', None)or GreedyController()


        # _context['Fruit'] = context.get('FRUIT', None) or GreedyFruit()

    def run(self):
        the_graph = _context['GRAPH']
        the_snake = _context['SNAKE']
        the_controller = _context['CONTROLLER']
        the_graph.paint()
        while True:
            # input_key = getch()
            input_key = input()
            the_controller.turn(input_key[0])
            os.system('clear')
            the_graph.paint()


if __name__ == '__main__':
    """
    length = 30
    width = 30
    graph = GreedyGraph(length, width)
    snake = GreedySnake(length//2, width//2)
    print(snake)

    print('-' * width)
    graph.paint(snake)
    print('-' * width)

    snake.move_right()
    print(snake)
    snake.grow()
    snake.move_down()
    print(snake)

    print('-'*width)
    graph.paint(snake)
    print('-'*width)

    controller = GreedyController(snake)
    """
    app = GreedyApp()
    app.run()


    print('i just want to use git')
    print('please change')
