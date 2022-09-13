# creating a clock function to time the code
import time
import functools

def clock(func):
  functools.wraps(func)
  def clocked(*args, **kwargs):
    t0 = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - t0
    args_lst = [repr(arg) for arg in args]
    args_lst.extend(f'{k}={v!r}' for k, v in kwargs)
    args_str = ', '.join(args_lst)
    name = func.__name__

    print(f'[{elapsed:0.8f}] {name}({args_str}) -> {result!r}')
    return result
  return clocked

@functools.cache
@clock  # fib = clock(fib)
def fibonacci(n):
  if n <= 2: return 1
  return fibonacci(n - 1) + fibonacci(n - 2)
# this is using the built in cached (memoize) technique

# the function below is equivalent 
@clock
def memoized_fib(n, memo={}):
  if n <= 2: return 1
  if n in memo: return memo[n]
  memo[n] = memoized_fib(n -1, memo) + memoized_fib(n - 2, memo)
  return memo[n]



# Using lru_cache
@functools.lru_cache
@clock
def fib(n):
  if n <= 2: return 1
  return fib(n-1) + fib(n-2)

# fib(300)



# Single Dispatch Generic Functions
# @singledispatch creates a custom @htmlize.register to bundle several functions into a generic function
import html 
from functools import singledispatch
from collections import abc
import fractions
import decimal
import numbers

@singledispatch
def htmlize(obj):
  content = html.escape(repr(obj))
  return f'<pre>{content}</pre>'

@htmlize.register
def _(text: str) -> str:
  content = html.escape(text).replace('\n', '<br/>\n')
  return f'<p>{content}</p>'

@htmlize.register
def _(seq: abc.Sequence) -> str:
  inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
  return '<ul>\n<li>'+inner + '</li>\n</ul>'

@htmlize.register
def _(n: numbers.Integral) -> str:
  return f'<pre>{n}(0x{n:x})</pre>'

@htmlize.register
def _(n:bool) -> str:
  return f'<pre>{n}</pre>'

@htmlize.register(fractions.Fraction)
def _(x) -> str:
  frac = fractions.Fraction(x)
  return f'<pre>{frac.numerator}/{frac.denominator}</pre>'

@htmlize.register(decimal.Decimal)
@htmlize.register(float)
def _(x) -> str:
  frac = fractions.Fraction(x).limit_denominator()
  return f'<pre>{x} ({frac.numerator}/{frac.denominator})</pre>'

print(htmlize(1/2))