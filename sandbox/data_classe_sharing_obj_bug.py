from dataclasses import dataclass, field

# The folllowing is a wrapper around a list (so that dataclass would not flag it and reprot an exception)
class Guests(object):
  def __init__(self, *people) -> None:
    self.list = []

    for person in people:
      self.push(person)

  def push(self, person):
    self.list.append(person)
  
  def __repr__(self) -> str:
    return f'{self.list!r}'

# create a data class using our newly crated class
@dataclass(frozen=True, order=False)
class ClubMember(object):
  name: str 
  guests: Guests = Guests()

m = ClubMember('Jane')
m2 = ClubMember('John')
m.guests.push('Larry')
# print(m, m2)  # ClubMember(name='Jane', guests=['Larry']) ClubMember(name='John', guests=['Larry'])
# note that m and m2 share the same guest object. This is not what we want

@dataclass(frozen=True, order=False)
class ClubMember(object):
  name: str
  guests: Guests = field(default_factory=Guests)

m = ClubMember('Jane')
m2 = ClubMember('John')
m.guests.push('Larry')

# print(m, m2)  # ClubMember(name='Jane', guests=['Larry']) ClubMember(name='John', guests=[])
# notice that with the new change, the objects are no longer shared