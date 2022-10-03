# Multiple Inheritance and Method Resolution Order

# demonstrating the diamond problem 
class Root:
  def ping(self):
    print(f'{self}.ping() in Root')
  
  def pong(self):
    print(f'{self}.pong() in Root')
  
  def __repr__(self) -> str:
    cls_name = type(self).__name__
    return f'<instance of {cls_name}>'

class A(Root):
  def ping(self):
    print(f'{self}.ping() in A')
    super().ping()

  def pong(self):
    print(f'{self}.pong() in A')
    super().pong() 

class B(Root):
  def ping(self):
    print(f'{self}.ping() in B')
    super().ping()
  
  def pong(self):
    print(f'{self}.pong() in B')

class Leaf(A, B):
  def ping(self):
    print(f'{self}.ping() in Leaf')
    super().ping()


class U():
  def ping(self):
    print(f'{self}.ping() in U')
    super().ping()

class LeafUA(U, A):
  def ping(self):
    print(f'{self}.ping() in LeafUA')
    super().ping()

lua = LeafUA()
lua.ping()
