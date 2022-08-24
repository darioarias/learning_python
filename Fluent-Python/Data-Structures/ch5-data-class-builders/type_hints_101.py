# type hints <==> type annotations : are ways to declare the expected type of 
# function arguments, return values, variables, and attributes.


# No Runtime Effect <> Type hints do not affect run time
# example;
import typing

class Coordinate(typing.NamedTuple):
  lat: float 
  lon: float 

trash = Coordinate('Ni!', None)
# print(trash)  # Coordinate(lat='Ni!', lon=None)  -- note that this should have not worked if types where checked at runtime



## Variable Annotation Syntax
# Basic syntax => var_name: some_type
name: str 

# We can also definde and assign: var_name: some_type = a_value
name: str = 'Pepe'


## The Meaning of Variable Annotations

# A plain class with type hints
class DemoPlainClass:
  a: int 
  b: float = 1.1
  c = 'pain'

# print(DemoPlainClass.__annotations__)  # {'a': <class 'int'>, 'b': <class 'float'>} -- note that c is just a plain old class attribute, not an annotation.
# print(DemoPlainClass.a)  # AttributeError: type object 'DemoPlainClass' has no attribute 'a'
# print(DemoPlainClass.b)  # 1.1
# print(DemoPlainClass.c)  # pain

## inspecting a typing.NamedTuple
class DemoPlainClass(typing.NamedTuple):
  a: int
  b: float = 1.1
  c = 'pain'

# print(DemoPlainClass.__annotations__)  # {'a': <class 'int'>, 'b': <class 'float'>}
# print(DemoPlainClass.a)  # _tuplegetter(0, 'Alias for field number 0')
# print(DemoPlainClass.b)  # _tuplegetter(1, 'Alias for field number 1')
# print(DemoPlainClass.c)  # pain
# print(DemoPlainClass.__doc__)  # Note that c is missing since it's just a class attribute

nt = DemoPlainClass(8)
# nt.a = 9  # AttributeError: can't set attribute
# nt.b = 7  # AttributeError: can't set attribute
# nt.c = 'obj'  # AttributeError: 'DemoPlainClass' object attribute 'c' is read-only.
# nt.z = 'new attr'  # AttributeError: 'DemoPlainClass' object has no attribute 'z'

## Inspecting a class decorated with dataclass
from dataclasses import dataclass

@dataclass(frozen=True)
class DemoDataClass:
  a: int
  b: float = 1.1
  c = 'pain'

# print(DemoDataClass.__annotations__)  # {'a': <class 'int'>, 'b': <class 'float'>}
# print(DemoDataClass.__doc__)   # DemoDataClass(a: int, b: float = 1.1)
# print(DemoDataClass.a)  # AttributeError: type object 'DemoDataClass' has no attribute 'a'
# print(DemoDataClass.b)  # 1.1
# print(DemoDataClass.c)  # pain

# dc = DemoDataClass(8)  
# dc.a = 9  # dataclasses.FrozenInstanceError: cannot assign to field 'a'
# dc.b = 7  # dataclasses.FrozenInstanceError: cannot assign to field 'b'
# dc.c = 'obj'  # dataclasses.FrozenInstanceError: cannot assign to field 'c'
# dc.z = 'new attr'  # dataclasses.FrozenInstanceError: cannot assign to field 'z'
