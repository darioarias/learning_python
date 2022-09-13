# DECORATORS 101
## A decorator is a callable that takes another function as an 
##   argument (the decorated function).
## A decorator may perform some processing with the decorated 
##   function, and returns it or replaces it with another function or callable object

# assuming an existing decorator named decorate, this code
# @decorate
# def target():
#   print('running target()')
# has the same effect as writing this:
# def target():
#   print('running target()')
# target = decorate(target)

# Proving that a function can get replaced when decorated

def deco(func):
  def inner():
    print('running inner()')
  return inner

@deco 
def target():
  print('running target()')

# target()  # running inner() -- think; target = deco(target); target()

# Three essential facts make a good summary of decorators
## A decorator is a function or another callable
## A decorator may replace the decorated function with a different one
## Decorators are executed immediately when a module is loaded

