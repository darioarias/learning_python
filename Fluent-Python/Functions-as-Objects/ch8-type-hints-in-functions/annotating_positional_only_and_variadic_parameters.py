


# recall
def tag(name, /, *content, class_=None, **attrs):
  pass 

# lets annotate it
from typing import Optional

def tag(
  name: str,
  /,
  *content: str,
  class_:Optional[str] = None, 
  **attrs: str,
) -> str:
  pass
