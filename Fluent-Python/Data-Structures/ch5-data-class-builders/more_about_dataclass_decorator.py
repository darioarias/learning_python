

from dataclasses import InitVar, dataclass, field
from typing import ClassVar

# @dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False) 
# here is the signature for the dataclass decorator

# since type hints are used to generate types, @data rejects complex hints

# @dataclass(frozen=True, order=True)
# class ClubMember:
#   name: str
#   guests: list = []  # ValueError: mutable default <class 'list'> for field guests is not allowed: use default_factory

# to fix the issue we can use the suggested solution
@dataclass(frozen=True, order=True)
class ClubMember:
  name: str
  guests: list = field(default_factory=list)  # if default is not set, all instances will share the same obj


# more precise definition for ClubMember
@dataclass(frozen=False, order=False)
class ClubMember(object):
  name: str
  guests: list[str] = field(default_factory=list)  # The list[str] syntax is a parameterized generic type: 
                                                   # since Python 3.9, the list built-in accepts that bracket notation to specify the type of the list items.

@dataclass(frozen=False, order=False)
class HackerClubMember(ClubMember):
  all_handles: ClassVar[set[str]] = set()
  handle: str = ''

  def __post_init__(self):
    cls = self.__class__
    if self.handle == '':
      self.handle = self.name.split()[0]

    if self.handle in cls.all_handles:
      msg = f'handle {self.handle!r} already exists.'
      raise ValueError(msg)
    cls.all_handles.add(self.handle)

hacker1 = HackerClubMember('Dario Arias')
hacker2 = HackerClubMember('Dario Arias', handle='d2')
hacker2.guests.append(hacker1)

# Initialization Variables That Are Not Fields
# Example from the dataclasses module documentation
# @dataclass
# class C:
#   i: int 
#   j: int = None
#   database: InitVar[DatabaseType] = None

#   def __post_init__(self, database):
#     if self.j is None and database is not None: 
#       self.j = database.lookup('j')
