#!/Users/darioarias/Desktop_2/studies/python/learning_python/venv/bin/python

import sys 
import unicodedata

START, END = ord(' '), sys.maxunicode + 1 

def find(*query_words, start=START, end=END):
  query = {w.upper() for w in query_words}
  for code in range(start, end):
    char = chr(code)
    name = unicodedata.name(char, None)
    if name and query.issubset(name.split()):
      print(f'U+{code:04X}\t{char}\t{name}')
    # if name and len(query.intersection({letter.upper() for letter in name.split()})) > 0:
    #    print(f'U+{code:04X}\t{char}\t{name}')

def print_all_unicode():
  for code in range(START, END):
    char = chr(code)
    name = unicodedata.name(char, None)
    if name:
      print(f'U+{code:04X}\t{char}\t{name}')


def main(words):
  if words:
    find(*words)
  else:
    print('Please provide words to find.')


if __name__ == '__main__':
  main(sys.argv[1:])