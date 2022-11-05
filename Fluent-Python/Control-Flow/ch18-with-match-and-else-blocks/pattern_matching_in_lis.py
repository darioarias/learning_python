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
    if len(tokens) == 0:
        raise SyntaxError("unexpected EOF while reading")
    token = tokens.pop(0)
    if "(" == token:
        exp = []
        while tokens[0] != ")":
            exp.append(read_from_tokens(tokens))
        tokens.pop(0)  # discard ')'
        return exp
    elif ")" == token:
        raise SyntaxError("unexpected )")
    else:
        return parse_atom(token)


def parse_atom(token: str) -> Atom:
    "Numbers become numbers; every other token is a symbol."
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)


# The Environmnet

# The Environment class
class Environmnet(ChainMap[Symbol, Any]):
    "A ChainMap that allows changing an item in-place"

    def change(self, key: Symbol, value: Any) -> None:
        "Find where key is defined and change the value there."
        for map in self.maps:
            if key in map:
                map[key] = value
                return
        raise KeyError(key)


# building and returning global environment
def standard_env() -> Environmnet:
    "An environment with some scheme standard procedures."
    env = Environmnet()
    env.update(vars(math))  # sin, cons, sqrt, pi, ...
    env.update(
        {
            "+": op.add,
            "-": op.sub,
            "*": op.mul,
            "/": op.truediv,
            "quotient": op.floordiv,
            ">": op.gt,
            "<": op.lt,
            ">=": op.ge,
            "<=": op.le,
            "=": op.eq,
            "abs": abs,
            "append": lambda *args: list(chain(*args)),
            "apply": lambda proc, args: proc(*args),
            "begin": lambda *x: x[-1],
            "car": lambda x: x[0],
            "cdr": lambda x: x[1:],
            "cons": lambda x, y: [x] + y,
            "display": lambda x: print(lispstr(x)),
            "eq?": op.is_,
            "equal?": op.eq,
            "filter": lambda *args: list(filter(*args)),
            "length": len,
            "list": lambda *x: list(x),
            "list?": lambda x: isinstance(x, list),
            "map": lambda *args: list(map(*args)),
            "max": max,
            "min": min,
            "not": op.not_,
            "null?": lambda x: x == [],
            "number?": lambda x: isinstance(x, (int, float)),
            "procedure?": callable,
            "round": round,
            "symbol?": lambda x: isinstance(x, Symbol),
        }
    )
    return env
