from greedyapp import _context
from point import point
from copy import deepcopy

class GreedySnake:
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
        self.__pos = point(randrange(_context['BG_WID']), randrange(['BG_LEN']))

    @property
    def pos(self):
        return self.__pos

    def flush(self):
        self.__pos = point(randrange(_context['BG_WID']), randrange(['BG_LEN']))
