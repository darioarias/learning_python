"""About the while loop"""

# n = 1
# while n < 100:
#   output = ""
#   if n % 3 == 0:
#     output += "Fizz"
#   if n % 5 == 0:
#     output += 'Buzz'

#   if not (n % 5 == 0) and not (n % 3 == 0):
#     output = f"{n}"
  
#   n += 1
  
#   print(output)



def fizz_buzz_num(n: int = 100):
  result = [];
  for i in range(1, n + 1):
    if i % 3 == 0:
      result.append('Fizz')
    
    if i % 5 == 0:
      if i >= len(result):
        result.append('Buzz')
      else:
        result[i] = result[i] + 'Buzz'
    
    if not(i % 3 == 0) and not(i % 5 == 0):
      result.append(i)
  return result



for char in "salut":
  print(f"{char}")