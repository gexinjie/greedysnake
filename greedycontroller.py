from greedycontext import _context
from greedyexception import DirectionError
from greedyitem import GreedySnake, GreedyFruit
from greedyexception import DieError


class GreedyController:
    direct = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}
    reverse_direct = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
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
        input_direct = GreedyController.direct.get(direct_key)    # could be None
        if self.cur_direction == input_direct or self.cur_direction ==GreedyController.reverse_direct.get(input_direct):
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
            return True
        return False

    def check_over(self):   # to see whether the snake hit itself
        the_snake = _context['SNAKE']
        snake_real_body = the_snake.body[:-1]       # real means except the head
        for p in snake_real_body:
            if p == the_snake.head_pos:
                raise DieError

    def check(self):
        if not self.check_eat():
            self.check_over()