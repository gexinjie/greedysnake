from greedyitem import GreedySnake
from greedycontext import _context

class GreedyGraph:
    def __init__(self):
        self.__graph = None

    def paint(self):
        self.__graph = [[_context['BG_AUTOFILL'] for i in range(_context['BG_WID'])] for i in range(_context['BG_LEN'])]
        the_snake = _context['SNAKE']
        the_fruits = _context['FRUITS']
        snake_pat = _context['SNAKE_PAT']
        fruit_pat = _context['FRUIT_PAT']
        for p in the_snake.body:
            try:
                self.__graph[p.x][p.y] = snake_pat
            except IndexError as e:  # a interesting thing happen!
                pass                 # (this happen before i have the dot moded)
                                     # the snake come to bottom after hit the ceiling!don't understand what heppened
                                     # just for now, i will edit it later
        for fruit in the_fruits:
            p = fruit.pos
            self.__graph[p.x][p.y] = fruit_pat

        for line in self.__graph:
            for pix in line:
                print(pix, end='')
            print()

