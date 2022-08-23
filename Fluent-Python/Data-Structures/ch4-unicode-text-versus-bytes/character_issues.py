

# note: Converting from code points to bytes is encoding; converting from bytes to code points is decoding

# Encoding and Decoding Examples
s = 'café'
len(s)  # 4

b = s.encode('utf-8')
len(b)  # 5

b = b.decode('utf-8')
len(b)  # 4

print(s.encode('utf8'))

