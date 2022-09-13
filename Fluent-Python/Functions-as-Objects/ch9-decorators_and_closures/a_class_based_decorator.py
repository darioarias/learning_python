# Module clockdeco_cls.py: parameterized clock decorator implemented as class
import time 

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

class clock(object):
  def __init__(self, fmt=DEFAULT_FMT):
    self.fmt = fmt 
  
  def __call__(self, func):
    def clocked(*_args):
      t0 = time.perf_counter()
      _result = func(*_args)
      elapsed = time.perf_counter() - t0 
      name = func.__name__
      args = ', '.join(repr(arg) for arg in _args)
      result = repr(_result)
      print(self.fmt.format(**locals()))
      return _result
    return clocked



@clock()
def f1():
  print('running f1')


if __name__ == "__main__":
  f1()