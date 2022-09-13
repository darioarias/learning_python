
""" 
Find the longest chain given;
  - a word starts with the ending of the previous;
      example: one-two -> two-three
      non-example: one-two -/> one->three
 """
from operator import ne
from typing import Optional
from collections import defaultdict

words = [
  "one-two",
  "two-three",
  "two-four",
  "three-two",
  "four-three",
  "four-five",
  "three-six",
  "six-three"
]

# words = [
#   "one-two",
#   "two-three",
#   "three-four",
#   "three-five",
#   "five-one"
# ]

def split(word: str, *items_pos, delimiter: str = "-"):
  if len(word) < 2: return []
  letters = word.split(delimiter)

  if len(items_pos) == 0:
    return letters
  # if len(set(items_pos)) > len(letters): 
  #   raise IndexError('Cannot access more items than the list contains')
  return [letters[index] for index in items_pos]


def process_words(words: list[str]) -> dict:
  connections = {}
  for word in words:
    [first_word, last_word] = split(word, 0, -1)
    connections.setdefault(first_word, []).append(word)
    if not(last_word in connections):
      connections[last_word] = []

  for key in connections:
    connections[key] = connections[key][::-1]

  return connections

# def explore_paths(word_hash, start, visited):
#   if (start in visited): return [[]]
#   visited.add(start)

#   paths = []
#   for neighbor in word_hash[start]:
#     [last_letter] = split(neighbor, -1)
#     if len(word_hash[last_letter]) > 0:
#       sub_paths = explore_paths(word_hash, last_letter, visited)
#       for path in sub_paths:
#         path.insert(0, neighbor)
#         paths.append(path)
#     else: paths.append([neighbor])
#   return paths
from collections import deque
def explore_paths(hash, start):

  new_paths = []
  path_to_explore = deque([start])
  while(len(path_to_explore) > 0):
    # print(path_to_explore)
    candidate = path_to_explore.pop()
    for pos_path in hash[candidate]:
      # print('ran')
      if len(new_paths) == 0:
        # print('len 0')
        new_paths.append([pos_path])
        [last] = split(pos_path, -1)
        path_to_explore.append(last)
        continue
      for saved_path in new_paths:
        # print('inner ran')
        first, last = split(pos_path, 0, -1)
        [saved_last] = split(saved_path[-1], -1)
        # print(saved_path, saved_last)
        if saved_last == first:
          saved_path.append(pos_path)
          path_to_explore.append(last)
        else:
          new_path = [*saved_path[:-1], pos_path]
          if not new_path in new_paths:
            new_paths.append(new_path)
          print('branch', new_paths)


      
  
  print(new_paths)
  return ""
  # for neighbor in hash[start]:
  #   for path in paths:
  #     if not neighbor in path:
  #       neighbor_first, neighbor_last = split(neighbor, 0, -1)
        
  #       # print(path[-1], path) if len(path) > 0 else None
  #       # if len(path) == 0:
  #       # if len(path) == 0 or neighbor_first == split(path[-1], -1)[0]:
  #       path.append(neighbor)
  #         # print()
  #       # if len(path) > 0:
  #       #   print("PATH", path)
  #       # if len(path) == 0:
  #       #   pass
  #         # path.append(neighbor)
  #       # else:
  #         # new_paths.append([*path[:-1], neighbor])
  #         # pass

  #         # new_paths.append(*path[:-1], neighbor)
  #       explore_paths(hash, neighbor_last)
  #     # else:
  #     #   paths.append([*path[:-1], neighbor])
  #     # print(paths)
  #       # if path_last == neighbor_first:
  #       #   path.append(neighbor)
    
  # print(paths)
      




# def find_longest_chain(words):
#   words_hashed = process_words(words)
#   # print(words_hashed)
#   # return;
#   path_length, longest_path = 0, []
#   for start in words_hashed:
#     for path in explore_paths(words_hashed, start):
#       if len(path) > path_length:
#         path_length = len(path)
#         longest_path = path

#   return longest_path


# find_longest_chain(words)
# print(find_longest_chain(words))

processed = process_words(words)
# print(processed)
longest_chain = explore_paths(processed, 'one')
print(longest_chain)
