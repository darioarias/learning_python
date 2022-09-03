
from collections import namedtuple, defaultdict
from math import gcd

Rectangle = namedtuple('Rectangle', ['width', 'hight'])

rects = [
  Rectangle(1, 2),
  Rectangle(15, 30),
  Rectangle(5, 10),
  Rectangle(3, 4),
  Rectangle(75, 100)
]

def same_ratio(rects):
  seen_ratios = defaultdict(int)
  for index, rect in enumerate(rects):
    common = gcd(rect.width, rect.hight)
    key = f'{rect.width//common},{rect.hight//common}'
    seen_ratios[key] = seen_ratios[key] + 1

  total = 0
  for value in (x for x in seen_ratios.values()):
    total += value
  return total

print(same_ratio(rects))