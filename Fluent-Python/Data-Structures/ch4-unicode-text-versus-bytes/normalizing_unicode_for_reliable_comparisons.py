## There are some issues when trying to check if two strings are the same. Consider the following

str1 = 'café'
str2 = 'cafe\N{COMBINING ACUTE ACCENT}'

# print((str1, str2))  # ('café', 'café') -- note that the two words look exactly the same
# print((len(str1), len(str2)))  # (4, 5) -- notice, however, that their lengths are not the same

# these two strings are "canonical equivalents" but python sees different bytes thus thinks they are different 
# to fix the issue, we must use string normalization, below is an example
from unicodedata import normalize, name

str1_normalized_nfc = normalize('NFC', str1)
str2_normalized_nfc = normalize('NFC', str2)

# print((str1_normalized_nfc, str2_normalized_nfc))  # ('café', 'café') -- still look the same
# print((len(str1_normalized_nfc), len(str2_normalized_nfc)))  # (4, 4) - Notice that the length is now the same

str1_normalized_nfd = normalize('NFD', str1)
str2_normalized_nfd = normalize('NFD', str2)

# print((str1_normalized_nfd, str2_normalized_nfd))  # ('café', 'café') -- still look the same
# print((len(str1_normalized_nfd), len(str2_normalized_nfd)))  # (5, 5) - Notice that the lengths are now the same


# it's a good idea to normalize user-input-text before saving it


ohm = '\u2126'
name(ohm)  # 'OHM SIGN'
ohm_c = normalize('NFC', ohm)
name(ohm_c)  # 'GREEK CAPITAL LETTER OMEGA'
ohm == ohm_c  # False
normalize('NFC', ohm) == normalize('NFC', ohm_c)  # True

