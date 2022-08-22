# function to check the built in attributes (i.e types, objs and function)
def print_built_ins():
  data = __builtins__.__dict__  # Stores all built-in types, objects, and functions
  for key in data:
    print(f'{key} - {data[key]}\n') 


# dict comprehensions

# 1. A dictcomp (dict comprehension) builds a dict instance by taking key:value pairs from any iterable.
from collections import namedtuple
Dial_Code = namedtuple('Dial_Code', ['Code', 'Country'])

dial_codes = [
  Dial_Code(880, 'Bangladesh'),
  Dial_Code(55, 'Brazil'),
  Dial_Code(86, 'China'),
  Dial_Code(91, 'India'),
  Dial_Code(62, 'Indonesia'),
  Dial_Code(81, 'Japan'),
  Dial_Code(234, 'Nigeria'),
  Dial_Code(92, 'Pakistan'),
  Dial_Code(7, 'Russia'),
  Dial_Code(1, 'United States')
]


country_dial = { country:code for code, country in dial_codes }

country_dial_upper = {code: country.upper() for country, code in country_dial.items() if code < 70}  # notice that code and country are switched, country is upper-cased and codes are filtered


# Unpacking Mappings
def dump(**kwargs):
  return kwargs

dump(**{'x': 1}, y=2, **{'z': 3})  # {'x': 1, 'y': 2, 'z': 3}
# notice I was able to use ** more than once

# using ** in literals
my_dict = {'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4, 'a':1}}
my_dict  # {'a': 1, 'x': 4, 'y': 2, 'z': 3}
# noticed that duplicates are allowed in the literal, but are over-written by later ones
# we can use this for merging dicts


friend1 = {
  'name': 'Pepe',
  'last_name': 'Lope',
  'age': 28
}

friend2 = {
  'name': 'Rick',
  'last_name': 'Mounts',
  'age': 24
}

friends = {
  'f1': {
    **friend1
  },
  'f2': {
    **friend2
  }
}  # {'f1': {'name': 'Pepe', 'last_name': 'Lope', 'age': 28}, 'f2': {'name': 'Rick', 'last_name': 'Mounts', 'age': 24}}

# Merging Mappings with | and |=
# | creates a new mapping
d1 = {'a': 1, 'b': 3}
d2 = {'a': 2, 'b': 4, 'c': 6}
# notice that keys can be the same, but they will be over-written
new_map = d1 | d2  # {'a': 2, 'b': 4, 'c': 6}

# as you can see, the keys are overwritten by the lastest value
new_map2 = d2 | d1  # {'a': 1, 'b': 3, 'c': 6}


# |= updates the lhs operand in place
d1 |= d2  
d1  # {'a': 2, 'b': 4, 'c': 6}

