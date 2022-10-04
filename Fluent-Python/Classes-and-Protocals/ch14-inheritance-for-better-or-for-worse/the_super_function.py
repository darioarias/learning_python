# example of using the super function 
from typing import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):
  """Store items in the order they were last updated"""
  
  def __setitem__(self, key, value): 
    super().__setitem__(key, value) 
    self.move_to_end(key)

# In the preceding example, the following is happening 
# super().__setitem__ is used to call teh superclass method to insert or update key/value pair
# self.move_to_end is used to update teh key to last position

# NOTE: unlike other programming langauges, Python does not automatically call the constructor for the base class, get used to the following
class Car(object):
  def __init__(self, a, b) -> None:
    super().__init(a, b)

# you may also see
class NotRecommended(OrderedDict): 
  """This is a counter example!"""

  def __setitem__(self, key, value): 
    OrderedDict.__setitem__(self, key, value) 
    self.move_to_end(key)
# the preceding example is not recommended b/c it hardcodes the parent class


class LastUpdatedOrderedDict(OrderedDict):
  """This code works in Python 2 and Python 3"""
  
  def __setitem__(self, key, value) -> None:
    super(LastUpdatedOrderedDict, self).__setitem__(key, value)
    self.move_to_end(key)

  
# the preceding example works for both, python2 and python3. notice the variables passed to super. 
# type: the start of the saerch path for the superclass implementing the desired method.
# object_or_type: the object (for instance method calls) or class (for class method call) to be the receiver of the method call. 
## By default, it is self if the super() call happens in an instance method. 

