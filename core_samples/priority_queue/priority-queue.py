#!/usr/bin/python

class PriorityQueue:
    """ for the sake of simplicity the values which can be stored in this
     data structure are 'int' values. it implements min binary heap """

    def __init__(self, ) -> None:
        self._min_heap: list[int] = None
        self._is_min_heap: bool = False

    def heapify(self, arr: list[int]) -> list[int]:
        if len(self._min_heap) > 0:
            print('PriorityQueue::heapify(): _min_heap not empty...')
            return

        for priority in arr:
            self.enqueue(priority=priority)
        
        self._is_min_heap = True

    def enqueue(self, priority: int):
        """ to add a new element to the min heap data structue """
        self._min_heap.append(priority)
        new_index = len(self._min_heap) - 1

        while True:
            parent_index = (new_index - 1) / 2

            if self._min_heap[new_index] < self._min_heap[parent_index]:
                # following instruction swaps the contents of the items!
                self._min_heap[parent_index], self._min_heap[new_index] = self._min_heap[new_index], self._min_heap[parent_index]

                new_index = parent_index
            else:
                break

    def dequeue(self) -> int:
        """ to remove the root element from the min heap data structure """
        pass

    def peek(self) -> int:
        pass

if __name__ == '__main__':
    pass

