class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def pat(self):
        return self.__pat

    def __add__(self, other):
        return point(self.x+other.x, self.y+other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return point(self.x-other.x, self.y-other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, num):
        return point(self.x*num, self.y*num)

    def __imul__(self, num):
        self.x = self.x*num
        self.y = self.y*num
        return self     # 为什么要return self?

    def __truediv__(self, num):
        return point(self.x/num, self.y/num)

    def __itruediv__(self, num):
        self.x, self.y = (self.x/num, self.y/num)
        return self

    def __floordiv__(self, num):
        return point(self.x//num, self.y//num)

    def __ifloordiv__(self, num):
        self.x, self.y = (self.x//num, self.y//num)
        return self

    def __str__(self):
        return 'point({}, {})'.format(self.x, self.y)


if __name__ == '__main__':
    p = point(1, 2)
    print(p*2)
    p *= 3
    print(p)
    print(p//2)
    print(p/2)
    print(__file__)
    from pprint import pprint
    pprint(globals())
    print('\n\n')
    pprint(locals())


