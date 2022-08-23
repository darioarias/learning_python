

# In Python there are more than 100 codecs (encoder/decoders) for text to byte conversion


# Example of the string “El Niño” encoded with three codecs producing very different byte sequences
for codec in ['latin_1', 'utf-8', 'utf_16']:
  print(f'codec: {codec}, {"El Niño".encode(codec)}', end='\t')