#!/usr/bin/python

from typing import Any, Self

class Node:
    def __init__(self) -> None:
        self._value: Any = None
        self._lheight: int = 0
        self._rheight: int = 0
        self._parent: Node = None
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
                node._left._parent = node

            lheight, rheight = self.add_node(node._left, value)
            node._lheight = max(lheight, rheight) + 1
        else:
            if node._right == None:
                node._right = Node()
                node._right._parent = node

            lheight, rheight = self.add_node(node._right, value)
            node._rheight = max(lheight, rheight) + 1

        return (node._lheight, node._rheight)
    
    def _remove_links(self, node: Node):
        if node._right != None:
            pass

    def remove_node(self, node: Node, value: Any) -> bool:
        if node == None:
            return False

        if node._value == value:
            self._remove_links(node)
            return True

        deleted: bool = False

        if value <= node._value:
            deleted = self.remove_node(node._left, value)

        else:
            deleted = self.remove_node(node._right, value)

        return deleted
        

if __name__ == "__main__":
    pass
