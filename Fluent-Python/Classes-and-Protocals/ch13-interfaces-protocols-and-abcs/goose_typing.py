
# Subclassing an ABC
from collections import namedtuple, abc

Card = namedtuple('Card', ['rank', 'suit'])

class FenchDeck2(abc.MutableSequence):
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self) -> None:
    self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

  def __len__(self) -> int:
    return len(self._cards)
  
  def __getitem__(self, position):
    return self._cards[position]
  
  def __setitem__(self, position, value):
    self._cards[position] = value
  
  def __delitem__(self, position):
    del self._cards[position]
  
  def insert(self, position, value):
    self._cards.insert(position, value)
  
# note that abc.MutableSequence forced us to implement a couple of functions here.
# namely; __init__, __getitem__, __setitem__, __delitem__, __len__, and insert().


# Defining and Using an ABC
import abc

class Tombola(abc.ABC):
  @abc.abstractmethod
  def load(self, iterable):
    """Add items from an iterable."""
  
  @abc.abstractmethod
  def pick(self):
    """Remove item at random, returning it.
    
    This method should raise `LookupError` when the instance is empty.
    """
  
  def loaded(self):
    """Return `True` if there's at least 1 item, `False` otherwise."""
    return bool(self.inspect())

  def inspect(self):
    """Return a sorted tuple with the items currently inside."""
    items = []
    while True:
      try:
        items.append(self.pick())
      except LookupError:
        break
    self.load(items)
    return tuple(items)


# trying to create a fake subclass
class Fake(Tombola):
  def pick(self):
    return 13

# f = Fake()  # will break--does not implement load

class MyABC(abc.ABC):
  @classmethod
  @abc.abstractmethod
  def an_abstract_classmethod(cls):
    pass
# show that we can stack decorators
# abc.abstractmethod decorator should be the inner most decorator


# Subclassing an ABC
import random

class BingoCage(Tombola):
  def __init__(self, items) -> None:
    self._randomizer = random.SystemRandom()
    self._items = []
    self.load(items)
  
  def load(self, items):
    self._items.extend(items)
    self._randomizer.shuffle(self._items)
  
  def pick(self):
    try: 
      return self._items.pop()
    except IndexError:
      raise LookupError('Pick from empty BingoCage')
    
  def __repr__(self):
    return f"{self._items!r}"
  
  def __call__(self):
    self.pick()

# this class inherrents the expensive loaded method
# but this is okay since we are not overly concerned with 
# complexity


class LottoBlower(Tombola):
  def __init__(self, iterable) -> None:
    self._balls = list(iterable)

  def load(self, iterable):
    self._balls.extend(iterable)
  
  def pick(self):
    try: 
      position = random.randrange(len(self._balls))
    except ValueError:
      raise LookupError('pick from empty LottoBlower')
    return self._balls.pop(position)

  def loaded(self):
    return bool(self._balls)
  
  def inspect(self):
    return tuple(self._balls)

# A virtual Subclass of an ABC

@Tombola.register
class TomboList(list):
  def pick(self):
    if self:
      position = random.randrange(len(self))
      return self.pop(position)
    else:
      raise LookupError('pop from empty TomoList')
    
  load = list.extend

  def loaded(self):
    return bool(self)

  def inspect(self):
    return tuple(self)

# Tombola.register(TomboList)

# __mro__ holds a reference to the superclasses types
# print(Tombola.__mro__)  # (<class '__main__.Tombola'>, <class 'abc.ABC'>, <class 'object'>)


# Usage of register in Practice
# in most cases register is called like a function, 
# this is what the source code for the abc module does


# Structural Typing With ABCs
class Sized(metaclass=abc.ABCMeta):
  __slots__ = ()

  @abc.abstractmethod
  def __len__(self):
    return 0
  
  @classmethod
  def __subclasshook__(cls, C):
    if cls is Sized:
      if any('__len__' in B.__dict__ for B in C.__mro__):
        return True
    return NotImplemented
