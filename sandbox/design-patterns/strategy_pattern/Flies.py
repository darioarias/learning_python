
class Fly(object):
  # def __init__(self, )
  def fly(self):
    pass
  
  def __call__(self):
    return self.fly()

class CanFly(Fly):
  def fly(self):
    return 'Flying High'


class CantFly(Fly):
  def fly(self):
    return 'Cannot fly'