""" Lets take a look at some of the errors that can occur while working with different codecs """


## Coping with UnicodeEncodeError
city = 'São Paulo'
city.encode('utf-8')  # b'S\xc3\xa3o Paulo'
city.encode('utf_16')  # b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
city.encode('iso8859_1')  # b'S\xe3o Paulo'
#city.encode('cp437')  # UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>
city.encode('cp437', errors='ignore')  # b'So Paulo' -- to deal with the above error, we can pass in an argument
city.encode('cp437', errors='replace')  # b'S?o Paulo' -- to deal with the above error, we can pass in an argument
city.encode('cp437', errors='xmlcharrefreplace')  # b'S&#227;o Paulo' -- to deal with the above error, we can pass in an argument

## Coping with UnicodeDecodeError
# illustrates how using the wrong codec may produce gremlins or a UnicodeDecodeError.
octets = b'Montr\xe9al'
octets.decode('cp1252')  # 'Montréal'
octets.decode('iso8859_7')  # Montrιal
octets.decode('koi8_r')  # MontrИal
#octets.decode('utf_8')  # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte
octets.decode('utf_8', errors='replace')  # Montr�al


## SyntaxError When Loading Modules with Unexpected Encoding
# an error will occur if a module does not have any encoding/non-U8 encodings. 
# To fix it, add a magic comment, '# coding: cp1252 (etc)'

## How to Discover the Encoding of a Byte Sequence
# How do you find the encoding of a byte sequence? Short answer: you can’t. You must be told