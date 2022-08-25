

# Simple Class Patterns
# case [str(name), _, _, (float(lat), float(lon))]:
# The above matches a sequence where the first item is 
# an instance of str and the last item is a tuple containing 
# two float

# from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass, field

# Coordinate = namedtuple('Coordinate', [('lat', float), ('lon', float)])
Coordinate = NamedTuple('Coordinate', [('lat', float), ('lon', float)])
City = NamedTuple(
  'City', 
  [('name', str), ('population', int), ('language', str), ('cords', Coordinate)]
)

# @dataclass(frozen=True, order=True)
# class City(object):
#   name: str
#   population: int = 0
#   language: str = 'ENG'
#   cords: Coordinate = field(default_factory=Coordinate)

def check_lang(lang: str):
  print(lang)
  return False

def filter_by_lang(*cities: City, lang: str): # "ENG"
  for city in (city for city in cities if city.language == lang):
    print(city)
  
  # for city in cities:
  #   match city:
  #     case (str(name), _, _, (float(lat), float(lon))):
  #       print(city)
  #     case _:
  #       pass

  # print((city for city in cities if city.language == lang))


nyc = City('New York City', 0, 'ENG', cords=(10.0, 0.0))
sf = City('San Francisco', 0, 'ENG', (0.0, 0.0))
p = City('Paris', 0, 'FRA', (0.0, 0.0))

# print(*nyc, sep='\t')
# for f in t:
#   print(f, type(f))
filter_by_lang(nyc, sf, p, lang='FRA')
# print(nyc[0])