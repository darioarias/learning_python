
# refering the same object
charles = {'name': 'Charles L. Dodgson', 'born': 1832}

lewis = charles
# print(lewis is charles)  # True
# print(id(charles), id(lewis))  # 4365042112 4365042112 -- may differ, but the idea is that they are equal
lewis['balance'] = 950
# print(charles)  # {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
alex == charles  # True
alex is not charles  # True
# in the above example, lewis and charles are aliases, but alex is not. They are equal, since the __eq__ dunder checks for content equality
# An object’s identity never changes once it has been created; 
# you may think of it as the object’s address in memory. 
# The is operator compares the identity of two objects; 
# the id() function returns an integer representing its identity.

## Choosing between == and is
# Note that '==' cares more about the value, whereas 'is' cares about the identity
from dataclasses import dataclass
from re import T

@dataclass(frozen=True, order=True)
class Shoe:
  name: str
  size: float 
  brand: str

s1 = Shoe('Pegasus Turbo Next Nature', 8.5, 'Nike')
s2 = s1 
s3 = Shoe('Pegasus Turbo Next Nature', 8.5, 'Nike')

# print('is')
# print(s1 is s2)  # True
# print(s1 is s3)  # False

# print('==')
# print(s1 == s2)  # True
# print(s1 == s3)  # True

# We use 'is' to check against singleton or to check if a varibale is bound to something 
# for example
# x is None
# or
# x is not None

# we can often check bound-ness against a sentinal 
# END_OF_DATA = object()
# # ... many lines later
# def traverse(...):
#   # ... some more lines
#   if node is END_OF_DATA:
#     return 
#   # etc


## The Relative Immutability of Tuples
# as mentioned before, tuple's immutability only extends to the content it holds, 
# but if it hold something mutable, that item itself can change
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
t1 == t2  # True

id(t1[-1])  # 4505418880 <<-- not important beyond the fact they are the same
t1[-1].append(50)
t1  # (1, 2, [30, 40, 50]) -- note the change on the 3rd element of the tuple
id(t1[-1])  # 4505418880 <<-- not important beyond the fact they are the same
# note that the id for items in tuples wont change since the items are immutable

t1 == t2  # False


# A topic this brings up is, if I want to copy t1, should I just copy the content or the inner content when 
# an object is present?

# Copies Are Shallow by Default
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)  # I can also use slice to make copies
l2 = l1[:]  # same as the line above

l2  # [3, [55, 44], (7, 8, 9)]

# we expect that l1 and l2 are equivalent, but not the same object; thus...
l1 == l2  # True
l1 is l2  # False

# note that most copies by default are shallow copies
# which means that when an object is present, 
# it just copies the reference to the object for memory and time efficiency
# you should be able to see the issue with this lol

# continuing from above...,
l1.append(100)
l1[1].remove(55)
l1[1].insert(0, 66)

# print('l1', l1)  # [3, [66, 44], (7, 8, 9), 100]
# print('l2', l2)  # [3, [66, 44], (7, 8, 9)]
# note that the lists at index 1 are the same. That's becuase of the shallow copies which saves the reference

l2[1] += [33, 22]
l2[2] += (10, 11)
# print('l1:', l1)
# print('l2:', l2)


## Deep and Shallow Copies of Arbitrary Objects
# we can use the copy module
from copy import deepcopy, copy

class Bus(object):
  def __init__(self, passengers=None) -> None:
    if passengers is None:
      self.passengers = []
    else:
      self.passengers = list(passengers)
    
  def pick(self, name):
    self.passengers.append(name)
  
  def drop(self, name):
    self.passengers.remove(name)

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy(bus1)
bus3 = deepcopy(bus1)

# print((id(bus1), id(bus2), id(bus3)))  # (4473617712, 4473616944, 4475355872) <- the only fact that is relevant is the fact that they are different

bus1.drop('Bill')
# print(bus2.passengers)  # ['Alice', 'Claire', 'David'] - notice that since it's a shallow copy, b2 passengers changed
# print((id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)))  # (4505798656, 4505798656, 4505717632) -- note that 0 and 1 are the same here. 
bus3.passengers  # ['Alice', 'Bill', 'Claire', 'David']


# Note that cyclic references may cause an inifite loop. 
# Thanksfully deepcopy remembers the references it has copied so avoid loops
# Cyclic references: b refers to a, and then is appended to a; deepcopy still manages to copy a
a = [10, 20]
b = [a, 30]

a.append(b)
print(a)
c = deepcopy(a)
c  # [10, 20, [[...], 30]]