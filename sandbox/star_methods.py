

# using dynamic args to collect all arguments
def greet(*people):
  for person in people:
    print(f'Hello {person}')


#returning a list that can be unpacked on the other side
def greet_msg(*people):
  message = []
  for person in people:
    message.append(f'Hello {person}')

  return message


msg1, msg2, msg3 = greet_msg('Pepe', 'Lissa', 'Greta')  # unpacking a function's return data
msg1, *rest = greet_msg('Pepe', 'Lissa', 'Greta')  # unpacking a function's return data

print(msg1)