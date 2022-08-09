from copy import deepcopy



class Node(object):
  def __init__(self, value = None, next = None) -> None:
    self.value = value
    self.next = next
  
  def __eq__(self, rhs: object) -> bool:
    return self.value == rhs.value and self.next == rhs.next

  def __repr__(self) -> str:
    return f"Node({self.value!r}, {f'Node<{self.next.value!r}>' if self.next is not None else ''})"


  




n1 = Node("one")
n1.next = Node("two")
n1.next.next = Node("Three")

# n1_copy = deepcopy(n1)
# n1_copy.value = "two"

print(n1)