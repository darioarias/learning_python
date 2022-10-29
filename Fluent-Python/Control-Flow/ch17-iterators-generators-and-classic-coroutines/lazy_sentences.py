

# building a Sentence class lazily to save memory 
import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text) -> None:
        self.text = text 
    
    def __repr__(self) -> str:
        return f"Sentence({reprlib.repr(self.text)})"
    
    def __iter__(self):
        # for match in RE_WORD.finditer(self.text):
        #     yield match.group()
        return (match.group() for match in RE_WORD.finditer(self.text))
