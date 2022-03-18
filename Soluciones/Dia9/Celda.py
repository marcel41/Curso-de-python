from pygame import  Rect
class Cell(Rect):
    BASE_COLOUR = (0, 0, 0)
    def __init__(self, position, cell_size, free, colour=BASE_COLOUR, left=None, right=None, up=None, down=None):
        self.__free = free
        self.__left = left
        self.__right = right
        self.__up = up
        self.__down = down
        self.__colour = colour
        self.__position = position
        self.__visible = True
        super().__init__(position[0]*cell_size, position[1]*cell_size, cell_size, cell_size)

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @property
    def up(self):
        return self.__up

    @property
    def down(self):
        return self.__down

    @left.setter
    def left(self, left):
        self.__left = left

    @right.setter
    def right(self, right):
        self.__right = right

    @up.setter
    def up(self, up):
        self.__up = up

    @down.setter
    def down(self, down):
        self.__down = down

    @property
    def free(self):
        return self.__free

    @free.setter
    def free(self, free):
        self.__free = free

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        self.__colour = colour

    @property
    def position(self):
        return self.__position

    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, value):
        self.__visible = value

    @position.setter
    def position(self, position):
        self.__position = position

    def clear(self):
        self.__colour = Cell.BASE_COLOUR
        self.__free = True

    def set(self, colur):
        self.__colour = colur
        self.__free = False
        
