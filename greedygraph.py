from greedyitem import GreedySnake
from greedyapp import _context

class GreedyGraph:
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
            except IndexError as e:  # a interesting thing happen!
                pass                 # (this happen before i have the dot moded)
                                     # the snake come to bottom after hit the ceiling!don't understand what heppened
                                     # just for now, i will edit it later
        for line in self.__graph:
            for pix in line:
                print(pix, end='')
            print()


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
    #app = GreedyApp()
    #app.run()


