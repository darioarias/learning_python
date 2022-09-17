


class BaseDataStructure(object):
  data_type = "BaseDataStructure"
  
  @property
  def type(self):
    return self.data_type
  
  def __repr__(self, indent_depth: int = 1) -> str:
    name = type(self).__name__
    indent = " " * (2*indent_depth)
    repr = f"{name} (\n{indent}"
    attrs = self.__dict__
    for attr in attrs:
      repr += f"{attr} = {attrs[attr]!r}\n{indent}"
    repr += f")"
    return f'{repr}'

class BaseNode(BaseDataStructure, object):
  data_type = "BaseNode"
  def __init__(self, value) -> None:
    self.value = value
  
  # def __repr__(self) -> str:
  #   name = type(self).__name__
  #   return f'{name}({self.value!r})'
  
  def __str__(self) -> str:
    return f'{self.value!r}'
  
  def test(self):
    print(self.__dict__)

  def __eq__(self, other) -> bool:
    self_name = type(self).__name__
    other_name = type(other).__name__
    if not self_name == other_name:
      return False 

    if not self.value == other.value:
      return False

    return True

class SinglyLinkedListNode(BaseNode):
  data_type = "SinglyLinkedListNode"

  def __init__(self, value, next: BaseNode = None) -> None:
    super().__init__(value)
    self.next = next 

  # def __repr__(self) -> str:
  #   name = type(self).__name__
  #   next = f'{name}({self.next.value!r})' if self.next else ""
  #   return f"{name}({self.value!r}, next={next})"


t = SinglyLinkedListNode('Arias')
test = SinglyLinkedListNode("Dario")
test.next = t

print(repr(test))
# print(test.__dict__)
# test.test()


# sl = SinglyLinkedListNode('Dario')
# print(sl.type)
# class BaseList(object):
