


nodes = []

def create_node(func):
  def init(self, value, next = None) -> None:
    self.value = value
    self.next = next
  return init

def repr(func):
  def represent(self):
    cls = self.__class__
    cls_name = cls.__name__
    return f'{cls_name}({self.value!r})'
  
  return represent


class Node(object):
  @create_node
  def __init__(self) -> None:
    pass
  
  @repr
  def __repr__(self):
    pass


n1 = Node('Dario')
n2 = Node('Liberty')

print(n1)