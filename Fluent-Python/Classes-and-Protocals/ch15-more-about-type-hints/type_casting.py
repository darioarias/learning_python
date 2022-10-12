# The typing.cast() special function provides one way to handle type checking mal‐ functions or incorrect type hints in code we can’t fix.
from typing import List, cast


def cast(typ, val):
    """Cast a value to a type.
    This returns the value unchanged. To the type checker this signals that the return value has the designated type, but at runtime we intentionally don't check anything (we want this to be as fast as possible).
    """

    return val


def find_first_str(a: List[object]) -> str:
    index = next(
        i for i, x in enumerate(a) if isinstance(x, str)
    )  # We only get here if there's at least one string
    return cast(str, a[index])
