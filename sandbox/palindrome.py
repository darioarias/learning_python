
from collections import Counter

exam1 = "civic"
exam2 = "Anna"

def is_palindrome(s: str):
  s = ''.join([char for char in s if char.isalnum()])
  i = 0
  j = len(s) - 1
  while(i < j):
    if s[i].lower() != s[j].lower():
      return False 
    i += 1
    j -= 1
  return True


print(is_palindrome("A man, a plan, a canal: Panama"))