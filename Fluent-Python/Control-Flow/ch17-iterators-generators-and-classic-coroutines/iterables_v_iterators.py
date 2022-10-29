# iterable
# Any object from which the iter built-in function can obtain an iterator. 
# Objects implementing an __iter__ method returning an iterator are iterable. 
# Sequences are always iterable, as are objects implementing a __getitem__ method that accepts 0-based indexes.


from __future__ import annotations

from typing import Iterable, Iterator, Optional, TypeVar, Union

# s = 'ABC'  # iterable 
# for char in s:
#     print(char, char.__iter__)  
# under the hood, an iterator is being used 

# without the for, we would have to do the iteration manually 
# it = iter(s)
# while True:
#     try:
#         print(next(it)) 
#     except StopIteration:
#         del it 
#         break 


# T = TypeVar('T', str, int)

# class Node(object):
#     def __init__(
#         self, 
#         value: T, 
#         prev: Union[Node, None] = None, 
#         next: Union[Node, None] = None
#     ) -> None:
#         self.value: T = value
#         self.next: Union[Node, None] = next
#         self.prev: Union[Node, None] = prev
    
#     def __repr__(self) -> str:
#         cls = type(self)
#         return f"{cls.__name__}({self.value!r})"


# class LinkedList(object):
#     def __init__(self, items: Optional[Iterable[T]] = None) -> None:
#         self._head: Union[Node, None] = None 
#         self._tail: Union[Node, None] = None
        
#         if items:
#             for item in items:
#                 self.append(item)

#     def push(self, __item: T) -> None:
#         """Adds a value at the front of the list."""
#         if not self._head:
#             self._head = Node(__item)
#             self._tail = self._head
#             return None 
#         self._head = Node(__item, None, self._head)
#         return None

#     def append(self, __item: T) -> None:
#         """Adds a value at the end of the list."""
#         if not self._tail:
#             self.push(__item)
#             return None 
        
#         self._tail.next = Node(__item, self._tail)
#         self._tail = self._tail.next 
#         return None 

#     def insert(self, value: T,  after: int = 0) -> bool:
#         """Adds a value after a particular list node."""
#         _prev = self.node(after)
#         if not _prev:
#             return False 
#         _prev.next = Node(value, _prev, _prev.next)
#         if _prev == self._tail:
#             self._tail = _prev

#         return True

#     def node(self, at: int) -> Union[Node, None]:
#         _inx = 0
#         _current = self._head
#         while _current:
#             if _inx == at:
#                 return _current
#             _current = _current.next 
#             _inx += 1
#         return None
    
#     def pop(self) -> Union[T, None]:
#         """Removes the value at the front of the list"""
#         if not self._head:
#             return None 
        
#         r_val: T = self._head.value
#         if not self._head.next:
#             self._head = None 
#             self._tail = None 
#         else:
#             self._head = self._head.next

#         return r_val 

#     def remove_last(self) -> Union[T, None]:
#         """Removes the value at the end of the list."""
#         if not self._tail:
#             return None
#         if self._tail == self._head:
#             return self.pop()
        
#         r_val: T = self._tail.value
#         self._tail = self._tail.prev
#         self._tail.next = None

#         return r_val

#     def remove(self, at: int) -> Union[T, None]:
#         """Removes a value anywhere in the list."""
#         if at == 0:
#             return self.pop()
        
#         _prev = self.node(at-1)
#         if at == -1 or (_prev == self._tail):
#             print(_prev, self._tail, _prev == self._tail)
#             return self.remove_last()
        

#         r_val: T = _prev.next.value
#         _prev.next = _prev.next.next 
#         if _prev.next and _prev.next.next:
#             _prev.next.next.prev = _prev
#         # 1 -> 2 -> 3 -> 4
#         return r_val

#     ####### PYTHON SPECIAL METHODS
#     def __repr__(self) -> str:
#         cls_name = self.__class__.__name__
#         return F"{cls_name}({[node.value for node in self._gexp_helper(self._head)]!r})"

#     def __str__(self) -> str:
#         _nodes_str = []
#         for node in self._gexp_helper(self._head):
#             _nodes_str.append(str(node))
#         return " -> ".join(_nodes_str)
    
#     ######## HELPERS
#     def _gexp_helper(self, root: Node) -> Iterator[Node]:
#         while root: 
#             yield root
#             root = root.next

# # l = LinkedList([1, 2, 3, 4])
# l = LinkedList()
# l.append(1)
# l.insert(2, 0)
# l.insert(3, 0)
# l.insert(4, 0)
# l.remove(1)
# # l.push(1)
# # l.push(2)
# # l.append(3)
# # print(l.insert(6, 3))
# # print(l.remove_last())
# # print(l.remove_last())
# # print(l.remove_last())
# # print(l.remove_last())
# # print(l.remove_last())
# # print(l)
# print(repr(l))
