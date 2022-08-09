from collections import namedtuple


Color = namedtuple('Color', ['red', 'green', 'blue'])
Point = namedtuple('Point', "x y z")


white = Color(255, 255, 255)

p1 = Point(0, 2, 1)



print(p1._asdict())