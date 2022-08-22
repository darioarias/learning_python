
# collections.ChainMap
# A ChainMap instance holds a list of mappings that can be searched as one. 
# The lookup is performed on each input mapping in the order it appears in the constructor call, 
# and succeeds as soon as the key is found in one of those mappings.
from collections import ChainMap

d1 = dict(a=1, b=3)
d2 = dict(a=2, b=4, c=6)
chain = ChainMap(d1, d2)

chain['a']  # 1
chain['b']  # 6


# The ChainMap instance does not copy the input mappings, but holds references to them. 
# Updates or insertions to a ChainMap only affect the first input mapping.

chain['c'] = -1

d1  # {'a': 1, 'b': 3, 'c': -1}
d2  # {'a': 2, 'b': 4, 'c': 6}


# ChainMap is useful to implement interpreters for languages with nested scopes, where each 
# mapping represents a scope context, from the innermost enclosing scope to the outermost scope.
import builtins
pylookup = ChainMap(locals(), globals(), vars(builtins))


# collections.Counter
# A mapping that holds an integer count for each key.
# Updating an existing key adds to its count.

from collections import Counter

ct = Counter('abracadabra')
ct  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.update('aaaaazzz')
ct  # Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.most_common(3)  # [('a', 10), ('z', 3), ('b', 2)]



# Subclassing UserDict Instead of dict
# It’s better to create a new mapping type by extending collections.UserDict rather than dict.
from collections import UserDict

class StrKeyDict(UserDict):
  def __missing__(self, key):
    if isinstance(key, str):
      raise KeyError(key)
    return self[str(key)]
  
  def __contains__(self, key):
    return str(key) in self.data
  
  def __setitem__(self, key, item):
    self.data[str(key)]= item