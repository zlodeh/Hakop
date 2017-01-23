class Figura(object):

    def squar(self):
        raise NotImplementedError


class Circle


class Rect(Figura):
    def squar(self):
        return  math.p

    def __str__(self):
        return 'krug R={}'.format(self.radius)


    def __str__(self):
        return 'rectagle {}x{}'.format(self.width, self.height)

class Square(Circle):
    def squar(self):
        return

c = Circle(10)
r = Rect(5, 5)
s = Square(10)

l = [c, r, s]

common_s = 0
for fig in l:
    common_s += fig.squar()
print(common_s)




class Gettor(object):
    def __init__(self):
        self.collection = []


    def __add__.figure(self, 'cirlce', 'square, ''):
