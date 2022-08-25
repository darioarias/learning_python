## Python variables are like reference variables in Java [not boxes];
# a better metaphor is to think of variables as labels with names attached to objects

## Take a look at the following example
# Variables a and b hold references to the same list, not copies of the list
a = [1, 2, 3]
b = a 
a.append(4)
b  # [1, 2, 3, 4]
# notice that b cannot be a box holding reference to [1, 2, 3]
# instead is holding a reference to the memory where a is stored
# which gets updated when a gets updated
# the b = a statement does not copy the contents of box a into box b. 
# It attaches the label b to the object that already has the label a


## x = ... binds the x name to the object created or referenced on the righthand side.
# And the object must exist before a name can be bound to it
# look at the following example

class Gizmo:
  def __init__(self) -> None:
    print(f'Gizmo id: {id(self)}')

x = Gizmo()
# y = Gizmo() * 10  # TypeError: unsupported operand type(s) for *: 'Gizmo' and 'int'
# print(dir())  # ['Gizmo', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'x']
