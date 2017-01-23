class Point(object):
    def __init__(self, x, y):
       self.x = x
       self.y = y


    def __str__(self):
        return 'x: {}, y: {}'.format(self.x, self.y)

    def __repr__(self):
        return 'x: {}, y: {}'.format(self.x, self.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self

    def move(self, n = 1):
        self.x = self.x * -1 * n
        self.y = self.y * -1 * n
        return self

p1 = Point(1, 1)

x = p1.move()

print(x)
