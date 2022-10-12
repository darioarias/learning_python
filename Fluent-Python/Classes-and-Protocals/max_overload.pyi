# annotating max
# from collections.abc import Callable, Iterable
from typing import Any, Callable, Iterable, Protocol, TypeVar, Union, overload

class SupportsLessThan(Protocol):
    def __lt__(self, other: Any) -> bool: ...

T = TypeVar("T")
LT = TypeVar("LT", bound=SupportsLessThan)
DT = TypeVar("DT")

MISSING = object()
EMPTY_MSG = "max() arg is an empty sequence"

@overload
def max(__arg1: LT, __arg2: LT, *args: LT, key: None = ...) -> LT: ...
@overload
def max(__arg1: T, __arg2: T, *args: T, key: Callable[[T], LT]) -> T: ...
@overload
def max(__iterable: Iterable[LT], *, key: None = ...) -> LT: ...
@overload
def max(__iterable: Iterable[T], *, key: Callable[[T], LT]) -> T: ...
@overload
def max(__iterable: Iterable[LT], *, key: None = ..., default: DT) -> Union[LT, DT]: ...
@overload
def max(
    __iterable: Iterable[T], *, key: Callable[[T], LT], default: DT
) -> Union[T, DT]: ...
