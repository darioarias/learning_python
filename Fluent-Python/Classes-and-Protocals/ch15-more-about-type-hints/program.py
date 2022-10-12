import functools
import operator
from collections.abc import Iterable
from typing import TypeVar, Union, overload


# leading under scores make it __itr positional only and user cannot do __itr =
def sum_concat(__itr):
    """Given an interable of ints, this function will sum them together and return the sum. When an iterable of str is given, the function concats them together"""
    _result = 0 if isinstance(__itr[0], int) else ""
    for item in __itr:
        _result += item
    return _result


# having type hints and implementation on the same file

T = TypeVar("T")
S = TypeVar("S")


@overload
def sum(it: Iterable[T]) -> Union[T, int]:
    ...


@overload
def sum(it: Iterable[T], /, start: S) -> Union[T, S]:
    ...


def sum(it, /, start=0):
    return functools.reduce(operator.add, it, start)
