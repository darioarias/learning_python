# functions are nothing but objects in python...
# In the following exmaple, we create a function, call it, 
# read its __doc__ attribute, and check that the function object 
# itself is an instance of the function class.

def factorial(n):
  """returns n"""
  return 1 if n < 2 else n * factorial(n - 1)

# print(factorial(4))  # 24
# print(factorial.__doc__)  # returns n
# print(type(factorial))  # <class 'function'>
# print(help(factorial))

# we can also re-assign factorial
fact = factorial
# print(fact)  # <function factorial at 0x...>
# print(fact(5))  # 120
# print(map(factorial, range(6)))  # <map object at 0x...>
# print(list(map(factorial, range(6))))  # [1, 1, 2, 6, 24, 120]

