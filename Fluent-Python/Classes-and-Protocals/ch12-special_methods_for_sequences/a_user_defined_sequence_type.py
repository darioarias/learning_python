
"""
Create a vector sequence that has the following
• Basic sequence protocol: __len__ and __getitem__
• Safe representation of instances with many items
• Proper slicing support, producing new Vector instances
• Aggregate hashing, taking into account every contained element value
• Custom formatting language extension
"""

from array import array
import reprlib
import math 


class Vector: 
  typecode = 'd'

  def __init__(self, components):
    self._components = array(self.typecode, components)
  
  def __iter__(self):
    return iter(self._components)
  
  def __repr__(self):
    components = reprlib.repr(self._components)
    components = components[components.find('['):-1]
    return f'Vector({components})'
  
  def __str__(self):
    return str(tuple(self))
  
  def __bytes__(self):
    return (bytes([ord(self.typecode)]) + bytes(self._components))
  
  def __eq__(self, other):
    return tuple(self) == tuple(other)
  
  def __abs__(self):
    return math.hypot(*self)
  
  def __bool__(self):
    return bool(abs(self))
  
  @classmethod
  def frombytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    return cls(memv)
  
  