from .Animal import Animal
from .Flies import CantFly, CanFly

class Dog(Animal):
  def __init__(self, name) -> None:
    self.name = name 
    self.flies = CantFly()

class Duck(Animal):
  def __init__(self, name) -> None:
    self.name = name 
    self.flies = CanFly()