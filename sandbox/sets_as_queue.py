


# I want to see if I can use a set as a queue
# - We know that set perserve order
# - we also know that you can 'pop' and 'add' to the set

"""
Problem: Return the size of the bigest island
"""


map = [
  ['L', 'O', 'O', 'O', 'O', 'O'],
  ['L', 'O', 'O', 'O', 'O', 'O'],
  ['L', 'O', 'O', 'O', 'L', 'L'],
  ['O', 'O', 'O', 'O', 'O', 'O'],
  ['O', 'O', 'O', 'O', 'L', 'L'],
  ['O', 'O', 'O', 'O', 'L', 'L'],
]


def island_size(matrix, start_row, start_col, visited):
  queue = set([(start_row, start_col)])
  visited.add((start_row, start_col))

  size = 0
  while(len(queue) > 0):
    row, col = queue.pop()

    if matrix[row][col] == 'L':
      size += 1

    for delta_row, delta_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      new_row, new_col = (row + delta_row, col + delta_col)
      if not(new_row >= 0) or not(new_row < len(matrix)): continue
      if not(new_col >= 0) or not(new_col < len(matrix[0])): continue
      if not(matrix[new_row][new_col] == "L"): continue

      if not((new_row, new_col) in visited):
        queue.add((new_row, new_col))
        print(f'visiting: {(new_row, new_col)}')
        visited.add((new_row, new_col))
     
  return size

def max_island_size(matrix):
  visited = set()
  max_size = float('-inf')

  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      if matrix[row][col] == 'L' and not((row, col) in visited):
       max_size = max(island_size(matrix, *[row, col], visited), max_size)  
  return max_size

# Findings: this works, but set.pop() returns a random value, so it's not quite breath first search. 
# This works if bfs is not required


""" 
Trying Breath First Search on a binary Tree using set as a queue
"""

class Node(object):
  def __init__(self, value, left= None, right= None) -> None:
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self) -> str:
    return f'Node({self.value!r}{", Node" if self.left is not None else ""}{", Node" if self.right is not None else ""})'

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
"""
          10
    5            15
2       7    12      17
"""
from collections import deque


def bfs_set(root: Node):
  queue = set([root])
  nodes = []
  while(len(queue) > 0):
    current = queue.pop()

    nodes.append(current.value)

    if current.left is not None: 
      queue.add(current.left)

    if current.right is not None:
      queue.add(current.right)
  return nodes

def bfs_dequeue(root: Node):
  queue = deque([root])
  nodes = []
  while(len(queue) > 0):
    current = queue.popleft()

    nodes.append(current.value)

    if current.left is not None: 
      queue.append(current.left)

    if current.right is not None:
      queue.append(current.right)
  return nodes

print(bfs_set(root))  # notice that this does not yield a true breath first search 
print(bfs_dequeue(root))  # works as expected