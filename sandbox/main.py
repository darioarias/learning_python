class Node(object):
  def __init__(self, value, left = None, right = None) -> None:
    self.value = value
    self.left = left
    self.right = right

"""
       10
    5      15
  2  7   12  17
"""

# Creating the nodes, note the names
root = Node(10)

left = Node(5)
left_left = Node(2)
left_right = Node(7)

right = Node(15)
right_left = Node(12)
right_right = Node(17)

#linking the nodes.
root.left = left

left.left = left_left
left.right = left_right

root.right = right

right.left = right_left
right.right = right_right


def pre_order(root: Node = None):
  if root is None: 
    return; 

  print(f"visiting: {root.value}")
  pre_order(root.left)
  pre_order(root.right)


def post_order(root: Node = None):
  if root is None: 
    return; 
  
  post_order(root.left)
  post_order(root.right)
  print(f"visiting: {root.value}")


def in_order(root: Node = None):
  if root is None: 
    return;
  
  in_order(root.left)
  print(f"visiting: {root.value}")
  in_order(root.right)


def breath_first(root: Node = None):
  queue = [root]  # F.I.F.O | L.I.L.A 

  while(len(queue) > 0):
    current = queue.pop(0)

    print(f"visiting: {current.value}")
    if current.left: 
      queue.append(current.left)
    if current.right:
      queue.append(current.right)

# pre_order(root)
# in_order(root)
# post_order(root)

# breath_first(root)