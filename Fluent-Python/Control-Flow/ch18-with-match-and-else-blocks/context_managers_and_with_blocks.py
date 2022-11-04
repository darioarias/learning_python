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


with BinarySearchTree([10, 5, 15]) as tree:
    tree.insert(20)
