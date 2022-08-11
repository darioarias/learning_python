# from collections import deque


# queue = deque([1, 2, 3, 4])


# while(len(queue) > 0):
#   # print(queue.popleft())
#   pass

# for i in range(1, 5):
#   queue.append(i)



# Array can replace lists in some cases
# if a list only contains numbers, an array.array is more efficient 
from array import array
from random import random

floats = array('d', (random() for i in range(10*7)))

# saving array to file
# fp = open('floats.bin', 'wb')
# floats.tofile(fp)
# fp.close()

# loading array from file
# floats2 = array('d')
# fp = open("floats.bin", 'rb')
# floats2.fromfile(fp, 10*7)
# fp.close()


# print(floats)