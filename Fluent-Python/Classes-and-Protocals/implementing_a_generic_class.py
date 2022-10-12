from __future__ import annotations

import abc
import random
from collections.abc import Iterable
from typing import Generic, TypeVar


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)


T = TypeVar("T")


class LottoBlower(Tombola, Generic[T]):
    def __init__(self, items: Iterable[T]) -> None:
        self._balls = list[T](items)

    def load(self, items: Iterable[T]) -> None:
        self._balls.extend(items)

    def pick(self) -> T:
        try:
            position = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError("Pick from empty LottoBlower")
        return self._balls.pop(position)

    def loaded(self) -> bool:
        return bool(self._balls)

    def inspect(self) -> tuple[T, ...]:
        return tuple(self._balls)


# Basic Jargon for Generic Types
# Generic type
## A type declared with one or more type variables. Examples: LottoBlower[T], abc.Mapping[KT, VT]

# Formal type parameter
## The type variables that appear in a generic type declaration.
## Example: KT and VT in the previous example abc.Mapping[KT, VT]

# Parameterized type
## A type declared with actual type parameters.
## Examples: LottoBlower[int], abc.Mapping[str, float]

# Actual type parameter
## The actual types given as parameters when a
## parameterized type is declared. Example: the int in LottoBlower[int]
