# Simple decorator to show the running time of functions
import time

def clock(func):
  def clocked(*args):
    t0 = time.perf_counter() 
    result = func(*args)
    elapsed = time.perf_counter() - t0 
    name = func.__name__
    arg_str = ', '.join(repr(arg) for arg in args)
    print(f'{elapsed:0.8f}s {name}({arg_str}) -> {result!r}')
    return result
  return clocked

# new version of clock using functools module
import functools

def clock(func):
  @functools.wraps(func)
  def clocked(*args, **kwargs):
    t0 = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - t0 
    name = func.__name__
    arg_lst = [repr(arg) for arg in args]
    arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
    arg_str = ', '.join(arg_lst)
    print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
    return result
  return clocked



@clock  # greet = clock(greet)
def greet(name: str):
  return f'Hello, I\'m {name}. It\'s nice to meet you!'

@clock  # snooze = clock(snooze)
def snooze(seconds):
  time.sleep(seconds)

@clock  # factorial = clock(factorial)
def factorial(n):
  return 1 if n < 2 else n * factorial(n-1)



# factorial(9)
snooze(.1)
# performace('Dario')
# print(p1)
# performace(p1) 
# greet('Dario')
