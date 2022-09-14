
from typing import NamedTuple
from .RectangleFactory import ColorFactory

class Position(NamedTuple):
  x: int 
  y: int

class Rectangle(object):
  factory = ColorFactory()
  
  def __init__(self, color: tuple, pos: tuple) -> None:
    self.color = self.factory.getColor(color)
    self.position = Position(*pos)
  
  def __repr__(self) -> str:
    name = self.__class__.__name__
    return f'{name}({self.color!r}, {self.position!r})'