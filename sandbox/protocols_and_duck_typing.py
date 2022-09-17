# In the context of object-oriented programming, 
# a protocol is an informal interface, 
# defined only in documentation and not in code

import collections
from reprlib import aRepr, repr

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self) -> None:
    self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self, position):
    return self._cards[position]
  
  def __repr__(self) -> str:
    aRepr.maxlist = 2
    return f"{repr(self._cards)}"

# An experienced Python coder will look at it and understand that it is a sequence, 
# even if it subclasses object. We say it is a sequence because it behaves like one, and that is what matters.


seq = FrenchDeck()
print(seq)