from collections.abc import Iterable
from typing import overload

@overload
def sum_concat(__itr: Iterable[int]) -> int: ...
@overload
def sum_concat(__itr: Iterable[str]) -> str: ...
