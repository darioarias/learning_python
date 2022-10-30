# Whenever Python needs to iterate over an object x, it automatically calls iter(x).
# The iter built-in function:
# 1. Checks whether the object implements __iter__, and calls that to obtain an iterator.
# 2. If __iter__ is not implemented, but __getitem__ is, then iter() creates an iter‐ ator that tries to fetch items by index, starting from 0 (zero).
# 3. If that fails, Python raises TypeError, usually saying 'C' object is not itera ble, where C is the class of the target object.

from collections import abc
from random import randint


class Spam:
    def __getitem__(self, i):
        print(' ->', i)
        raise IndexError()

# spam_can = Spam()
# print(iter(spam_can))  # <iterator object at 0x107553f10>
# print(list(spam_can))  #  -> 0, []
# print(isinstance(spam_can, abc.Iterable))  # False

class GooseSpam:
    def __iter__(self):
        pass 

# print(issubclass(GooseSpam, abc.Iterable))  # True
# goose_spam_can = GooseSpam()
# print(isinstance(goose_spam_can, abc.Iterable))  # True




## Using iter with a Callable
# We can call iter() with two arguments to create an iterator from a function or any callable object.

def d6():
    return randint(1, 6)

SENTINEL = 1
d6_iter = iter(d6, SENTINEL)

print(d6_iter)
for n in d6_iter:
    print(n)

