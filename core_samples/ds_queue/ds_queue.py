#!/usr/bin/python

from typing import Any

class DsQueue:
    def __init__(self) -> None:
        self._container: list[Any] = []

    def is_empty(self) -> bool:
        return len(self._container) == 0
    
    def length(self):
        return len(self._container)
    
    def enqueue(self, item: Any) -> int:
        """ Enqueues the item into Queue and
          returns the index in which the item enqueued """

        self._container.append(item)
        return len(self._container) - 1
    
    def peek(self) -> Any:
        if self.is_empty():
            return None

        return self._container[0]
    
    def dequeue(self) -> Any:
        if self.is_empty():
            return None

        item = self._container.pop(0)
        return item

if __name__ == "__main__":
    pass