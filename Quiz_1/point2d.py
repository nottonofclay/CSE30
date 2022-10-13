import math

class Point2D:

    # x and y are the x and y coordinates of a point
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # returns a string in the following format: '(x, y)'
    def __str__(self):
        return f'({self.x}, {self.y})'

    # returns a distance between two points self and point
    def distance(self, point):
        return math.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)

    # returns a new Point2D with x = x1 + x2 and y = y1 + y2, where x1 and x2 and
    # y1 and y2 are x and y coordinates
    def __add__(self, point):
        return Point2D((self.x + point.x), (self.y + point.y))

    # returns a new Point2D with x = x1 - x2 and y = y1 - y2, where x1 and x2 and
    # y1 and y2 are x and y coordinates
    def __sub__(self, point):
        return Point2D((self.x - point.x), (self.y - point.y))

    # returns a new Point2D with x = x1 * scalar and y = y1 * scalar
    def __mul__(self, scalar):
        return Point2D((self.x * scalar), (self.y * scalar))

    # True if points have the same coordinates or the distance between them
    # is equal or less than the threshold 0.000001
    def __eq__(self,point):
        if self.distance(point) <= 0.000001 :
            return True
        return False


if __name__ == '__main__':
    A = Point2D(1, 1)
    B = Point2D(0, 0)
    C = Point2D(0, 3)
    D = Point2D(0, 1)
    print(A)             # should print (1.0, 1.0)
    assert A == Point2D(1,1)
    print(A + B)         # should print (1.0, 1.0)
    assert A + B == Point2D(1,1)
    print(A - C)         # should print (1.0, -2.0)
    assert A - C == Point2D(1, -2)
    print(A * 3)         # should print (3.0, 3.0)
    assert A * 3 == Point2D(3, 3)
    print(D.distance(C)) # should print 2.0
    assert D.distance(C) == 2.0
    print(B == A)        # should print False
    assert B != A
    print(B == A * 0)    # should print True
    assert B == A * 0
    print('Everything works correctly!')