from typing import NamedTuple, Sequence, Optional

class Color(NamedTuple):
  red: int 
  green: int
  blue: int 
  opacity: Optional['float'] = 1.0

class ColorFactory(object):
  colors: Sequence[Color]

  def __init__(self) -> None:
    self.colors = {}

  def getColor(self, color: tuple):
    tempColor = Color(*color)
    if tempColor in self.colors:
      return self.colors[tempColor]
    self.colors[tempColor] = tempColor
    return self.colors[tempColor]
  
  def __repr__(self) -> str:
    return f'Factory({len(self.colors)})<{self.colors!r}>'