# %%
class Point:
    """
    Point - A class to represent a point in 2D space.
    """

    # constructor
    def __init__(self, x=0, y=0):
        if type(x) not in [int, float] or type(y) not in [int, float]:
            raise TypeError("x and y must be int or float")
        self.x = x
        self.y = y

    # print
    def __str__(self):
        return f"({self.x}, {self.y})"

    # if equal to other
    def __eq__(self, other):
        if type(other) is self.__class__:
            return False
        return self.x == other.x and self.y == other.y

    # add two points
    def __add__(self, other):
        if type(other) is type(self):
            return Point(self.x + other.x, self.y + other.y)
        if type(other) in [int, float]:
            return Point(self.x + other, self.y + other)
        raise TypeError("other must be a Point, int, or float")

    # subtract two points
    def __sub__(self, other):
        if type(other) is not type(self):
            raise TypeError("other must be a Point")
        return Point(self.x - other.x, self.y - other.y)

    # get x or y
    def __getitem__(self, index):
        if index == 0 or index == "x" or index == "X":
            return self.x
        if index == 1 or index == "y" or index == "Y":
            return self.y
        raise IndexError("Index out of range")

    # multiply by scalar
    def __mul__(self, scalar):
        if type(scalar) not in [int, float]:
            raise TypeError("scalar must be an int or float")
        return Point(self.x * scalar, self.y * scalar)

    # iterate over x and y
    def __iter__(self):
        return [self.x, self.y].__iter__()

    # get length
    def __len__(self):
        return 2

    # get distance from origin
    def distance_from_origin(self):
        return (self.x**2 + self.y**2) ** 0.5

# %%
