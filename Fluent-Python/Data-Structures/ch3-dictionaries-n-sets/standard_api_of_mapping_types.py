from collections.abc import Mapping, MutableMapping

my_dict = {}
isinstance(my_dict, Mapping)  # True
isinstance(my_dict, MutableMapping)  # True



# hashable review

# data/variable are hashable if they have a hashcode that does not changes through their lifetime. 
# think immutable, if immutable container, each element in it must be hashable

tt = (1, 2, (30, 40))  # hashable since it's an immutable container and each item is hashable
tt_hash = hash(tt)
# print(tt_hash)

tl = (1, 2, [30, 40])  # un-hashable since some elements within are unhashable. (i.e lists are mutable containers)
# tl_hash = hash(tl)  # creates a TypeError

# we can use frozenset to make a mutable container hash-able
tf = (1, 2, frozenset([30, 40]))
tf_hash = hash(tf)
# print(tf_hash)


# dict.get(item, default) is not always the best, especially when updating a dict

from pathlib import Path
from collections import namedtuple
import re 
import sys

Location = namedtuple('Location', ['line_no', 'column_no'])

def parse_file(file: str):
  story_path = Path.joinpath(Path.cwd(), file)
  index = {}
  word_regx = re.compile('\w+')
  with story_path.open(mode='r', encoding='utf-8') as story:
    for line_no, line in enumerate(story, 1):
      for match in word_regx.finditer(line):
        word = match.group()
        column_no = match.start() + 1

        word_pos = Location(line_no, column_no)
        # occurrences = index.get(word_pos.word, [])  # <REPLACED> first search through the dict to find the word
        # occurrences.append(word_pos)  # <REPLACED>
        # index[word_pos.word] = occurrences  # <REPLACED> second search through the dict to insert

        index.setdefault(word, []).append(word_pos)  # notice that we only do one search, if found, append to it. if not, set to empty, add the 
  return index
        

print(parse_file(sys.argv[1]))