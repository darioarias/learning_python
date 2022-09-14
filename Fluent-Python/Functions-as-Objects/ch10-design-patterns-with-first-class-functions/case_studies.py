

# Classic Stategy 
#  UML class diagram for order discount processing implemented with the Strategy design pattern.
#               |-----------—|             |-----------—|   
#               |    ORDER   |             | Promotion  |   (Strategy)
#               | total()    | ----------> | discount() | 
#               | due()      |             |-----------—|
#               |-----------—|                  ^
#                  (context)                    |
#                _______________________________|____________________________                                                           
#               |                               |                            |                                            
#      |—————-----------—|            |—————-----------—|           |---------——————--—|                                                     
#      |  FidelityPromo  |            | BuilkItemPromo  |           | LargeOrderPromo  |                                                   
#      | discount()      |            | discount()      |           | discount()       |                                                   
#      |—————-----------—|            |—————-----------—|           |-------——————----—|         
#                      \                       |                         /                                      
#                          \                   |                    /                                          
#                              \               |               /                                              
#                                   \          |         /                                                   
#                                    (Concrete Strategies)                                                             
#                                                                                            
#                                                                                            
#                                                                                            
# Strategy Design pattern
# Define a family of algorithms, encapsulate each one, and make them interchangeable.
# Strategy lets the algorithm vary independently from clients that use it.

# Implementation of the Order class with pluggable discount strategies
from abc import ABC, abstractmethod
from collections.abc import Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import NamedTuple, Optional

class Customer(NamedTuple):
  name: str 
  fidelity: int 

class LineItem(NamedTuple):
  product: str 
  quality: int 
  price: Decimal

  def total(self) -> Decimal:
    return self.price * self.quality

class Order(NamedTuple):
  customer: Customer
  cart: Sequence[LineItem]
  promotion: Optional['Promotion'] = None
  def total(self) -> Decimal:
    totals = (item.total() for item in self.cart)
    return sum(totals, start=Decimal(0))
  
  def due(self) -> Decimal:
    if self.promotion is None:
      discount = Decimal(0)
    else:
      discount = self.promotion.discount(self)
    
    return self.total() - discount
  
  def __repr__(self) -> str:
    return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'
  
class Promotion(ABC):
  @abstractmethod
  def discount(self, order: Order) -> Decimal:
    """Return discount as a positive dollar amount"""

class FidelityPromo(Promotion):
  """5% discount for customers with 1000 or more fidelity points"""
  def discount(self, order: Order) -> Decimal:
    rate = Decimal('0.05')
    if order.customer.fidelity >= 1000:
      return order.total() * rate
    return Decimal(0)

class BulkItemPromo(Promotion):
  """10% discount for each LineItem with 20 or more units"""

  def discount(self, order: Order) -> Decimal:
    discount = Decimal(0)
    for item in order.cart:
      if item.quality >= 10:
        discount += item.total() * Decimal('0.1')
    return discount


class LargeOrderPromo(Promotion):
  """7% discount for orders with 10 or more distinct items"""
  def discount(self, order: Order) -> Decimal:
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
      return order.total() * Decimal('0.07')
    return Decimal(0)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = (
  LineItem('Banana', 4, Decimal('0.5')),
  LineItem('Apple', 10, Decimal('1.5')),
  LineItem('Watermelon', 5, Decimal('5'))
)

banana_cart = (
  LineItem('banana', 30, Decimal('.5')),
  LineItem('apple', 10, Decimal('1.5'))
)

long_cart = tuple(
  LineItem(str(sku), 1, Decimal(1)) for sku in range(10)
)

# for order in (
#   Order(joe, cart, FidelityPromo()), 
#   Order(ann, cart, FidelityPromo()),
#   Order(joe, banana_cart, BulkItemPromo()),
#   Order(joe, long_cart, LargeOrderPromo()),
#   Order(joe, cart, LargeOrderPromo())
#   ):
#   print(order)


# Function-Oriented Strategy
  # the following have been imported already 
  # from collections.abc import Sequence
  # from dataclasses import dataclass
  # from decimal import Decimal
  # from typing import Optional 
from typing import Callable, NamedTuple

# Customer has been implemented above
# LineItem has been implemented above

@dataclass(frozen=True)
class Order:
  customer: Customer
  cart: Sequence[LineItem]
  promotion: Optional[Callable[['Order'], Decimal]] = None

  def total(self) -> Decimal:
    totals = (item.total() for item in self.cart)
    return sum(totals, start=Decimal(0))

  def due(self) -> Decimal:
    if self.promotion is None:
      discount = Decimal(0)
    else: 
      discount = self.promotion(self)
    return self.total() - discount
  
  def __repr__(self) -> str:
    return f'<Order total: {self.total():.2f}, due: {self.due():.2f}>'

def fidelity_promo(order: Order) -> Decimal:
  """5% discount for customers with 1000 or more fidelity points"""
  if order.customer.fidelity >= 1000:
    return order.total() * Decimal('0.05')
  return Decimal(0)

def bulk_item_promo(order: Order) -> Decimal:
  """10% discount for each LineItem with 20 or more units"""
  discount = Decimal(0)
  for item in order.cart:
    if item.quality >= 20:
      discount += item.total() * Decimal('0.1')
  return discount

def large_order_promo(order: Order) -> Decimal:
  """7% discount for orders with 10 or more distinct items"""
  distinct_items = {item.product for item in order.cart}
  if len(distinct_items) >= 10:
    return order.total() * Decimal('0.07')
  return Decimal(0)


# Choosing the Best Strategy: Simple Approach
# Example 10-6. best_promo finds the maximum discount iterating over a list of functions

promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order: Order) -> Decimal:
  """Compute the best discount available"""
  return max(promo(order) for promo in promos)



# for order in (
#   Order(joe, cart, best_promo), 
#   Order(ann, cart, best_promo),
#   Order(joe, banana_cart, best_promo),
#   Order(joe, long_cart, best_promo),
#   Order(joe, cart, best_promo)
#   ):
#   print(order)


# Finding Strategies in a Module
# since globals() include a dict containing all of the functions in the global scope, 
# we can use it to make sure that we apply all prmo functions

promos = [promo for name, promo in globals().items() if name.endswith('_promo') and name != 'best_promo']
def best_promo(order: Order):
  return max(promo(order) for promo in promos)  # makes sure that all promos are applied


# Decorator-Enhanced Strategy Pattern
# just use a decorator which saves the function in a list
