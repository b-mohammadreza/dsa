#!/usr/bin/python

from typing import Any, Self

class Node:
    def __init__(self) -> None:
        self._value: Any = None
        self._lheight: int = 0
        self._rheight: int = 0
        self._left: Node = None
        self._right: Node = None

    def get_bf(self) -> int:
        return self._rheight - self._lheight

class BST:
    def __init__(self, arr: list[Any]) -> None:
        self._root : Node = None

        for value in arr:
            self.add_node(self._root, value)

    def add_node(self, root: Node, value: Any) -> (int, int):
        """ Need to create a balanced BST """

        if root == None:
            root = Node()
            root._value = value
            return (0, 0)
        
        lheight: int = 0
        rheight: int = 0

        if value <= root._value:
            lheight, rheight = self.add_node(root._left, value)
            root._lheight += max(lheight, rheight) + 1
        else:
            lheight, rheight = self.add_node(root._right, value)
            root._rheight += max(lheight, rheight) + 1

        return (root._lheight, root._rheight)
        

    def remove_node(self, value: Any):
        pass

if __name__ == "__main__":
    pass