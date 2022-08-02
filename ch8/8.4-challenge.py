from math import floor
"""
to n that divides n with no remainder.
For example, 3 is a factor of 12 because 12 divided by 3 is 4, 
with no remainder. However, 5 is not a factor of 12 because 5 goes into 12 twice with a remainder of 2.
"""

def find_factors(n: int): 
  # for i in range(1, floor(n / 2) + 1):
  for i in range(2, floor(n/2) + 1):
    if n % i == 0: 
      print(f"{i} is a factor of {n}")

find_factors(100000000)