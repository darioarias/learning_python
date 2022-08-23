


from pathlib import Path


file_path = Path.cwd()/'cafe.txt'

with file_path.open(mode='w', encoding='U8') as file:
  file.write('café') 

print(open('cafe.txt').read())  # works because the default is utf-8. But if the default changes, or encoding on line 10 changes, 
                                # it will break. Never depend on default, especailly if this is meant to be run on different computers.


## Checking system defaults 
import sys
import locale
my_file = open('dummy', 'w')
expressions = """
        locale.getpreferredencoding()
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
"""

for expression in expressions.split():
  value = eval(expression)
  print(f'{expression:>30} -> {value!r}')


## System analiss 