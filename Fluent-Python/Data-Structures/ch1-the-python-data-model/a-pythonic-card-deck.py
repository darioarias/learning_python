import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()

  def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

  def __len__(self):
    return len(self._cards)
  
  def __getitem__(self, position):
    return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
  rank_value = FrenchDeck.ranks.index(card.rank)
  print(f'bounds: 0 - {len(FrenchDeck.ranks)}, got {rank_value}')

  order_priority = rank_value * len(suit_values) + suit_values[card.suit]
  print(card, f'has priority {order_priority}')
  return order_priority


deck = FrenchDeck()
print(sorted(deck, key=spades_high))
# print(FrenchDeck.ranks)

# print(choice(deck))
# print(len(deck._cards))
# print(test._cards)
# for card in test._cards:
#   print(card)