from random import randint

"""NESTED LISTS"""
two_by_two = [[1, 2], [3, 4]]

row = [5, 4, 2, 9, 6, 8]

def less_than(val):
  # print(val)
  x = randint(0, 1)
  if x == 1:
    return True
  return False

# row.sort(key=less_than)

# print(row)



dict = {
  "New York": "Albany",
  "California": "Sacramento",
  "Colorado": "Denver"
}

for [state, capital] in dict.items():
  print(state, capital)