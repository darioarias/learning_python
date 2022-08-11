"""
Given the root of a tree, return a list with every node by level, from left to right. 
Example: 
             10  <-- (root)
        5         15
    2      7   12     17  

Your code should return: [10, 5, 15, 2, 7, 12, 17]
Note: we do not care what data structure or algorithm you use, we only care about the output
Moreover, the solution has to be strictly O(N) or better in time and space complexity """

from collections import deque
from trees import Node, root  # brings in a pre-built tree representetd the given example

def bfs(root: Node):
  queue = deque([root])  # notice that I was able to start using a double-ended queue from collections, 
                         # without writting any custome code
  output = []
  while(len(queue) > 0):
    value, left, right = queue.popleft()  # for unpacking, i had to implement the iter dunder
    output.append(value)

    if(left is not None):
      queue.append(left)
    
    if(right is not None):
      queue.append(right)
  return output

print(bfs(root))