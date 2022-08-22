



from unicodedata import name

# set_comp = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '') }

for i in range(32, 256):
  print(name(chr(i)), chr(i), i) 