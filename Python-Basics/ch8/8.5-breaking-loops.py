






phrase = "Python is interpreseted, X not compiled"


for letter in phrase:
  if letter == 'd':
    print('breaking loop')
    break  # exits out of the loop
  if letter == 'o':
    print('using continue to move on')
    continue  # skips the rest of the code in the loop
  

#example of for-else loops

for letter in phrase:
  if letter == 'X':
    print('there is an X in the list')
    break
  # print(f'looking at {letter}')
else:
  print("There are no X on the loop")


