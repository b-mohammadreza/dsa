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

    def _rebalance_tree(self, node: Node) -> None:
        if abs(node.get_bf()) < 2:
            return
        
        # right heavy
        if node.get_bf() < 0:
            if node._right.get_bf() <= 0:
                # RR -> rotate left
                temp_node = node._right
                temp_node._parent = node._parent

                if node._right._parent == None:
                    self._root = node._right

                node._parent = node._right
                node._right._left = node
                node._right = temp_node._left

                # adjust the heights
                node._rheight = max(node._right._rheight, node._right._lheight)
                node._parent._lheight = max(node._rheight, node._lheight)
            else:
                # RL -> rotate right then left
                pass

        # left heavy
        if node.get_bf() > 0:
            if node._left.get_bf() >= 0:
                # LL -> rotate right
                pass
            else:
                # LR -> rotate left then right
                pass

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

        self._rebalance_tree() 

        return (node._lheight, node._rheight)
    
    def _remove_node_leaf(self, node: Node) -> None:
        if node is self._root:
            node._value = None
        elif node._parent._left is node:
            node._parent._left = None
        elif node._parent._right is node:
            node._parent._right = None
        
    def _remove_node_with_one_child(self, node: Node) -> None:
        child: Node = node._left
        if child == None:
            child = node._right

        if node is self._root:
            self._root = child
        elif node._parent._left is node:
            node._parent._left = child
        elif node._parent._right is node:
            node._parent._right = child

    def _get_inorder_successor_node(self, node: Node, nodes_to_update: list[Node]) -> (Node,  list[Node]):
        if node._left == None:
            return (node, nodes_to_update)

        nodes_to_update.append(node)
        return self._get_inorder_successor_node(node._left, nodes_to_update)

    def _remove_node_with_children(self, node: Node) -> None:
        (node_to_rm, nodes_to_update) = self._get_inorder_successor_node(node._right, [])
        node._value = node_to_rm._value

        self._remove_node(node_to_rm)

        node._rheight -= 1

        node_item: Node
        for node_item in nodes_to_update:
            node_item._lheight -= 1

    def _remove_node(self, node: Node) -> None:
        if node._right == None and node._left == None:
            self._remove_node_leaf(node)
            return

        if node._right == None or node._left == None:
            self._remove_node_with_one_child(node)
            return
            
        self._remove_node_with_children(node)

    def remove_node(self, node: Node, value: Any) -> bool:
        """ Need to create balanced BST """

        if node == None:
            return False

        if node._value == value:
            self._remove_node(node)
            return True

        deleted: bool = False

        if value <= node._value:
            deleted = self.remove_node(node._left, value)
            if deleted == True:
                node._lheight -= 1

        else:
            deleted = self.remove_node(node._right, value)
            if deleted == True:
                node._rheight -= 1

        return deleted
        

if __name__ == "__main__":
    pass
