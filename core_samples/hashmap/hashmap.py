#!/usr/bin/python

from typing import Any

class Hashmap:
    """ Simple hashmap implementation.
     Only accepts 'int' and 'str' as the key type. """

    def __init__(self) -> None:
        self._index: int = 0
        self._hash_index_map: dict = {}
        self._hashmap: list[list[tuple]] = []


    def _bucket_search(self, entries: list[tuple], key) ->Any:
        for entry in entries:
            if entry[0] == key:
                return entry[1]
        else:
            print(f'_bucket_search(): key->{key} not found')
            raise KeyError


    def _get_item(self, key) -> Any:
        key_hash = hash(key)

        if key_hash not in self._hash_index_map:
            print(f'_get_item(): key_hash->{key_hash} not found')
            raise KeyError
        
        index = self._hash_index_map[key_hash]
        entries = self._hashmap[index]

        return self._bucket_search(entries, key)


    def __getitem__(self, key: int) -> Any:
        """ Return the item of hashmap with key 'key'.
          Raises a 'KeyError' if 'key' is not in the map """

        return self._get_item(key)

    def __getitem__(self, key: str) -> Any:
        """ Return the item of hashmap with key 'key'.
          Raises a 'KeyError' if 'key' is not in the map """

        return self._get_item(key)

    def length(self) -> int:
        length = 0

        for entries in self._hashmap:
            length += len(entries)

        return length

    def _add_item(self, key, value: Any) -> None:
        key_hash = hash(key)

        if key_hash not in self._hash_index_map:
            self._hash_index_map[key_hash] = self._index
            index = self._index
            self._index += 1
        else:
            index = self._hash_index_map[key_hash]

        if index >= len(self._hashmap):
            entries: list[tuple] = []
            entries.append((key, value))

            self._hashmap.append(entries)
        else:
            self._hashmap[index].append((key, value))


    def add_item(self, key: int, value: Any) -> None:
        """ Adds the entry with key 'key' and value 'value'. """

        self._add_item(key, value)

    def add_item(self, key: str, value: Any) -> None:
        """ Adds the entry with key 'key' and value 'value'. """

        self._add_item(key, value)

    def remove_item(self, key: int) -> None:
        """ Removes the entry with key 'key'. """

    def remove_item(self, key: str) -> None:
        """ Removes the entry with key 'key'. """

if __name__ == "__main__":
    pass
