from .Flies import Fly

class Animal(object):
  flies = Fly()
  def __init__(self, flies: Fly) -> None:
    self.flies = flies

  


    

