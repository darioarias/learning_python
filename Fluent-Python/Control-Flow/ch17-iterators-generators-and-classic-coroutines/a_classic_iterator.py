

# Sentence implemented using the iterator pattern
from __future__ import annotations

import re
import reprlib
from typing import Union

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, txt) -> None:
        self.text = txt 
        self.words = RE_WORD.findall(txt)
    
    def __repr__(self) -> str:
        return f'Sentence({reprlib.repr(self.text)})'
    
    # def __iter__(self):
    #     return SentenceIterator(self.words)
    def __iter__(self):
        for word in self.words:
            yield word

# notice that we have to build an Iterator by hand
# class SentenceIterator:
#     def __init__(self, words) -> None:
#         self.words = words
#         self.index = 0
    
#     def __next__(self):
#         try:
#             word = self.words[self.index]
#         except IndexError:
#             raise StopIteration()
#         self.index += 1 
#         return word
    
#     def __iter__(self):
#         return self 
        
# def test():
#     yield from ['dario', 'arias']

# for word in test():
#     print(word)

class Node(object):
    def __init__(self, value: str | int, next: Union[Node, None] = None, previous: Union[Node, None] = None) -> None:
        self._val = value 
        self._next = next 
        self._prev = previous

    @property
    def value(self) -> str | int:
        return self._val

    @property
    def next(self) -> Union[Node, None]:
        return self.next

    @property
    def previous(self) -> Union[Node, None]:
        return self._prev

    def __iter__(self):
        yield from (self._val, self._next, self._prev)
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._val!r})"
