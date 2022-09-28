# The Typed double Function

from abc import abstractmethod
from typing import NamedTuple, runtime_checkable
from fractions import Fraction
from typing_extensions import reveal_type


class Point(NamedTuple):
 x: int 
 y: int 

 def __mul__(self, factor):
  cls = self.__class__
  return cls(self.x * factor, self.y * factor)

def double(x):
  """X does not have a type, so anything implementing the __mul__ dunder will work here"""
  return x * 2

# example of showing how double works with different types that implement __mul__
# print(double(1.5))  # 3.0
# print(double('A'))  # AA
# print(double([10, 20, 30]))  # [10, 20, 30, 10, 20, 30]
# print(double(Point(2, 3)))  # Point(x=4, y=6)
# print(double(Fraction(2, 5)))  # 4/5


# trying to annotate this function will be a nightmare, 
# lets look at some possible ways to do it
from typing import TypeVar, Protocol

T = TypeVar('T')
class Repeatable(Protocol):
  def __mul__(self: T, repeat_count: int) -> T: ...

RT = TypeVar('RT', bound=Repeatable)

def double(x: RT) -> RT:
  return x * 2


# Runtime Checkable Static Protocols

@runtime_checkable
class SupportsComplex(Protocol):
  """An ABC with one abstract method __complex__."""
  __slots__ = ()

  @abstractmethod
  def __complex__(self) -> complex:
    pass 

# Using SupportsComplex at runtime
import numpy as np
c64 = np.complex64(3+4j)

# print(isinstance(c64, complex))  # False
# print(isinstance(c64, SupportsComplex))  # True
# c = complex(c64)
# print(isinstance(c, SupportsComplex))  # False
# print(isinstance(c, (complex, SupportsComplex)))  # True




# Supporting a Static Protocol
from typing import Any, Iterable, TYPE_CHECKING
import random

@runtime_checkable
class RandomPicker(Protocol):
  def pick(self) -> Any: ...

class SimplePicker:
  def __init__(self, items: Iterable) -> None:
    self._items = list(items)
    random.shuffle(self._items)

  def pick(self) -> Any:
    return self._items.pop()
  
def test_isinstance() -> None:
  popper: RandomPicker = SimplePicker([1])
  assert isinstance(popper, RandomPicker)

def test_item_type() -> None: 
  items = [1, 2]
  popper = SimplePicker(items)
  item = popper.pick()
  assert item in items 

  if TYPE_CHECKING:
    reveal_type(item)
  
  assert isinstance(item, int)