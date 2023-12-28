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

    _ROTATE_LEFT = 0
    _ROTATE_RIGHT = 1    

    def __init__(self, arr: list[Any], rebalance: bool) -> None:
        self._root : Node = Node()

        for value in arr:
            self.add_node(self._root, value, rebalance)

    def _simple_rotation(self, rotate_diraction, node: Node):
        if rotate_diraction == self._ROTATE_LEFT:
            temp_node = node._right

            node._right._parent = node._parent

            if node._right._parent == None:
                self._root = node._right

            node._parent = node._right
            node._right = node._right._left
            temp_node._left = node

            # adjust the heights
            node._rheight = node._parent._lheight
            node._parent._lheight = max(node._rheight, node._lheight) + 1
        else:
            temp_node = node._left

            node._left._parent = node._parent

            if node._left._parent == None:
                self._root = node._left

            node._parent = node._left
            node._left = node._left._right
            temp_node._right = node

            # adjust the heights
            node._lheight = node._parent._rheight
            node._parent._rheight = max(node._rheight, node._lheight) + 1


    def _rebalance_tree(self, node: Node) -> None:
        if abs(node.get_bf()) < 2:
            return
        
        # right heavy
        if node.get_bf() > 0:
            if node._right.get_bf() >= 0:
                # RR -> rotate left
                self._simple_rotation(self._ROTATE_LEFT, node)
            else:
                # RL -> rotate right then left

                # perform rotate right
                node._right._parent = node._right._left
                node._right._left = node._right._parent._right
                node._right._parent._parent = node
                node._right._parent._right = node._right
                node._right = node._right._parent
                
                # adjust the heights
                node._right._right._lheight = node._right._rheight
                node._right._rheight = max(node._right._right._lheight, node._right._right._rheight) + 1
                node._rheight = max(node._right._lheight, node._right._rheight) + 1

                # perform rotate left
                self._simple_rotation(self._ROTATE_LEFT, node)

        # left heavy
        if node.get_bf() < 0:
            if node._left.get_bf() <= 0:
                # LL -> rotate right
                self._simple_rotation(self._ROTATE_RIGHT, node=node)
            else:
                # LR -> rotate left then right

                # perform rotate left
                node._left._parent = node._left._right
                node._left._right = node._left._parent._left
                node._left._parent._parent = node
                node._left._parent._left = node._left
                node._left = node._left._parent
                
                # adjust the heights
                node._left._left._rheight = node._left._lheight
                node._left._lheight = max(node._left._left._lheight, node._left._left._rheight) + 1
                node._lheight = max(node._left._lheight, node._left._rheight) + 1

                # perform rotate right
                self._simple_rotation(self._ROTATE_RIGHT, node)

    def add_node(self, node: Node, value: Any, rebalance: bool) -> (int, int):
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

            lheight, rheight = self.add_node(node._left, value, rebalance)
            node._lheight = max(lheight, rheight) + 1
        else:
            if node._right == None:
                node._right = Node()
                node._right._parent = node

            lheight, rheight = self.add_node(node._right, value, rebalance)
            node._rheight = max(lheight, rheight) + 1

        if rebalance == True:
            self._rebalance_tree(node) 

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

    def remove_node(self, node: Node, value: Any, rebalance: bool) -> bool:
        """ Need to create balanced BST """

        if node == None:
            return False

        if node._value == value:
            self._remove_node(node)
            return True

        deleted: bool = False

        if value <= node._value:
            deleted = self.remove_node(node._left, value, rebalance=rebalance)
            if deleted == True:
                node._lheight -= 1

        else:
            deleted = self.remove_node(node._right, value, rebalance=rebalance)
            if deleted == True:
                node._rheight -= 1

        if rebalance == True:
            self._rebalance_tree(node)

        return deleted
        

if __name__ == "__main__":
    pass
