

# A set is a collection of unique objects. A basic use case is removing duplication
l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
unique = set(l)  # {'spam', 'eggs', 'bacon'}
unique_list = list(unique)  # ['eggs', 'spam', 'bacon']

# If you want to remove duplicates but also preserve the order of the first occurrence of each item, 
# you can now use a plain dict to do it

unique_ordered = dict.fromkeys(l).keys()  # dict_keys(['spam', 'eggs', 'bacon'])
unique_ordered_list = list(unique_ordered)  # ['spam', 'eggs', 'bacon']



# operations: let A and B be sets (i.e Set A, Set B)
# A | B -- union
# A & B -- intersection
# A - B -- difference
# A ^ B -- symmetric difference


# magine you have a large set of email addresses (the haystack) and 
# a smaller set of addresses (the needles) and you need to count how many needles occur in the haystack.

# Count occurrences of needles in a haystack, both of type set
haystack = set(['pl@gmail.com', 'pl@work.com', 'wl@gmail.com', 'wl@work.com'])
needles = set(['wl@work.com', 'some@work.com'])
found = len(needles & haystack) 


# Same problem -- Without the intersection operator
found = 0
for n in needles:
  if n in haystack:
    found += 1

# the first example runs a little faster, but we need sets


# Same problem -- starting structures are not sets
found = len(set(needles) & set(haystack))

# another way
found = len(set(needles).intersection(haystack))


# set literals
lit_set = {1, 2, 3}
empty_set = set()
lit_set.pop()  # 1

lit_set_2 = set([1, 2, 3])  # less readable, actually slower: look up for constructuor, list constructor, then built set


# frozensets don't have special literals
lit_frozen = frozenset(range(10))



# Set comprehensions 
# there are also SETCOMPS!
# Build a set of Latin-1 characters that have the word “SIGN” in their Unicode names
from unicodedata import name

set_comp = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '') }
# print(set_comp)

# print(set([1, 2]) <= set([1, 2, 3]))

# Fiding common keys amongst dict
d1 = dict(a=1, b=2, c=3, d=4)
d2 = dict(b=20, d=40, e=50)

d1.keys() & d2.keys()  # {'d', 'b'} -- returns the interception between d1.keys and d2.keys
