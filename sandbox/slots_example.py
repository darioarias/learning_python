
class Pixel:
  __slots__ = ('x', 'y')

  def __repr__(self) -> str:
    return f'{self.__class__.__name__}({self.x}, {self.y})'

class OpenPixel(Pixel):
  pass  # To make sure that instances of a subclass have no __dict__, you must declare __slots__ again in the subclass.


class ColorPixel(Pixel):
  __slots__ = ('color',)

cp = ColorPixel()


# p = Pixel()
# op = OpenPixel()
# print(op.__dict__)
# p.__dict__
# p.x = 10
# p.y = 20
# p.color = 'red'

# print(p)
