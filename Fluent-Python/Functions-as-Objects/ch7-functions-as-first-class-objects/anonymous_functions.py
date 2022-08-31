# Lamdba 'functions' are meant to be anonymous
#  the simple syntax of Python limits the body of lambda functions to be pure expressions. 
# In other words, the body cannot contain other Python statements such as while, try, etc. 
# Assignment with = is also a statement, so it cannot occur in a lambda. 
# The new assignment expression syntax using := can be used—but if you need it, 
# your lambda is probably too complicated and hard to read, and it should be refactored into a regular function using def.

# The best use of anonymous functions is in the context of an argument list for a higher-order function.
# for example;
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=lambda word : word[::-1])  # ['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']

