
def apply(func, list):
  """ This function takes a list and a function as a parameter and returns a new list after applying the function """
  return [func(x) for x in list]

def apply_in_place(func, list):
  """This function takes a list and a function as parameters and modifies the list in-place by applying the given function"""
  for i in range(len(list)):
    list[i] = func(list[i])

def apply_return_gen(func, list):
  for x in list:
    yield func(x)

square = lambda x : x * x
list = [1, 2, 3, 4]

# apply_in_place(square, list)
# print(list)
# print(apply(, list))

for x in apply_return_gen(square, list):
  print(x)

