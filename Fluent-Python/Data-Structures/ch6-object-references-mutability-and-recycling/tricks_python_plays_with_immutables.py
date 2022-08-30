# for a tuple t, t[:] does not make a copy, but returns a reference to the same object. 
# You also get a reference to the same tuple if you write tuple(t).

# example
t1 = (1, 2, 3)
t2 = tuple(t1)

t2 is t1  # True

t3 = t1[:]

t3 is t1  # True


# The same behavior exits for str, bytes, and frozenset. Though frozenset is not a sequence
s1 = 'ABC'
s2 = 'ABC'
s2 is s1  # True
## The sharing of string literals is an optimization technique called interning -- not every string or int is interned 
