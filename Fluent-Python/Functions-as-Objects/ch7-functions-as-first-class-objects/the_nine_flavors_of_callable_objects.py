# The call operator () may be applied to other objects besides functions. 
# To determine whether an object is callable, use the callable() built-in function

# Below is a list of all of the callable objects as in Python 3.9
# User-defined functions
## Created with def statements or lambda expressions.

# Built-in functions
## A function implemented in C (for CPython), like len or time.strftime.

# Built-in methods
## Methods implemented in C, like dict.get.

# Methods
## Functions defined in the body of a class.

# Classes
## When invoked, a class runs its __new__ method to create an instance, 
## then __init__ to initialize it, and finally the instance is returned to the caller. 
## Because there is no new operator in Python, calling a class is like calling a function.

# Class instances
## If a class defines a __call__ method, then its instances may be invoked as 
## functions—that’s the subject of the next section.

# Generator functions
## Functions or methods that use the yield keyword in their body. 
## When called, they return a generator object

# Native coroutine functions
## Functions or methods defined with async def. 
## When called, they return a coroutine object. Added in Python 3.5.

# Asynchronous generator functions
## Functions or methods defined with async def that have yield in their body. 
## When called, they return an asynchronous generator for use with async for. Added in Python 3.6.


# using built in "callable" to check if something is a function, i.e can be called
for obj in (abs, str, 'Ni!'):
  # print(f'{obj!r} is callable <{callable(obj)}>')
  pass


# User-Defined Callable Types
# Python objects may also be made to behave like functions. Implementing a __call__ instance method is all it takes.
import random

class BingoCage:
  def __init__(self, items) -> None:
    self._items = list(items)
    random.shuffle(self._items)
  
  def pick(self):
    try:
      return self._items.pop()
    except IndexError:
      raise LookupError('pick from empty BingoCage')
  
  def __repr__(self) -> str:
    cls = self.__class__
    name = cls.__name__
    return f'{name}({self._items!r})'

  def __call__(self):
    return self.pick()

def numbers(min: int = 0, max: int = 5):
  for number in range(min, max):
    yield number

# cage = BingoCage(numbers(min=1, max=10))
cage = BingoCage(range(10))
print(cage, range(1))