from point import point
from copy import deepcopy
from random import randrange
import time
import os
# from inputwithoutwait import getch    # getch don't work well on Pycharm
class GreedySnake:
    def __init__(self, pos_x, pos_y, bg_length, bg_width, pat='o'):     # 方向是否合法交给controler控制
        self.__len = 1                                                  # snake 需要知道背景大小, 不然碰到边框难以处理
        self.__pat = pat
        self.__head = point(pos_x, pos_y)
        self.__body = [deepcopy(self.__head)]
        self.__bg_wid = bg_width
        self.__bg_len = bg_length

    @property
    def pat(self):
        return self.__pat

    @property
    def body(self):
        return self.__body

    def grow(self):
        self.__body.insert(0, deepcopy(self.__body[0]))

    def move_right(self):
        self.__body.pop()
        self.__head.y += 1
        self.__head.y %= self.__bg_wid
        self.__body.append(deepcopy(self.__head))

    def move_left(self):
        self.__body.pop()
        self.__head.y += self.__bg_wid - 1      # equal to self.__head.y -= 1, but this way will produce negtive number
        self.__head.y %= self.__bg_wid
        self.__body.append(deepcopy(self.__head))

    def move_up(self):
        self.__body.pop()
        self.__head.x +=  self.__bg_len - 1
        self.__head.x %= self.__bg_len
        self.__body.append(deepcopy(self.__head))

    def move_down(self):
        self.__body.pop()
        self.__head.x += 1
        self.__head.x %= self.__bg_len
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
    def __init__(self, length, width, autofill=' '):
        self.__len = length
        self.__wid = width
        self.__autofill = autofill

    def paint(self, the_snake, the_fruit=None):
        self.__graph = [[self.__autofill for i in range(self.__wid)] for i in range(self.__len)]
        assert isinstance(the_snake, GreedySnake), print('snake is needed!')
        snake_pat = the_snake.pat
        for p in the_snake.body:
            try:
                self.__graph[p.x][p.y] = snake_pat
            except IndexError as e: # a intersting thing happen!(this happen before i have the dot moded) the snake come to bottom after hit the ceiling! don't understand what heppened
                pass    # just for now, i will edit it later

        for line in self.__graph:
            for pix in line:
                print(pix, end='')
            print()

class DirectionError(Exception):
    pass

class GreedyController:
    direct = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}
    snake_move = {}
    def __init__(self, the_snake, init_direction='right'):
        assert isinstance(the_snake, GreedySnake)
        self.cur_direction = init_direction
        self.__snake = the_snake
        GreedyController.snake_move = {'up': self.__snake.move_up, 'down': self.__snake.move_down, 'left': self.__snake.move_left, 'right': self.__snake.move_right}

    @property
    def cur_direction(self): # cur_direction: 'up', 'down', 'right', 'left'
        return self.__cur_direction

    @cur_direction.setter
    def cur_direction(self, direction):
        if direction not in GreedyController.direct.values():
            raise DirectionError
        else:
            self.__cur_direction = direction

    def turn(self, direction):
        if self.cur_direction == GreedyController.direct.get(direction, None):
            pass
        else:
            try:
                self.cur_direction = GreedyController.direct[direction]
            except DirectionError as e:
                pass
        GreedyController.snake_move[self.cur_direction]()

class GreedyApp:
    def __init__(self, length, width):
        self.__len = length
        self.__wid = width
        self.__graph = GreedyGraph(length, width)
        self.__snake = GreedySnake(width//2, length//2, length, width)
        self.__controller = GreedyController(self.__snake)

    def run(self):
        self.__graph.paint(self.__snake)
        while True:
            # input_key = getch()
            input_key = input()
            self.__controller.turn(input_key[0])
            os.system('clear')
            self.__graph.paint(self.__snake)




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
    app = GreedyApp(30, 30)
    app.run()


