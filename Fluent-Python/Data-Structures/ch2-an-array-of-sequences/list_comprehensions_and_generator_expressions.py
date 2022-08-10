
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