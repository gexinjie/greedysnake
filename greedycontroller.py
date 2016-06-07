from greedycontext import _context
from greedyexception import DirectionError
from greedyitem import GreedySnake, GreedyFruit


class GreedyController:
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

    def turn(self, input_keys):
        try:                            # input_key could be anything(still string)
            direct_key = input_keys[0]  # while direct_key should be 'w', 'a', 's', 'd',
        except IndexError as e:         # so interpret it to cur_direction
            GreedyController.snake_move[self.cur_direction]()
            return

        if self.cur_direction == GreedyController.direct.get(direct_key, None):
            pass
        else:
            try:
                self.cur_direction = GreedyController.direct[direct_key]
            except DirectionError as e:
                pass
            except KeyError as e:   # when having key that unknown, not bother to change
                pass
        GreedyController.snake_move[self.cur_direction]()

    def check_eat(self):
        the_fruits = _context['FRUITS']
        the_snake = _context['SNAKE']
        for fruit in the_fruits:
            if fruit.pos == the_snake.head_pos:
                the_snake.grow()
                fruit.flush()