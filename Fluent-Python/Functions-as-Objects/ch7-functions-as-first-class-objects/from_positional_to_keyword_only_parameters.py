# checking how versitile python parameters can be

# tag generates HTML elements; a keyword-only argument class_ 
# is used to pass “class” attributes as a workaround because class is a keyword in Python
def tag(name, *content, class_=None, **attrs):
  """Generate one of more HTML tags"""
  if class_ is not None: 
    attrs['class'] = class_
  
  attr_pairs = (f' {attr}="{value}"' for attr, value in sorted(attrs.items()))
  attr_str = ''.join(attr_pairs)

  if content:
    elements = (f'<{name}{attr_str}>{c}</{name}>' for c in content)
    return '\n'.join(elements)
  
  else:
    return f'<{name}{attr_str} />'


# print(tag('br'))
# print(tag('p', 'hello', 'world'))
# print(tag('p', 'hello', 'world', id=23, target='id-runner'))
# print(tag('p', 'hello', 'world', class_="sidebar"))
# print(tag(content="testing", name="img"))
# some_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'class': 'framed'}
# print(tag(**some_tag))

# if we are only interested in supporting named arguments we can 
# declare the following signature

def f(a, *, b):
  return a, b

# f(1, b=1)  # (1, 2)
# f(1, 2)  # TypeError: f() takes 1 positional argument but 2 were given

# Positional-Only Parameters
# To define a function requiring positional-only parameters, use / in the parameter list.
def divmod(a, b, /):
  return (a // b, a % b)