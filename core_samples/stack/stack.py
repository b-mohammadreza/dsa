#!/usr/bin/python

from typing import Any

class Stack:
    def __init__(self) -> None:
        self._container: list[Any] = []

    def is_empty(self) -> bool:
        return len(self._container) == 0
    
    def push(self, item: Any) -> int:
        """ Pushes the item into stack and
          returns the index in which the item pushed """

        self._container.append(item)
        return len(self._container) - 1
    
    def peek(self) -> Any:
        if self.is_empty():
            return None

        return self._container[-1]
    
    def pop(self) -> Any:
        if self.is_empty():
            return None

        item = self._container.pop()
        return item

if __name__ == "__main__":
    pass