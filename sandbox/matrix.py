from collections import namedtuple

# North
grid = [
  [0, 0, 0, 0, 0, 0],
  [0, 1, 1, 0, 0, 0],
  [0, 1, 1, 1, 1, 0],
  [0, 0, 1, 1, 0, 0],
  [0, 1, 1, 0, 0, 0],
  [0, 0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0],
]
# South 

Point = namedtuple('Point', 'row col')

points = [ 

  Point(5, 2), Point(4, 1),
  Point(1, 1), Point(2, 2), Point(2, 1), 
  Point(1, 2), Point(2, 3),
  Point(3, 3), Point(3, 2), Point(2, 4), 
  Point(4, 2),
]


def top_to_bottom_left_to_right(point: Point):
  top_val = point.row
  left_val = point.col
  sort_val = (top_val + left_val) + (top_val * 100)
  print(point, f"has sorted value {sort_val}")
  return sort_val

print(sorted(points, key=top_to_bottom_left_to_right))