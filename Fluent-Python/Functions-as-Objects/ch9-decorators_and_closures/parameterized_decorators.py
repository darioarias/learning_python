
# Abridged registration.py module from Example 9-2, repeated here for convenience
# registry = []

# def register(func):
#   print(f'running register ({func.__name__} -- {func})') 
#   registry.append(func)
#   return func 

# @register
# def f1():
#   print('running f1()')


# A Parameterized Registration Decorator
# To accept parameters, the new register decorator must be called as a function

registry = set()
def register(active=True):
  def decorate(func):
    print('running register'
          f'({active=}) -> decorate({func})')
    if active:
      registry.add(func)
    else:
      registry.discard(func)
    
    return func 
  return decorate

# @register(active=False)
def f1():
  print('running f1()')

# @register()
def f2():
  print('running f2()')

def f3():
  print('running f3()')



# Module clockdeco_param.py: the parameterized clock decorator
import time
DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT): #1
  def decorate(func): #2
    def clocked(*_args): #3
      t0 = time.perf_counter()
      _result = func(*_args) #4
      elapsed = time.perf_counter() - t0
      name = func.__name__
      args = ', '.join(repr(arg) for arg in _args) #5
      result = repr(_result) #6
      print(fmt.format(**locals())) #7
      return _result # 8
    return clocked #9
  return decorate #10

# if __name__ == '__main__':
#   @clock() # 11
#   def snooze(seconds):
#     time.sleep(seconds)

#   for i in range(101):
#     # snooze(i ** 1.2)
#     print(i ** 1.23 - 0.0001)

# 