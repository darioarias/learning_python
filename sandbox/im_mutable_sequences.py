from array import array
from collections import deque


# Mutable sequences are those whose data can be modified 
# list, bytearray, array.array, collections.deque
list = [8, 2, 3]
list[0] = 1  #  mutating a list

barr = bytearray([8, 2, 3])
barr[0] = 1  # mutating a byte-array

arr = array('i', [8, 2, 3])
arr[0] = 1  # mutating an array 

dque = deque([8, 2, 3])
dque[0] = 1  # mutating a deque


# Immutable sequencecs
# tuple, str, bytes

tuple = (8, 2, 3)
# tuple[0] = 1  # crashes the program

name = "8 2 3"
# name[0] = 1  # crashes the program

byt = bytes([8, 2, 3])
byt[0] = 1  # crashes the program


print(byt)
