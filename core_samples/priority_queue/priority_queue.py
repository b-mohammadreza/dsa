#!/usr/bin/python

def is_min_heap(arr: list[int]) -> bool:
    pass

class PriorityQueue:
    """ for the sake of simplicity the values which can be stored in this
     data structure are 'int' values. it implements min binary heap """

    def __init__(self) -> None:
        self._min_heap: list[int] = []
        self._is_min_heap: bool = False

    def heapify(self, arr: list[int]) -> list[int]:
        if len(self._min_heap) > 0:
            print('PriorityQueue::heapify(): _min_heap already initialized...')
            return

        for priority in arr:
            self.enqueue(priority=priority)
        
        self._is_min_heap = True

        return self._min_heap

    def is_min_heap(self, arr: list[int] = None) -> bool:
        if arr == None:
            if len(self._min_heap) < 1:
                return True
            else:
                arr = self._min_heap

        arr_len = len(arr)
        print(f'is_min_heap(): arr len->{arr_len}')

        for index, elem in enumerate(arr):
            left_child_index = index * 2 + 1
            right_child_index = left_child_index + 1

            if left_child_index >= arr_len:
                continue
    
            if elem > arr[left_child_index]:
                return False
            
            if right_child_index >= arr_len:
                continue
    
            if elem > arr[right_child_index]:
                return False

        return True

    def enqueue(self, priority: int) -> list[int]:
        """ to add a new element to the min heap data structue """
        self._min_heap.append(priority)

        if len(self._min_heap) < 2:
            print(f'enqueue(): len < 2, self._min_heap -> {self._min_heap}')
            return self._min_heap

        new_index = len(self._min_heap) - 1

        while True:
            parent_index = (new_index - 1) // 2
            print(f'enqueue(): new_index->{new_index}, parent_index->{parent_index}, self._min_heap->{self._min_heap}')

            if self._min_heap[new_index] < self._min_heap[parent_index]:
                # following instruction swaps the contents of the items!
                self._min_heap[parent_index], self._min_heap[new_index] = self._min_heap[new_index], self._min_heap[parent_index]

                print(f'enqueue() ------- swapped: new_index->{new_index}, parent_index->{parent_index}, self._min_heap->{self._min_heap}')

                if parent_index == 0:
                    break

                new_index = parent_index
            else:
                break

        print(f'>>>>>>>>>>enqueue() end. self._min_heap->{self._min_heap}')
        return self._min_heap

    def dequeue(self) -> (list[int], int):
        """ to remove the root element from the min heap data structure """
        arr_len = len(self._min_heap)
        if arr_len < 1:
            return ([], None)

        root = self._min_heap.pop(0)
        arr_len = len(self._min_heap)

        if arr_len < 1:
            return ([], root)

        leaf = self._min_heap.pop(-1)

        self._min_heap.insert(0, leaf)

        # we need to update the array len at this point
        arr_len = len(self._min_heap)

        parent_index = 0
        while True:
            child_index = (parent_index * 2) + 1

            if child_index >= arr_len:
                break

            if child_index + 1 < arr_len:
                if self._min_heap[child_index + 1] < self._min_heap[child_index]:
                    child_index = child_index + 1 

            if self._min_heap[child_index] < self._min_heap[parent_index]:
                # following instruction swaps the contents of the items!
                self._min_heap[parent_index], self._min_heap[child_index] = self._min_heap[child_index], self._min_heap[parent_index]

                parent_index = child_index
            else:
                break

        print(f'--------dequeue() end. self._min_heap->{self._min_heap}, root->{root}')
        return (self._min_heap, root)

    def peek(self) -> int:
        return self._min_heap[0]

if __name__ == '__main__':
    pass

