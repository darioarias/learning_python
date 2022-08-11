



"""
Notes about slicing 
"""
from logging import exception
from math import floor
from typing import MutableSequence, Sequence

# Why Slices and Ranges Exclude the Last Item
# -> It’s easy to see the length of a slice or range when only the stop position is given: 
#    range(3) and my_list[:3] both produce three items.
# -> It’s easy to compute the length of a slice or range when start and stop are given: just subtract stop - start.
# -> It’s easy to split a sequence in two parts at any index x, without overlapping: sim‐ ply get my_list[:x] and my_list[x:]. For example:
list = [10, 20, 30, 40, 50, 60]
mid_point = floor(len(list)/2)

first_half = list[:mid_point]
second_haft = list[mid_point:]


# Slice Objects
# s[a:b:c] can be used to specify a stride or step c, causing the resulting slice to skip items.
# note that [a:b:c] creates a slice object, slice(stop), slice(start, stop[, step])
toy = 'bicycle'

# using [start:stop:step], i can grab any slice...yum
toy[0::3]  # bye -- starting at index 0, inclusive, grabs every 3rd letter

toy[::-1]  # elcycib -- starting at index 0, grabs every letter taking a negative step

palindrome = toy[2:5:]  # cyc

# to check that a word is a palindrome, I can check the sequence against its reverse counter-part
assert(palindrome == palindrome[::-1])  # passes if the word 'cyc' is the same spelled forwards and backwords




# slicing a flat file, naming slices
def proccess_flat_file(file):
  SKU = slice(0, 6)
  DESCRIPTION = slice(6, 40)
  UNIT_PRICE = slice(40, 49)
  QUANTITY = slice(49, 52)
  ITEM_TOTAL = slice(53, None)
  line_items = file.split('\n')[2:]
  print(f"{'SKU':6} {'DESCRIPTION':<31} {'UNIT_PRICE':8} {'QTY':>4} {'TOTAL':>6}")
  for line in line_items:
    print(f'{line[SKU]} {line[DESCRIPTION]} {line[UNIT_PRICE]} {line[QUANTITY]} {line[ITEM_TOTAL]}')


invoice = """
0.....6.................................40.......49..53.........
1909  Pimoroni PiBrella                 $17.50   3   $52.50
1489  6mm Tactile Switch x20             $4.95   2    $9.90
1510  Panavise Jr. - PV-201             $28.00   1   $28.00
1601  PiTFT Mini Kit 320x240            $34.95   1   $34.95"""

# proccess_flat_file(invoice)



# Assigning to Slices
"""
ASSERTION: 
Mutable sequences can be grafted, excised, and otherwise modified in place using 
slice notation on the lefthand side of an assignment statement or 
as the target of a del statement.
"""

def swap(a: int, b: int, list: MutableSequence):
  if not isinstance(a, int): 
    raise Exception("first index must be an Interger")
  if not isinstance(b, int):
    raise Exception("second index must be an Interger")
  if not isinstance(list, MutableSequence):
    raise Exception("list must be a mutable sequence")
  if not (-1 <= a and a < len(list)) or not(-1 <= b and b < len(list)):
    raise Exception('Indexies must be within bounds')
  
  [list[a], list[b]] = [list[b], list[a]]  # uses sequene slice notation to reassign values at index a and b


list = [50, 30, 40, 20]  # to sort this we just need to swap the last 

# [list[0], list[-1]] = [list[-1], list[0]]
swap(-1, 0, list) # calling swap on both, the first and last, elements will cause the list to be sorted

# print(list)  # [20, 30, 40, 50]

list[:] = list[::-1]  # reversing a list by re-writing the objects with their reverse counter-parts

#print(list) # [50, 40, 30, 20]

list[2:4] = [20, 30]  # modifying a list in place

del list[0:2]  # deleting elements in place

list[2:5:1] = [40, 50]  # in-place editing a list


# Using + and * with Sequences
list = [1, 2, 3]
list * 2  # [1, 2, 3, 1, 2, 3] 
mes = 'Da'*2 # 'DaDa'


# Building Lists of Lists
board = [['_'] * 3 for i in range(3)]



# Augmented Assignment with Sequences
# we can use id to check the identification of an obj

my_list = [1, 2, 3, 4]
list_id = id(my_list)

# *= calls __iadd__ if it's implemented, else __add__, which changes the value, and thus id, of the object
# __iadd__ does not change the object, __add__ changes the values

# print(f'list_id: {list_id}')
my_list *= 2
list_id = id(my_list)
# print(f'list_id: {list_id}')


my_tuple = (1, 2, 3)
t_id = id(my_tuple)
# print(f'tuple_id: {t_id}')
my_tuple *= 2
t_id = id(my_tuple)
# print(f'tuple_id: {t_id}')


# A += Assignment Puzzler

"""
Analyze the following
  t=(1,2,[30,40])
  t[2] += [50, 60]

What happens next? Choose the best answer:
A. t becomes (1, 2, [30, 40, 50, 60]).
B. TypeError is raised with the message 'tuple' object does not support item assignment.
C. Neither.
D. Both A and B.

ANSWER: D
"""

t=(1,2,[30,40])
# t[2] += [50, 60]

# use this link to visualize: https://pythontutor.com/render.html#code=t%3D%281,2,%5B30,40%5D%29%0At%5B2%5D%20%2B%3D%20%5B50,%2060%5D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


