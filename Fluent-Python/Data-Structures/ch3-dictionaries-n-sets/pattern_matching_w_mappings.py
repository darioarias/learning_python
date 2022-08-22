



# using match/case to extract data from dict (i.e api json responses)

#get_creators() extracts names of creators from media records
def get_creators(record: dict) -> list:
  match record:
    case {'type': 'book', 'api': 2, 'authors': [*names]}:
      return names
    case {'type': 'book', 'api': 1, 'author': name}:
      return [name]
    case {'type': 'book'}:
      raise ValueError(f"Invalid 'book' record: {record!r}")
    case {'type': 'movie', 'director': name}:
      return name
    case _:
      raise ValueError(f"Invalid record: {record!r}")

b1 = dict(api=1, author='Douglas Hofstadter', type='book', title='Godel, Escher, Bach')
get_creators(b1)  # ['Douglas Hofstadter']

from collections import OrderedDict

b2 = OrderedDict(api=2, type='book', title='Python in a Nutshell', authors='Martelli Ravenscroft Holden'.split())
get_creators(b2)  # ['Martelli', 'Ravenscroft', 'Holden']

# get_creators({'type': 'book', 'pages': 770})  # will raise a ValueError


# unlike lists we do not use *_ or **_. But if we want to package data into one variable we can do the following

food = dict(category='ice cream', flavor='vanilla', cost=199)
def grab_food_details(food: dict):
  match food: 
    case {'category': 'ice cream', **details}:
      print(f'Ice Cream Details: {details}')


# grab_food_details(food)