# closures are sometimes confused with anonymous functions


# a closure is a function—let’s call it f—with an extended scope that encompasses
# variables referenced in the body of f that are not global variables or local 
# variables of f. Such variables must come from the local scope of an outer function that encompasses f

def avg_maker():
  seen, total = 0, 0
  def avg(number:int):
    nonlocal seen 
    nonlocal total 
    total += number
    seen += 1
    return total/seen

  return avg
# print(avg(10))
# print(avg(11))

class Averager(object):
  def __init__(self) -> None:
    self.total = 0
    self.count = 0
  
  def __call__(self, new_value) -> float:
    self.total += new_value
    self.count += 1
    return self.total / self.count


# avg = avg_maker()
# avg = Averager()

# print(avg(10))
# print(avg(11))
# print(avg(11))
# print(avg(11))
# print(avg(20))