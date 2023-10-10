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
        self._root : Node = Node()

        for value in arr:
            self.add_node(self._root, value)

    def add_node(self, node: Node, value: Any) -> (int, int):
        """ Need to create a balanced BST.
        Returns current node left and right subtrees heights. """

        if node == None:
            raise ValueError("Invalid node. The node cannot be None when passing to add_node()!")

        if node._value == None:
            node._value = value
            return (0, 0)
        
        lheight: int = 0
        rheight: int = 0

        if value <= node._value:
            if node._left == None:
                node._left = Node()

            lheight, rheight = self.add_node(node._left, value)
            node._lheight = max(lheight, rheight) + 1
        else:
            if node._right == None:
                node._right = Node()

            lheight, rheight = self.add_node(node._right, value)
            node._rheight = max(lheight, rheight) + 1

        return (node._lheight, node._rheight)
        

    def remove_node(self, value: Any):
        pass

if __name__ == "__main__":
    pass