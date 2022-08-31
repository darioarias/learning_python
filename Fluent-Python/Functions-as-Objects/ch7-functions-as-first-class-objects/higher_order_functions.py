
# A function that takes a function as an argument or returns a function as the result is a higher-order function

# for example; Sorting a list of words by length
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
# print(sorted(fruits, key=len))  # ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']

#sorting the words using the last letter
# print(sorted(fruits, key=lambda word: word[::-1]))  # using lambda

def reverse(word):
  return word[::-1]
# print(sorted(fruits, key=reverse))  # using explicit defined function


# some of the best known higher-order functions are map, filter, reduce, and apply
# note that apply got deprecated in Python 2.3 and removed in Python 3
# you can write fn(*args, **kwargs) instead of apply(fn, args, kwargs).

def factorial(n):
  return 1 if n < 2 else n * factorial(n - 1)

## Modern replacements for map, filter, and reduce
# list comps and dict comps are more reliable 

# Lists of factorials produced with map and filter compared to alternatives coded as list comprehensions
l1 = list(map(factorial, range(6)))
l2 = [factorial(n) for n in range(6)]

l3 = list(map(factorial, filter(lambda n: n % 2, range(6))))
l4 = [factorial(n) for n in range(6) if n % 2]

## note that in both cases listcomps simplied everything
for l in [l1, l2, l3, l4]:
  # print(l)
  pass


# the reduce function got demoted to functools
from functools import reduce
from operator import add

# print(reduce(add, range(100)))
# print(sum(range(100)))

# other built-ins are;
# all(iterable)
## Returns True if there are no falsy elements in the iterable; all([]) returns True.
# any(iterable)
## Returns True if any element of the iterable is truthy; any([]) returns False.

