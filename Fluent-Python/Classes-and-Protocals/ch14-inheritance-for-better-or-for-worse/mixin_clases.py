
# What is a mixin?
# A mixin class is designed to be subclassed together with 
# at least one other class in a multiple inheritance arrangement. 
# A mixin is not supposed to be the only base class of a concrete class, 
# because it does not provide all the functionality for a concrete object, 
# but only adds or customizes the behavior of child or sibling classes.



# Case-Insensitive Mappings
import collections

def _upper(key):
  try: 
    return key.upper()
  except AttributeError:
    return key

class UpperCaseMixin:
  def __setitem__(self, key, item):
    super().__setitem__(_upper(key), item)
  
  def __getitem__(self, key):
    return super().__getitem__(_upper(key))
  
  def get(self, key, default=None):
    return super().get(_upper(key), default)
  
  def __contains__(self, key):
    return super().__contains__(_upper(key))
  
class UpperDict(UpperCaseMixin, collections.UserDict):
  pass 

class UpperCounter(UpperCaseMixin, collections.Counter):
  """Specialized 'Counter' that uppercases string keys"""
  