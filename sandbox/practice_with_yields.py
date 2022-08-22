



""" 
Problem: 
      Write a function fib, that returns the fibonacci sequence. 
      You may decide how to store the values, in memory or within a general expression
"""
from time import sleep

def fib():
  x_1 = 0
  x_2 = 1

  yield x_1
  yield x_2

  while True:
    yield x_1 + x_2
    x_2, x_1 = x_2, x_1 + x_2


for i in fib():
  print(i)
  sleep(0.5)

