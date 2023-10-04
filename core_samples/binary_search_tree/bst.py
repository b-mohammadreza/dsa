#!/usr/bin/python

from typing import Any, Self

class Node:
    def __init__(self) -> None:
        self._value: Any = None
        self._left: Self = None
        self._right: Self = None

class BST:
    def __init__(self, arr: list[Any]) -> None:
        self._root : Node = None

        for value in arr:
            self.add_node(value)

    def add_node(self, value: Any):
        """ Need to create a balanced BST """
        

    def remove_node(self, value: Any):
        pass

if __name__ == "__main__":
    pass