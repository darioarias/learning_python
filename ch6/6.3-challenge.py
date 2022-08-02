# Write a script called temperature.py that defines two functions:
"""
1. convert_cel_to_far() which takes one float parameter representing degrees Celsius 
    and returns a float representing the same temperature in degrees Fahrenheit using the following formula:
    F = C * 9 / 5 + 32

2. convert_far_to_cel() which takes one float parameter representing degrees Fahrenheit 
    and returns a float representing the same temperature in degrees Celsius using the following formula:
    C = (F - 32) * 5/9
"""

def convert_cel_to_far(celsius: float):
  """takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit"""
  fahrenheit = celsius * 9/5 + 32
  return fahrenheit 

def convert_far_to_cel(fahrenheit: float):
  """takes one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius"""
  celsius = (fahrenheit - 32) * 5/9
  return celsius


fahrenheit = float(input('Enter a temperature in degrees F: '))
print(f"{fahrenheit:.0f} degress F = {convert_far_to_cel(fahrenheit):.2f} degress C")

celsius = float(input("Enter a temperature in degrees C: "))
print(f"{celsius:.0f} degress C = {convert_cel_to_far(celsius):.2f} degrees F")