# Operator Overloading 101
## Operator overloading allows userdefined objects to
## interoperate with infix operators such as + and |, or unary operators like - and ~.


# Unary Operators

# -, implemented by __neg__
# Arithmetic unary negation. If x is -2 then -x == 2.
x = -2
-x  # 2


# +, implemented by __pos__
# Arithmetic unary plus. Usually x == +x, but there are a few cases when that’s not true.
x = 10
x == +x  # True

from collections import Counter
from email import iterators

ctr = Counter("racecar")  # Counter({'r': 2, 'a': 2, 'c': 2, 'e': 1})
ctr["e"] = 0
ctr["r"] = -1
ctr  # Counter({'a': 2, 'c': 2, 'e': 0, 'r': -1})
+ctr  # Counter({'a': 2, 'c': 2})
ctr == +ctr  # False
# notice that +Counter returns all tallies greather than 0


# ~, implemented by __invert__
# Bitwise not, or bitwise inverse of an integer, defined as ~x == -(x+1).
# If x is 2 then ~x == -3.

# abs, implemented by __abs__
# Arithmetic abs operator. if x = -2 then abs(x) == 2
x = -2
abs(x)
