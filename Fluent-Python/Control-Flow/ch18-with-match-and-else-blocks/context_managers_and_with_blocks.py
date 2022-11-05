# The context manager interface consists of the __enter__ and __exit__ methods.
# At the top of the with, Python calls the __enter__ method of the context manager object.
# When the with block completes or terminates for any reason, Python calls __exit__ on the context manager object.

from __future__ import annotations

import reprlib
from typing import Any, Iterable, List, Optional


class Node(object):
    def __init__(
        self, value: Any, left: Optional[Node] = None, right: Optional[Node] = None
    ) -> None:
        self.val = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{type(self).__name__}({self.val!r})"


class BinarySearchTree(object):
    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        self.root: Optional[Node] = None

        if items:
            try:
                for item in items:
                    self.insert(item)
            except:
                raise TypeError("Items must be an Iterable")

    def _insert(self, value: Any, root: Optional[Node]) -> Node:
        if not root:
            return Node(value)

        if value >= root.val:
            root.right = self._insert(value, root.right)
        else:
            root.left = self._insert(value, root.left)

        return root

    def insert(self, value: Any) -> None:
        self.root = self._insert(value, self.root)

    def __str__(self) -> str:
        def search_nodes(
            root: Optional[Node], nodes: Optional[List[Any]] = None
        ) -> List[Any]:
            if nodes is None:
                nodes = []

            if root is None:
                return nodes

            nodes.append(root.val)

            search_nodes(root.left, nodes)
            search_nodes(root.right, nodes)

            return nodes

        return reprlib.repr(search_nodes(self.root))

    def __enter__(self) -> BinarySearchTree:
        return self

    def __exit__(self, *args) -> None:
        pass


# with BinarySearchTree([10, 5, 15]) as tree:
#     tree.insert(20)


import sys


class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return "JABBERWOCKY"

    def reverse_write(self, txt):
        self.original_write(txt[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write

        if exc_type is ZeroDivisionError:
            print("Please DO NOT divide by zero!")
            return True


# with LookingGlass() as what:
#     print("hello")
#     print(what)
#     raise ZeroDivisionError("BRUTH")

# print("normal", what)


# You can see that context manager can be use here as well
# manager = LookingGlass()

# manager.__enter__()

# print("hello world")
# manager.__exit__(*(None, None, None))
# print("hello world")

import sys
from contextlib import contextmanager
from typing import Any, Iterator


@contextmanager
def context() -> Iterator[Any]:
    print("setting up")
    yield "Dario"
    print("tearing setting up")


@contextmanager
def stdout_manager() -> Iterator[Any]:
    org = sys.stdout.write

    def indent_write(txt: str) -> int:
        return org(f"\t {txt}")

    sys.stdout.write = indent_write
    msg = ""
    try:
        yield "Jab Ber Wocky"
    except ZeroDivisionError:
        msg = "Please DO NOT divided by zero!"
    finally:
        sys.stdout.write = org
        if msg:
            print(msg)


# with stdout_manager() as val:
#     print("hello world!")
#     raise ZeroDivisionError("brah")
#     pass


# Using contextmanagers as decorators
@stdout_manager()
def verse():
    print("the time has come")


verse()
