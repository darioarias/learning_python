

# Consider a simple class to represent a geographic coordinate pair
class Coordinate:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon
# writting the boiler is not ideal, especially when we have multiple values

moscow = Coordinate(55.76, 37.62)
# print(moscow)  # <__main__.Coordinate object at 0x10c737c10>  -- note that __repr__ inhereted from object is not very helpful, all we get is a memory address
location = Coordinate(55.76, 37.62)
# print(moscow == location)  # False  -- the __eq__ inhereted from object compares id, which is not helpful here
equals = ((location.lat, location.lon)==(moscow.lat, moscow.lon))
# print(equals)  # True  -- notice that I had to compared attributes explicitly

## overall, not very ideal

## Here is an alternative for the above
from collections import namedtuple
Coordinate = namedtuple('Coordinate', ['lat', 'lon'])

issubclass(Coordinate, tuple)  # True

moscow = Coordinate(55.76, 37.62)
# print(moscow)  # Coordinate(lat=55.76, lon=37.62) -- notice the useful __repr__
location = Coordinate(55.76, 37.62)
# print(moscow == location)  # True -- notice the useful __eq__

## Yet another way is using the new typing.NamedTuple
from typing import NamedTuple, get_type_hints
Coordinate = NamedTuple('Coordinate', [('lat', float), ('lon', float)])
# Coordinate = typing.NamedTuple('Coordinate', lat=float, lon=float)  # another way to write named tuples

issubclass(Coordinate, tuple)  # True
get_type_hints(Coordinate)  # {'lat': <class 'float'>, 'lon': <class 'float'>}
# print(t)


## updating the Coordinate class to use NamedTuple
class Coordinate(NamedTuple):
  lat: float 
  lon: float 

  def __str__(self) -> str:
    ns = 'N' if self.lat >= 0 else 'S'
    we = "E" if self.lon >= 0 else "W"
    return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
  

# the same can be accomplished by @dataclass decorator
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Coordinate:
  lat: float
  lon: float 

  def __str__(self) -> str:
    ns = 'N' if self.lat >= 0 else 'S'
    we = 'E' if self.lon >= 0 else 'W'
    return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
# note: that here we do not depend on inherentence to get the output to work

from inspect import get_annotations
# print(get_annotations(Coordinate))


## Exploring data classes features

# Mutable Instances
# A key difference between these class builders is that collections.namedtuple 
# and typing.NamedTuple build tuple subclasses, 
# therefore the instances are immutable. 
# By default, @dataclass produces mutable classes. 
# Use the arguemtn froozen to make it immutable

# Class statement syntax
# Only typing.NamedTuple and dataclass support the regular 
# class statement syntax, making it easier to 
# add methods and docstrings to the class you are creating.

# Construct dict
# Both named tuple variants provide an instance method (._asdict)
# to construct a dict object from the fields in a 
# data class instance. The dataclasses module provides 
# a function to do it: dataclasses.asdict.
# example;
# print(asdict(Coordinate(55.76, 37.62)))

# Get field names and default values
# All three class builders let you get the field names 
# and default values that may be con‐ figured for them.
# In named tuple classes, that metadata is in the ._fields 
# and ._fields_defaults class attributes.  
# You can get the same metadata from a data class decorated 
# class using the fields function from the dataclasses module.
# example;
# from dataclasses import fields
# print(fields(Coordinate(55.76, 37.62)))

# Get field types
# Classes defined with the help of typing.NamedTuple and @dataclass have a 
# mapping of field names to type the __annotations__ class attribute.
# print(get_type_hints(Coordinate))

# New instance with changes
# Given a named tuple instance x, the call x._replace(**kwargs) 
# returns a new instance with some attribute values replaced according 
# to the keyword arguments given. The dataclasses.replace(x, **kwargs) 
# module-level function does the same for an instance of a dataclass decorated class.

# New class at runtime
# to build class at runtime, you can use the default function call syntax of collections.namedtuple, 
# which is likewise supported by typing.NamedTuple. 
# The dataclasses module provides a make_dataclass function for the same purpose.



## Classic Named Tuples
# collections.namedtuple function is a factory that builds subclasses of tuple
# enhenced with filed names, a class name, and an informative __repr__.

# Using namedtuple
class Person(NamedTuple):
  name: str 
  last_name: str 
  age: int 
  isMarried: bool

  def __str__(self) -> str:
    return f'Hello, I\'m {self.name} {self.last_name} and I am {self.age} years old, also I am{" not" if self.isMarried else ""} single!'
 
City = namedtuple('City', ['name', 'country', 'population', 'location'])
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
# print(tokyo)  # City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722, 139.691667))
# print(tokyo.population)  # 36.933
# print(tokyo[1])  # JP
# print(City._fields)  # ('name', 'country', 'population', 'coordinates')
Coordinate = namedtuple('Coordinate', 'lat lon')
delhi_data = ('Delhi NCR', 'IN', 21.935, Coordinate(28.613889, 77.208889))
delhi = City._make(delhi_data)
# delhi = City(*delhi_data)

import json 
json_delhi = json.dumps(delhi._asdict())
# print(json_delhi)  # {"name": "Delhi NCR", "country": "IN", "population": 21.935, "location": [28.613889, 77.208889]}
# Note, if we need order dict, remember to use OrderedDict(x._asdict()).

# using default in data classes
Coordinate = namedtuple('Coordinate', 'lat lon reference', defaults=['WGS84'])
# print(Coordinate(0,0))  # Coordinate(lat=0, lon=0, reference='WGS84')

## adding methods to namedtuple Hack
# Hacking a namedtuple to Inject a Method
Person = namedtuple('Person', ['name', 'last_name', 'age'])

def say_hello(obj: Person): 
  return(f'Hello, I\'m {obj.name}')

Person.greet = say_hello
dario = Person('Pepe', 'Lopez', 42) 
dario.greet()  # Hello, I'm Pepe


## Typed Named Tuples
class Coordinate(NamedTuple):
  lat: float 
  lon: float 
  reference: str = 'WGS84'
  
  