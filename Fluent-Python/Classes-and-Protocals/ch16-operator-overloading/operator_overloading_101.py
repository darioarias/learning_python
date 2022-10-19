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


# Supporting unary operators
## Stick to the general rule of operators: always return a new object.
## In other words, do not modify the receiver (self),
## but create and return a new instance of a suitable type.


# Adding support for unary operators
import functools
import itertools
import math
import operator
import reprlib
from array import array


class Vector:
    typecode = "d"

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find("[") : -1]
        return f"Vector({components})"

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        # if len(self) != len(other):
        #   return False
        # for a, b in zip(other):
        #   if a != b:
        #     return False
        # return True
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        # return functools.reduce(operator.xor, hashes, 0)
        return functools.reduce(lambda a, b: a ^ b, hashes, 0)

    def __abs__(self):
        return math.hypot(*self)

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    # def __radd__(self, other):
    #     return self + other
    __radd__ = __add__

    def __mul__(self, scalar):
        try:
            factor = float(scalar)
        except TypeError:
            return NotImplemented
        return Vector(value * factor for value in self)

    # def __rmul__(self, scalar):
    #     return self * scalar
    __rmul__ = __mul__

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]

    __match_args__ = ("x", "y", "z", "t")

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f"{cls.__name__!r} object has no attribute {name!r}"
        raise AttributeError(msg)

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match_args__:
                error = "readonly attribute {attr_name!r}"
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ""
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def angle(self, n):
        r = math.hypot(*self[n:])
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=""):
        if fmt_spec.endswith("h"):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = "<{}>"
        else:
            coords = self
            outer_fmt = "({})"
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(", ".join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


v = Vector([1, 2])
v2 = Vector([4, 3])
print(v * v)
