# Checking out the behavior of __getitem__ and slices

from ast import Pass


class MySeq:
  def __getitem__(self, index):
    return index 

s = MySeq()
s[1]  # 1 -- we just get back the index
s[1:7]  # slice(1, 7, None)  -- not we get a slice object
s[1:2:3]  # slice(1, 2, 3)
s[1:2:3, 9]  # (slice(1, 2, 3), 9)  -- now we get a tuple
s[1:2:3, 5:6]  # (slice(1, 2, 3), slice(5, 6, None)) -- tuple of slices
# remember slice notation
# SLICE(START:STOP:STEP) so;
# slice(1:4:2) means start at 1, stop at 4, step by 2.
# range works the same
for x in range(1, 4, 2):  # start at 1, end at 4, step by 2
  # print(x)
  Pass

my_nums = list(x for x in range(10))
my_nums[slice(1, len(my_nums), 2)]  # [1, 3, 5, 7, 9] - we can use slice to access lists


# taking a look at slice in depth 
slice  # <class 'slice'>
dir(slice)  # ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__'...

# notice that slice has an indices method
slice.indices  # Assuming a sequence of length len, calculate the start and stop
    # indices, and the stride length of the extended slice described by
    # S. Out of bounds indices are clipped in a manner consistent with the
    # handling of normal slices.

slice(None, 10, 2).indices(5)  # (0, 5, 2)
slice(-3, None, None).indices(5)  # (2, 5, 1) -- note how indices reworks the indexies

'ABCDE'[:10:2]  # is the same as 'ABCDE'[0:5:2].
'ABCDE'[-3:]  # is the same as 'ABCDE'[2:5:1].
