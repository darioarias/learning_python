## The Unicode standard provides an entire database—in the form of several structured text files—that 
# includes not only the table mapping code points to character names, but also metadata about the individual characters and how they are related. 
# For example, the Unicode database records whether a character is printable, is a letter, is a decimal digit, or is some other numeric symbol.

## Finding characters by Name
from unicodedata import name

# print(name('A'))
# print(name('Ã'))
# print(name('ã'))
# print(name('♛'))
# print(name('😸'))

## we can use these to build simple application to search characters. Check emojify.py in sandbox


# Demo of Unicode database numerical character metadata (callouts describe each column in the output)
import unicodedata
import re 

re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
  print(f'U+{ord(char):04x}', char.center(6), 
  're_dig' if re_digit.match(char) else '-',
  'isdig' if char.isdigit() else '-',
  'isnum' if char.isnumeric() else '-',
  f'{unicodedata.numeric(char):5.2f}',
  unicodedata.name(char),
  sep='\t')
  