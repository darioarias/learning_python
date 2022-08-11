""" ABOUT LIST COMPREHENSION """

symbols = '$¢£¥€¤'

# build a list of Unicode code points from a string without list comprehension
codes_normal = []
for symbol in symbols:
  codes_normal.append(ord(symbol))

# build a list of unicode code points from a string using list comprehension
codes_listcomps = [ord(symbol) for symbol in symbols]
assert(codes_normal == codes_listcomps)  # assumes, and tests, that both lists are the same


# Cartesian product using a list comprehension
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]


assert(len(colors) * len(sizes) == len(tshirts))  # when doing cartesian product, the result should be len(lhs) * len(rhs)


""" ABOUT GENERATOR EXPRESSIONS """
import array
from nis import match
symbols = '$¢£¥€¤'  # redefinition so this section does not depend on the last one

ord_tuple = tuple(ord(symbol) for symbol in symbols)  # creating a tuple using Generator Expressions

ord_arr = array.array('I', [ord(symbol) for symbol in symbols])  # creating array using Generator Expressions


ord_arr = array.array('I', [ord(symbol) for symbol in symbols])  # creating array using Generator Expressions

# We do not have to pass in a list
ord_arr2 = array.array('I', (ord(symbol) for symbol in symbols))  # creating array using Generator Expressions




# Cartesian product in a generator expression
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in (f'{color} {size}' for color in colors for size in sizes): # note that that the genexp feeds one item at the time
  # print(tshirt)
  pass


# Tuples as Records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32_450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in traveler_ids:
  # print('%s/%s' % passport)
  pass

  
for country, _ in traveler_ids:
  # print(country)
  pass


# Tuples as Immutable Lists
a = (10, 'alpha', [1, 2])
b = (10, 'alpha', [1, 2])

assert(a == b)  # checks to see if both tuples are equals

b[-1].append(99)

assert(a != b)  # the tuples should no longer be equal since we modified the list in the tuple

def fixed(o):
  try:
    hash(o)
  except TypeError:
    return False
  return True

fixed_tuple = (10, 'alpha', (1, 2))
mutable_tuple = (10, 'alpha', [1, 2])

assert(fixed(fixed_tuple))
assert(not fixed(mutable_tuple))

# Unpacking Sequences and Iterables
from collections import namedtuple

User = namedtuple('User', ['first_name', 'last_name', 'email', 'age'])

pepe = User('Pepe', 'Lope', 'pepelope@mail.com', 36)

name, *data = pepe  # grabbing the first piece of data then packing the rest into 'data'
*data2, age = pepe  # packing all of the data into 'data2' and grabing age


last_name, first_name, *_ = pepe  # notice that I grab the wrong data. last_name is first_name and vices versa

first_name, last_name = last_name, first_name  # I can use unpacking to swap values without using a temp variable


# Unpacking with * in Function Calls and Sequence Literals

def func(a, b, c, d, *rest):
  return a, b, c, d, rest 

result = func(*[1, 2], 3, *range(4, 7))  # (1, 2, 3, 4, (5, 6)) - notice that the list got unpacked, '3' was used normally, 
                                         # range was unpacked, 4 passed as 'd' and the 5-(7-1)-6 were packed



# using star while defining list, tuple, or set literals
unpacked_data = *range(5),
unpacked_list = [*range(5),] + [*(5, 6)]
unpacked_set = {*range(5), *(5, 6)}


# Nested Unpacking | Unpacking nested tuples to access the longitude
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

# print(f'{"City":16} | {"latitude":>9} | {"longitude":>9}')
for city, _, _, (lat, lon) in metro_areas:
  # print(f'{city:16} | {lat:9.4f} | {lon:9.4f}')
  pass


# Pattern Matching with Sequences
def http_response(status):
  match status:
    case 200:
      return "Ok"
    case 400:
      return "Bad Request"


#  Destructuring nested tuples
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def display_(metro_areas):
  print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
  for record in metro_areas:
    match record:
      case [name, _, _, (lat, lon)] if lon <= 0:
        print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')


# matching and rename using 'as'
for record in metro_areas:
  match record:
    case [_, country, _, (_, _) as cords]:
      # print(f'country - {country}. Lat-lon: {cords}')
      pass

# matching specific types
for record in metro_areas:
  match record:
    case [_, str(country), _, (float(lat), float(lon)) as cords] as matched_record if lon <= 0: # We use specific type to match, we also name each match so we can use it later
      # print(matched_record)
      pass

# matching and binding un-necesary data
for record in metro_areas:
  match record:
    case [str(name), *_, (float(lat), float(lon)) as cords] as matched_record if lon <= 0:
      # print(f'city: {name}, lat: {lat}, lon: {lon} -- cords: {cords}')
      pass

