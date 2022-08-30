# The first strange fact about del is that it’s not a function, it’s a statement. 
# We write del x and not del(x)—although the latter also works, 
# but only because the expressions x and (x) usually mean the same thing in Python.

# The second surprising fact is that del deletes references, not objects.
# Python’s garbage collector may discard an object from memory as an indirect result of del, 
# if the deleted variable was the last reference to the object.
# Rebinding a variable may also cause the number of references to 
# an object to reach zero, causing its destruction.

a = [1, 2]
b = a
del a 
b  # [1, 2]
b = [3]  # rebinding b, at this point [1, 2] has no references; GC will delete it

import weakref
s1 = {1, 2, 3}
s2 = s1 

def bye():
  print('...like tears in the rain.')

ender = weakref.finalize(s1, bye)
ender.alive  # true

del s1 
ender.alive  # true 
s2 = 'spam'

ender.alive  # false