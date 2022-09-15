from datetime import datetime
# repr() -- unambiguous
# Return a string representing the object as the developer wants to see it. It’s what you get when the Python console or a debugger shows an object.

# str() -- readable
# Return a string representing the object as the user wants to see it. It’s what you get when you print() an object.




a = datetime.utcnow()
b = str(a)

# for var_ in (a, b):
#   in_scope = globals()
#   if in_scope['a'] == var_:
#     print("A")
#   else:
#     print("B")
#   print(f'repr => {repr(var_)}')
#   print(f'str => {str(var_)}\n')

  # note that str does help reading but not making clear what is what
  # on the other hand, repr does help make clear what is what

class Node(object):
  def __init__(self, value, next=None, prev=None) -> None:
    self.value = value
    self.next = next
    self.prev = prev 
  
  def __repr__(self) -> str:
    name = self.__class__.__name__
    return f'{name}({self.value!r})'
  
  def __str__(self) -> str:
    return f'{self.value}'
  
  def __eq__(self, __o: object) -> bool:
    if not self.__class__.__name__ == __o.__class__.__name__:
      return False
    if not self.value == __o.value:
      return False
    return True


n1 = Node('Dario')
name = 'Dario'


print(n1, name)  # print uses str, str makes Node readable but note that we would not be able to tell the difference here between node and name
print(repr(n1), repr(name))  # note how it's much easier to distinguish here