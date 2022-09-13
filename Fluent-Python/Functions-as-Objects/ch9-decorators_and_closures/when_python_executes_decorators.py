# A key feature of decorators is that they run right 
# after the decorated function is defined. 
# That is usually at import time (i.e., when a module is loaded by Python).

# tracking decorator runtime; The registration.py module
registry = []

def register(func):
  print(f'Running register({func})')
  registry.append(func)
  return func

@register 
def f1():
  print('Running f1()')

@register
def f2():
  print('Running f2()')

def f3():
  print('running f3()')

def main():
  print('Running main()')
  print('Registry -> ', registry)
  f1()
  f2()
  f3()

if __name__ == '__main__':
  main()

"""
Running register(<function f1 at 0x107176830>)
Running register(<function f2 at 0x107176950>)
Running main()
Registry ->  [<function f1 at 0x107176830>, <function f2 at 0x107176950>]
Running f1()
Running f2()
running f3()
"""