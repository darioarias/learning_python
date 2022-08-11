
class Node(object):
  def __init__(self, value, left = None, right = None) -> None:
    self.value = value
    self.left = left 
    self.right = right
  
  def __iter__(self):
    return [self.value, self.left, self.right].__iter__()

  def __repr__(self) -> str:
    return f'Node({self.value!r}{f", left: Node{type(self.left.value)}" if self.left is not None else ""}{f", right: Node{type(self.right.value)}" if self.right is not None else ""})'

root = Node(10)
left = Node(5)
right = Node(15)
left_left = Node(2)
left_right = Node(7)
right_left = Node(12)
right_right = Node(17)

root.left = left
root.right = right

left.left = left_left
left.right = left_right

right.left = right_left
right.right = right_right
