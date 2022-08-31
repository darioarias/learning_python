# even though python is not meant to be a functional programming language
# a functional coding style can be used to good extent, thanks to first-class functions, 
# pattern matching, and the support of packages like operator and functools, 
# which we cover in the next two sections.

# The operator Module
# Factorial implemented with reduce and an anonymous function
from functools import reduce

def factorial(n):
  return reduce(lambda a, b: a*b, range(1, n+1))

# the operator module provides function equivalents for dozens of operators 
# so you don’t have to code trivial functions like lambda a, b: a*b

# lets rewrite the example above
from operator import mul

def factorial(n):
  return reduce(mul, range(1, n + 1))

# Demo of itemgetter to sort a list of tuples
from operator import itemgetter
metro_data = [
  ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
  ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
  ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
  ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
  ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

for city in sorted(metro_data, key=itemgetter(2)):
  # print(city)
  pass

cc_name = itemgetter(1, 0)
for city in metro_data:
  # print(cc_name(city))
  pass

# Demo of attrgetter to process a namedtuple
from collections import namedtuple

Coordinate = namedtuple('Coordinate', ['lat', 'lon'])
Metropolis = namedtuple('Metropolis', ['name', 'cc', 'pop', 'coord'])
metro_areas = [Metropolis(name, cc, pop, Coordinate(lat, lon)) for name, cc, pop, (lat, lon) in metro_data]

from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):
  # print(name_lat(city)) if city.coord.lat <= 0 else None
  pass 

# Demo of methodcaller: second test shows the binding of extra arguments
from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
s_upper = upcase(s)  # THE TIME HAS COME
hyphenate = methodcaller('replace', ' ', '-')
s_dashed = hyphenate(s)  # The-time-has-come


# Freezing Arguments with functools.partial
from operator import mul
from functools import partial
triple = partial(mul, 3)
# print(triple(7))
# print(list(map(triple, range(1, 10))))

# also building normalizers
import unicodedata, functools
nfc = functools.partial(unicodedata.normalize, 'NFC')

s1 = 'café'
s2 = 'cafe\u0301'
s1 == s2  # False
s1, s2  # ('café', 'café')
nfc(s1) == nfc(s2)  # True


# Demo of partials applied to the function tag
def tag(name, *content, class_=None, **attrs):
  """Generate one of more HTML tags"""
  if class_ is not None: 
    attrs['class'] = class_
  
  attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
  attr_str = ''.join(attr_pairs)

  if content:
    elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
    return '\n'.join(elements)
  
  else:
    return f'<{name}{attr_str} />'

picture = partial(tag, 'img', class_='pic-frame')
# print(picture(src='wumpus.jpeg'))
