from collections import deque
from array import array

# Container sequences allow for data of different types
# List, Tuple, collections.deque

list = ["dario", 1, 2, "Arias"]  # lists are mutable
# print(list)

tuple = ('dario', 1, 2, "Arias")  # tuples are immutable
# print(tuple)

deque = deque(list)
# print(deque.popleft())


# Flat sequences only allow data of the same time, usually primative
arr = array('d', [9.2, 2])
print(arr)


class MagicNumber(object):
  def __init__(self, value = 0) -> None:
    self.value = value

# magic_nums_arr = array('MagicNumber', [MagicNumber(1), MagicNumber(2)])  # wont work -:

