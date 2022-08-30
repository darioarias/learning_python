
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