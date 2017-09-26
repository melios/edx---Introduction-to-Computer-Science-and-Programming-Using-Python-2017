## simple class for  the Euclidean distance or Euclidean metric

class Coordinate (object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0,5

    def __str__(self):
        #return  ('str(self.x) is {},  str(self.y) is {}').format(self.x, self.y)
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

if __name__ == '__main__':
    pass

c = Coordinate(3,4)
zero = Coordinate(0,0)
print(c.distance(zero))
print('------')
print(Coordinate.distance(c, zero))
print(c)
print(isinstance(c, Coordinate))