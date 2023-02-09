import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'Point({self.x}, {self.y})')

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

# a = Point(0, 0)
# b = Point(0, 4)
# a.show()
# a.move(0, 1)
# print(a.dist(b))
