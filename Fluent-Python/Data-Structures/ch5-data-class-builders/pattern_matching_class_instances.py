

# Simple Class Patterns
# case [str(name), _, _, (float(lat), float(lon))]:
# The above matches a sequence where the first item is 
# an instance of str and the last item is a tuple containing 
# two float


# Keyword Class Patterns
import typing
from unittest import result

class City(typing.NamedTuple):
  contient: str
  name: str 
  country: str


cities = [
  City('Asia', 'Tokyo', 'JP'),
  City('Asia', 'Delhi', 'IN'),
  City('North America', 'Mexico City', 'MX'),
  City('North America', 'New York', 'US'),
  City('South America', 'São Paulo', 'BR')
]

def match_asian_cities(cities):
  # result = []
  for city in cities:
    match city:
      case City(contient='Asia'):
        # result.append(city)
        yield city
  # return result

def match_asian_cities_values(cities):
  results = []
  for city in cities:
    match city:
      case City(contient='Asia', country=cc, name=nn):
        results.append((cc, nn))
  return results


# print(match_asian_cities_values(cities))
# for city in match_asian_cities(cities):
#   print(city)


## Positional Class Patterns

def match_asian_cities_pos(cities):
  results = []
  for city in cities:
    match city:
      case City('Asia'):
        results.append(city)
  return results


# def test(*cities, attr):
#   for city in cities:
#     match city:
#       case City(City.__match_args__[0] = 'Asia'):
#         print(city)


# what makes match work is the present of __match_args__
print(City.__match_args__)
