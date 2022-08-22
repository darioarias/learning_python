# defaultdict: Another Take on Missing Keys

from collections import defaultdict, namedtuple
import re 
import sys

def word_analysis(file: str):
  word_regx = re.compile(r'\w+')
  indexies = defaultdict(list)
  Location = namedtuple('Location', ['line_no', 'column_no'])
  with open(file, mode='r', encoding='utf-8') as story:
    for line_no, line in enumerate(story, 1):
      for match in word_regx.finditer(line):
        word = match.group()
        column_no = match.start() + 1
        location = Location(line_no, column_no)

        indexies[word].append(location)

  for word in sorted(indexies, key=str.upper):
    print(word, indexies[word])

# word_analysis(sys.argv[1])


# The __missing__ Method
class StrKeyDict0(dict):
  def __missing__(self, key):
    if isinstance(key, str):
      raise KeyError(key)
    return self[str(key)]
  
  def get(self, key, default=None):
    try:
      return self[key]
    except KeyError:
      return default
    
  def __contains__(self, key):
    return key in self.keys() or str(key) in self.keys()


usr = StrKeyDict0({"2": "two", "4": "four"})

# print(2 in usr)


