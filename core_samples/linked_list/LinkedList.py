#!/usr/bin/python

class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.prev : Node = None
        self.next : Node = None

class LinkedList:

    def __init__(self) -> None:
        self.head : Node = None
        self.lastNode : Node = None
        self.iter_next : Node = None
        self.iter_done : bool = False

    def add(self, val):
        node = Node(val)

        if self.head == None:
            self.head = node
            self.lastNode = self.head
        else:
            self.lastNode.next = node
            node.prev = self.lastNode
            self.lastNode = node

        self.lastNode = node
        self.head.prev = self.lastNode
        self.lastNode.next = self.head
    
    def remove(self, val):
        while self.head.data == val:
            node = self.head
            self.head = self.head.next
            self.head.prev = self.lastNode

        node = self.head.next
        while node is not self.head:
            if node.data == val:
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next

    def __iter__(self):
        self.iter_next = self.head
        self.iter_done = False
        return self
    
    def __next__(self):

        if self.iter_done == True:
            raise StopIteration

        next_node = self.iter_next
        self.iter_next = self.iter_next.next

        if self.iter_next is self.head:
            self.iter_done = True

        return next_node

if __name__ == '__main__':
    list_1 = LinkedList()
    list_1.add(val=99)
    print(list_1.head.data)


    for index, node in enumerate(list_1):
        print(f'iterator {index}: {node.data}')


    list_1.add(val=100)
    print(list_1.head.next.data)
    list_1.add(val=100)
    print(list_1.lastNode.data)
    list_1.add(val=101)
    print(list_1.lastNode.prev.data)

    for index, node in enumerate(list_1):
        print(f'iterator {index}: {node.data}')

    list_1.remove(100)
    print(list_1.head.data)
    print(list_1.head.next.data)
    print(list_1.lastNode.data)
    print(list_1.lastNode.next.data)
    list_1.remove(99)
    print(list_1.head.data)
    print(list_1.head.next.data)
    print(list_1.lastNode.data)
    print(list_1.lastNode.next.data)


