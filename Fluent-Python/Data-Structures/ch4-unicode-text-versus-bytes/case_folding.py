# Case folding is essentially converting all text to lowercase, with some additional transformations. 
# It is supported by the str.casefold() method.


# use casefold to compare case_insensative, NFC and NFD normalization functions
'Dario'.casefold() == 'dArio'.casefold()  # True

from unicodedata import normalize, combining
import string

def nfc_equal(str1, str2):
  return normalize('NFC', str1) == normalize('NFC', str2)

def fold_equal(str1, str2):
  return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())

# removing diacritics from a string
def shave_marks(txt):
  """Remove all diacritic marks"""
  norm_txt = normalize('NFD', txt)
  shaved = ''.join(c for c in norm_txt if not combining(c))
  return normalize('NFC', shaved)

# the above version of the shave function can go too far, 
# here is an edit 

def shave_marks_latin(txt):
  """Remove all diacritic marks from lating base characters"""
  norm_txt = normalize('NFD', txt)
  latin_base = False
  preserve = []

  for c in norm_txt:
    if combining(c) and latin_base:
      continue  # ignore diacritic on latin base char

    preserve.append(c)
    # if it isn't a combining char, it's a new base char
    if not combining(c):
      latin_base = c in string.ascii_letters
    
    shaved = ''.join(preserve)
    return normalize('NFC', shaved)

print(shave_marks_latin(''))