#!/usr/bin/python

from typing import Any

class Vector:
    def __init__(self) -> None:
        self._container: list[Any] = []

    def is_empty(self) -> bool:
        return len(self._container) == 0
    
    def size(self):
        return len(self._container)
    
    def push_back(self, item: Any) -> int:
        """ push_back the item into Vector and
          returns the index in which the item inserted """

        self._container.append(item)
        return len(self._container) - 1
    
    def insert(self, index: int, item: Any) -> None:
        """ insert the item into Vector at the specified index """

        self._container.insert(index, item)
    
    def back(self) -> Any:
        if self.is_empty():
            return None

        return self._container[-1]
    
    def front(self) -> Any:
        if self.is_empty():
            return None

        return self._container[0]
    
    def at(self, index: int) -> Any:
        if self.is_empty():
            return None

        return self._container[index]
    
    def pop_back(self) -> Any:
        if self.is_empty():
            return None

        item = self._container.pop()
        return item
    
    def erase(self, index: int) -> Any:
        if self.is_empty():
            return None

        item = self._container.pop(index)
        return item

if __name__ == "__main__":
    pass
