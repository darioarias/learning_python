import bisect
import sys

# this package uses binary search for searching and insertion which allows it to 
# keep a list sorted

#adding elements 
list = [1, 2, 3, 4]
bisect.insort(list, 3)  # [1, 2, 3, 3, 4] note that the list is still sorted

# Searching with bisect
print(bisect.bisect_left(list, 3))