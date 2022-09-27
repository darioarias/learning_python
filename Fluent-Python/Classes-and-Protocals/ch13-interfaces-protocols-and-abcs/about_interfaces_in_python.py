
# Python has four ways of defining and using interfaces since Python 3.8

# Duck Typing
## Python’s default approach to typing from the beginning. 
## We’ve been studying duck typing since Chapter 1.

# Goose typing
## The approach supported by abstract base classes (ABCs) since Python 2.6, 
## which relies on runtime checks of objects against ABCs. 
## Goose typing is a major subject in this chapter.

# Static typing
## The traditional approach of statically-typed languages like C and Java; 
## supported since Python 3.5 by the typing module, and enforced by external 
## type checkers compliant with PEP 484—Type Hints. This is not the theme of this chapter. 
## Most of Chapter 8 and the upcoming Chapter 15 are about static typing.

# Static duck typing
## An approach made popular by the Go language; supported by subclasses of typ ing. 
## Protocol—new in Python 3.8—also enforced by external type checkers. 
## We first saw this in “Static Protocols” on page 286 (Chapter 8).