from collections import deque
from heapq import heapify, heappop, heappush
from typing import MutableSequence


dq = deque(range(10), maxlen=10)
dq.rotate(-4)
dq.appendleft(1)
dq.extend([11, 12])
dq.extendleft([13, 14])
# print(dq)

# Working with heaps 

# max heaps
max_heap = []

# since the heapq package does not support max heap, i just flip the sign for each number
heappush(max_heap, -1 * 400)
heappush(max_heap, -1 * 500)
heappush(max_heap, -1 * 300)

# grabing the top (max) value
[top] = [heappop(max_heap) * -1]

# min heap
min_heap = []

# min heaps are supported out of the box
heappush(min_heap, 4)
heappush(min_heap, 3)
heappush(min_heap, 5)
heappush(min_heap, 2)

# grabbing the top (smallest) value
[top] = [heappop(min_heap)]



# creating a class on top of heapq

class MaxHeap(object):
  def __init__(self, items: MutableSequence = []) -> None:
    self.heap = []
    for item in items:
      self.push(item)

  def push(self, value):
    return heappush(self.heap, value * -1)

  def pop(self):
    return heappop(self.heap) * -1

  def peek(self):
    return self.heap[0] if len(self.heap) > 0 else None

  def empty(self):
    return len(self.heap) == 0



max_heap = MaxHeap([4, 1, 2, 9, 6])

while(not max_heap.empty()):
  print(f"Value: {max_heap.pop()}")