

# Sentence implemented using the iterator pattern

import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, txt) -> None:
        self.text = txt 
        self.words = RE_WORD.findall(txt)
    
    def __repr__(self) -> str:
        return f'Sentence({reprlib.repr(self.text)})'
    
    def __iter__(self):
        return SentenceIterator(self.words)

# notice that we have to build an Iterator by hand
class SentenceIterator:
    def __init__(self, words) -> None:
        self.words = words
        self.index = 0
    
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1 
        return word
    
    def __iter__(self):
        return self 
        
