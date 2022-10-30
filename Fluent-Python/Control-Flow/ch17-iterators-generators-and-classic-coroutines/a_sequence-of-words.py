# sentence.py: a Sentence as a sequence of words

import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:
    def __init__(self, text) -> None:
        self.text = text 
        self.words = RE_WORD.findall(text)
    
    def __getitem__(self, index) -> str:
        return self.words[index]
    
    def __len__(self) -> int:
        return len(self.words)
    
    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)

s = Sentence('"The time has come," the Walrus said,')
print(s)

# notice that this sentence is iterable. But the question remainds, why?
