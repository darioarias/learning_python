
# protocal just refers to the interface, in in python we can say that protocal in python are an informal interface

#there are times when we do not need to implement a full protocal as in
class Vowels:
  def __getitem__(self, i):
    return 'AEIOU'[i]

for vowel in Vowels():
  print(vowel)  # prints A, E, I, O, U

print(
  'O found in Vowels' 
  if 'O' in Vowels() 
  else 'O not found in Vowels'
)  # 'O found in Vowels' 

print(Vowels()[0])  # A

# Note that __getitem__ is all it took to make Vowels behave like a sequence
