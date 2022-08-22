# we can use sets to remove duplicate
# list of ingridient to make a Bacon-Egg-Cheese sandwich, in order from first to last
list_with_dups = ['first_bread', 'eggs', 'eggs', 'cheese', 'bacon', 'cheese', 'lettuce', 'second_bread']

no_dups = list(set(list_with_dups))  # {'lettuce', 'cheese', 'bread', 'bacon', 'eggs'} -- Note that this does not keep the order of the ingridients. 

# perserving the order of items
no_dups_ordered = list(dict.fromkeys(list_with_dups).keys())  # ['first_bread', 'eggs', 'cheese', 'bacon', 'lettuce', 'second_bread']




# set operations
A = set([1, 2, 3, 4])
B = set([3, 4, 5, 6])

# intersection subset
a_intercept_b = A.intersection(B)  # {3, 4} -- A ∩ B (Item shows in A AND B)

# union
a_union_b = A.union(B)  # {1, 2, 3, 4, 5, 6} --  A U B (Item shows in A OR B)

# difference
a_dif_b = A.difference(B)  # {1, 2} -- A - B (Item shows in A - B, In A and not in B or the interception of A and B)

b_dif_a = B.difference(A)  # {5, 6} -- B - A (Item shows in B - A, in B and not in A or the incerception of B and A)

# symmetric Difference
a_sym_dif_b = A.symmetric_difference(B)  # {1, 2, 5, 6} -- A ∆ B (Item shows in A XOR B, in A or B but not in both)



# counting elements using sets

# count the number of unique entries
entries = ['rice', 'bread', 'eggs', 'rice', 'eggs', 'tomato', 'mango', 'mango', 'mayo', 'cream']  # 'mayo', 'tomato'
unique_items = len(set(entries))  # 5 -- first forms a set (which only accepts unque items, then counts them)

# count the number of repeated entries
repeated_items = len(entries) - len(set(entries))  # 3 -- everything minus uniques

# count the number of items that only appear once
seen_once = len(set(entries)) - repeated_items


# grabbing the elements
from collections import Counter
from html import entities  # use counter to deal with duplicate elemtens 

# count each entry
entries_count = Counter(entries)

# grab the unique element as a set
unique_set = set()
for entry in entries_count:
  if entries_count[entry] == 1:
    unique_set.add(entry)

# grab the repeating elements as a set
repeating_set = set()
for entry in entries_count:
  repeating_set.add(entry) if entries_count[entry] >= 2 else None



# FINDING
# as long as the question does not ask for specific values, you can deal with the lengths and set of the elements
# when the question cares about the actual elements, counter comes in handy

C = set([entry for entry in entries if entry not in ('rice', 'mayo')])  # set of entries excluding 'rice' and 'mayo'
                                                                        # {'cream', 'tomato', 'bread', 'eggs', 'mango'} 
D = set([entry for entry in entries if entry not in ('mayo', 'tomato')]) # Set if entries excluding 'mayo' and 'tomato' 
                                                                         # {'cream', 'bread', 'mango', 'rice', 'eggs'}
# print(C | D)  # union operator
# print(C & D)  # interception operator
# print(C - D)  # differences operator
# print(D - C)  # differences operator
# print(C ^ D)  # symmetric differences operator

print(len(set(entries) & set(['rice'])))

