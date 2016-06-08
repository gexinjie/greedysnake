from greedycontext import _context
from greedyitem import GreedySnake, GreedyFruit
from greedygraph import GreedyGraph
from greedycontroller import GreedyController
import os

class GreedyApp:
    def __init__(self, context={}):  # !fruit未完成
        _context['BG_LEN'] = context.get('BG_LEN') or 30      # these constants need to be initialized first
        _context['BG_WID'] = context.get('BG_WID') or 30      # the snake and others need them
        _context['BG_AUTOFILL'] = context.get('BG_AUTOFILL') or ' '
        _context['SNAKE_START_FROM_X'] = context.get('SNAKE_START_FROM_X') or _context['BG_WID'] // 2
        _context['SNAKE_START_FROM_Y'] = context.get('SNAKE_START_FROM_Y') or _context['BG_LEN'] // 2
        _context['SNAKE_PAT'] = context.get('SNAKE_PAT') or 'o'
        _context['SNAKE_INIT_DIRECTION'] = context.get('SNAKE_INIT_DIRECTION') or 'right'
        _context['FRUIT_PAT'] = '*'
        _context['GRAPH'] = context.get('GRAPH') or GreedyGraph()
        _context['SNAKE'] = context.get('SNAKE') or GreedySnake()
        _context['FRUITS'] = context.get('FRUITS') or (GreedyFruit(), )
        _context['CONTROLLER'] = context.get('CONTROLLER', None)or GreedyController()

    def run(self):
        the_graph = _context['GRAPH']
        # the_snake = _context['SNAKE']
        the_fruits = _context['FRUITS']
        the_controller = _context['CONTROLLER']
        the_graph.paint()
        while True:
            # input_key = getch()
            the_controller.check_eat()
            input_str = input()
            the_controller.turn(input_str)
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
