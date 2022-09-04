from typing import NamedTuple

def Car(brand, color):
  _brand = brand
  _color = color

  def brand_setter(new_brand):
    nonlocal _brand
    _brand = new_brand
    return None
  
  def brand_getter():
    return _brand 
  
  def color_setter(new_color):
    nonlocal _color
    _color = new_color
    return None
  
  def color_getter():
    return _color
  
  def repr():
    return f'Car(brand={_brand!r}, color={_color!r})'

  class Property(NamedTuple):
    get: callable
    set: callable

  class Interface(NamedTuple):
    brand: Property
    color: Property
    
    def __repr__(self) -> str:
      return repr()

  return Interface(
    Property(brand_getter, brand_setter),
    Property(color_getter, color_setter)
  )
  


my_car = Car('Audi', 'Yellow')

# print(my_car['info']['print']())
# my_car['brand']['set']('Nissan')
# print(my_car['info']['print']())
my_car.brand.set('Nissan')
my_car.color.set('Red')
print(my_car)