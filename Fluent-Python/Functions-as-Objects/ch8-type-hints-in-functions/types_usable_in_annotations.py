# all the major annotations we can use
## typing.Any
## Simple types and classes
## typing.Optional and typing.Union
## Generic collections, including tuples and mappings
## Abstract base classes
## Generic iterables
## Parameterized generics and TypeVar
## typing.Protocols—the key to static duck typing
## typing.Callable
## typing.NoReturn—a good way to end this list


# The Any Type
# when the type checker sees something without a type, it assumes any, for example
from typing import Any, Sequence


def double(x):
  pass 

def double(x: Any):
  pass

# note that since every type is a subtype-of object, this would also work
def double(x: object) -> object:
  pass

# but type checkers will reject it becuase object does not implement __mul__

# Optional and Union Types
from typing import Optional

def show_count_none(count: int, singular: str, plural: Optional[str] = None) -> str: # The construct Optional[str] is actually a shortcut for Union[str, None], which means the type of plural may be str or None.
  pass 

def show_count_new_syntax(count: int, singular: str, plural: str | int = None):
  pass 

# for index, item in enumerate(["one", "two", "three"]):
#   print(f"at {index}, item-{item}")
#   for chr in item:
#     print(ord(chr))

# example that may return more than one thing
from typing import Union

# def parse_token(token: str) -> Union[str, float]:
#   try:
#     return float(token)
#   except ValueError:
#     return token


# Generic Collections

def tokenize(text: str) -> list[str]:
  return text.upper().split()


def int_list_parser(record: list[int]) -> list[str]:
  token = []
  for index, value in enumerate(record):
    token.append(f'{index},{value}')
  return token

# print(int_list_parser([10, 12, 41]))


# Tuple Types
#There are three ways to annotate tuple types:
## Tuples as records
## Tuples as records with named fields
## Tuples as immutable sequences

# Tuples as Records
# from geolib import geohash as gh
# PRECISION = 9

# def geohash(lat_lon: tuple[float, float]) -> str:
#   return gh.encode(*lat_lon, PRECISION)

# Tuples as records with named fields
from typing import NamedTuple

class Coordinate(NamedTuple):
  lat: float 
  lon: float 

  def __repr__(self) -> str:
    return f'{self.lat}, {self.lon}'

def dig_move(lat_lon: Coordinate) -> Coordinate:
  return Coordinate(lat_lon.lat + (lat_lon.lat/2), lat_lon.lon - (lat_lon.lon/2))

nyc = Coordinate(40.730610, -73.935242)
# print(dig_move(nyc))


# Tuples as immutable sequences
def columnize(sequence: Sequence[str], num_columns: int = 0) -> list[tuple[str, ...]]:
  pass 


#Generic Mappings
import sys 
import re 
import unicodedata
from collections.abc import Iterator

RE_WORD = re.compile(r'\w+')
STOP_CODE = sys.maxunicode + 1

def tokenize(text:str) -> Iterator(str):
  """Return iterable of uppercased words"""
  for match in RE_WORD.finditer(text):
    yield match.group().upper()

def name_index(start: int = 32, end: int = STOP_CODE) -> dict[str, set[str]]:
  index: dict[str, set[str]] = {}
  for char in (chr(i) for i in range(start, end)):
    if name := unicodedata.name(char, ''):
      for word in tokenize(name):
        index.setdefault(word, set()).add(char)
  return index

# Abstract Base Classes
from collections.abc import Mapping
def name2hex(name: str, color_map: Mapping[str, int]) -> str:
  pass 

def name2hex(name: str, color_map: dict[str, int]) -> str:  # notice that color now must be a dict (i.e defaultDict or OrderedDict)
  pass 



# The fall of the numeric tower
# not supported by typechecker, look into it


# Iterable
from collections.abc import Iterable
from typing import TypeAlias
# FromTo = tuple[str, str]
FromTo: TypeAlias = tuple[str, str]
def zip_replace(text: str, changes: Iterable[FromTo]):
  for from_, to in changes: 
    text = text.replace(from_, to)
  return text


# Parameterized Generics and TypeVar
from collections.abc import Sequence
from random import shuffle
from typing import TypeVar

T = TypeVar('T')

def sample(population: Sequence[T], size: int) -> list[T]:
  if size < 1:
    raise ValueError('Size must be >= 1')
  result = list(population)
  shuffle(result)
  return result[:size]


from collections import Counter
from collections.abc import Iterable

def mode(data: Iterable[float]) -> float:
  pairs = Counter(data).most_common(1)
  if len(pairs) == 0:
    raise ValueError('No mode for empty data')
  return pairs[0][0]

## Restricted TypeVar
from decimal import Decimal
from fractions import Fraction
from typing import TypeVar
from collections.abc import Iterable

NumberT = TypeVar('NumberT', float, Decimal, Fraction)
def mode(data: Iterable[NumberT]) -> NumberT:
  pass

## Bounded TypeVar
from collections.abc import Iterable, Hashable

def mode(data: Iterable[Hashable]) -> Hashable:
  pass 
