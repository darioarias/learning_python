
# The only mode of parameter passing in Python is call by sharing.
# This means that each formal parameter of the function gets a copy of each reference in the arguments. 
# In other words, the parameters inside the function become aliases of the actual arguments.

from typing import MutableSequence


def f(a, b):
  a += b 
  return a 

x, y = 1, 2
# print(f(x, y), (x, y))  # 3, (1, 2)

a = [1, 2]
b = [3, 4]
# print(f(a, b), (a, b))  # [1, 2, 3, 4] ([1, 2, 3, 4], [3, 4])

t = (10, 20)
u = (30, 40)
# print(f(t, u), (t, u))  # (10, 20, 30, 40) ((10, 20), (30, 40))


## Mutable Types as Parameter Defaults: Bad Idea
class HauntedBus:
  """A bus model haunted by ghost passengers"""

  def __init__(self, passengers=[]) -> None:
    self.passengers = passengers
  
  def pick(self, name):
    self.passengers.append(name)
  
  def drop(self, name):
    self.passengers.remove(name)


bus1 = HauntedBus(['Alice', 'Bill'])
# print(bus1.passengers)
bus1.pick('Charlie')
# print(bus1.passengers)
bus1.drop('Alice')
# print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick('Carrie')
# print(bus2.passengers)

bus3 = HauntedBus()
bus3.pick('Dave')
# print(bus2.passengers)  # ['Carrie', 'Dave']

# notice that since the default value of HauntedBus is an alias to the emtpy list
# all instances of the HauntedBus will share the default list.

# Inspecting our HauntedBus class
def print_seq(sequence, title: str = "HauntedBus Attributes"):
  genexify = lambda sequence : (item for item in sequence)

  print(f'{title:^80}')
  genex = genexify(sequence)
  for attr in genex:
    print(f'|{attr:^20}|{next(genex, "None"):^20}|{next(genex, "None"):^20}|{next(genex, "None"):^20}|') 
  # learn more about formating at http://cissandbox.bentley.edu/sandbox/wp-content/uploads/2022-02-10-Documentation-on-f-strings-Updated.pdf

# print_seq(dir(HauntedBus))
# print(HauntedBus.__init__.__defaults__)  # shows the class defaults
# print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)  # True -- means that HauntedBus default is the same as bus2 data. 
#                                                                # (i.e HunterBus default and bus2.passengers are aliases of the same objects)


class TwilightBus(object):
  """A bus model that makes passengers vanish"""
  def __init__(self, passengers = None) -> None:
    if passengers is None:
      self.passengers = []
    else:
      # self.passengers = passengers   # The problem here is that the bus is aliasing the list that is passed to the constructor. 
                                       # Instead, it should keep its own passenger list.
      self.passengers = list(passengers)  # this way, the class has it's own copy
  
  def pick(self, name):
    self.passengers.append(name) 

  def drop(self, name):
    self.passengers.remove(name)

# Passengers disappear when dropped by a TwilightBus
basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')

basketball_team  # ['Sue', 'Maya', 'Diana'] -- wow Pat and Tina are gone from the team!
                 # this violates the “Principle of least astonishment” (POLA) a best practice of interface design
                 # with the new updated class, this is no longer an issue
                 