# some times, you have to provide type hints to your functions
# for this we use stub files (.pyi). When a function supports
# more than one signature, you can use @overload decorator
# look at program.py and program.pyi
from program import sum_concat

# print(sum_concat(char for char in ('a', 'b', 'c', 'd')))
