# Python Digs Sequences

# a deck as a sequence of cards
import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self) -> None:
    self._cards = [
      Card(rank, suit) 
      for suit in self.suits 
      for rank in self.ranks 
    ]

  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self, position):
    return self._cards[position]
# Note: this class works by providing __getitem__ and __len__ which makes it behave like a sequence 
# Note: the class above does not support shuffle because it does not 
# implement mutable sequence method __setitem__
# we can do that at runtime, hence monkey Patching

# Monkey Patching: Implementing a protocol at runtime
def set_card(deck, position, card):
  deck._cards[position] = card

FrenchDeck.__setitem__ = set_card

from random import shuffle
deck = FrenchDeck()
shuffle(deck)

for card in deck:
  # print(card)
  pass  # shows that deck is different everytime

# Defensive Programming and "Fail Fast"

# the idea here is to fail fast
from typing import Sequence  
class ListWrapper(object):
  def __init__(self, items: Sequence[str]) -> None:
    self._items = list(items)  # first thing, it will create a runtime error

  def to_features(self, items: str | Sequence[str]):
    # assume that a string was passed
    try: 
      items = items.replace(', ', ' ').split()
    except AttributeError:
      pass # if failed, assume a an iterable was passed

    self._items = items
    return self

  def __repr__(self) -> str:
    return f"{self._items!r}"