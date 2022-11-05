# A Case Study

# Scheme Syntax
# In Scheme there is no distinction between expressions and statements, like we have in Python.
# All expressions use prefix notation like (+ x 13) instead of x + 13.
# SCHEME CODE
# (define (mod m n)
# (- m (* n (quotient m n))))
# (define (gcd m n) (if(=n0)
#         m
#         (gcd n (mod m n))))
# (display (gcd 18 45))

# same written in Python
def mod(m, n):
    return m - (m // n * n)


def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, mod(m, n))


# print(gcd(18, 45))  # 9


# Lis.py: Top of the file

import math
import operator as op
from collections import ChainMap
from itertools import chain
from typing import Any, NoReturn, TypeAlias

Symbol: TypeAlias = str
Atom: TypeAlias = float | int | Symbol
Expression: TypeAlias = Atom | list


# the parser
def parse(program: str) -> Expression:
    "Read a scheme expression from a string"
    return read_from_tokens(tokenize(program))


def tokenize(s: str) -> list[str]:
    "Convert a string into a list of tokens."
    return s.replace("(", "( ").replace(")", " ) ").split()


def read_from_tokens(tokens: list[str]) -> Expression:
    "Read an expression from a sequence of tokens."
    pass
