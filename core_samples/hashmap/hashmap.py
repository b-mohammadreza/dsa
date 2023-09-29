#!/usr/bin/python

from typing import Any

class Hashmap:
    """ Simple hashmap implementation.
     Only accepts 'int' and 'str' as the key type. """

    _BUCKET_SEARCH_GET = 0
    _BUCKET_SEARCH_REMOVE = 1

    def __init__(self) -> None:
        self._index: int = 0
        self._hash_index_map: dict = {}
        self._hashmap: list[list[tuple]] = []

    def is_valid_hash(self, hash) -> bool:
        return hash in self._hash_index_map

    def _get_bucket(self, key) -> (int, list[tuple]):
        key_hash = hash(key)

        if key_hash not in self._hash_index_map:
            raise KeyError(f'_get_bucket(): key_hash->{key_hash} not found')
        
        index = self._hash_index_map[key_hash]
        if index >= len(self._hashmap):
            raise KeyError(f'_get_bucket(): index->{index} out of bound')

        return (index, self._hashmap[index])

    def _bucket_search(self, op, entries_info: (int,list[tuple]), key) ->Any:
        if op == self._BUCKET_SEARCH_GET:
            return self._bucket_search_get(entries_info, key)

        elif op == self._BUCKET_SEARCH_REMOVE:
            return self._bucket_search_remove(entries_info, key)

    def _bucket_search_get(self, entries_info: (int, list[tuple]), key) ->Any:
        for entry in entries_info[1]:
            if entry[0] == key:
                return entry[1]
        else:
            raise KeyError(f'_bucket_search_get(): key->{key} not found')

    def _bucket_search_remove(self, entries_info: (int, list[tuple]), key) ->Any:
        for index, entry in enumerate(entries_info[1]):
            if entry[0] == key:
                entries_info[1].pop(index)
                break
        else:
            raise KeyError(f'_bucket_search_remove(): key->{key} not found')

    def _get_item(self, key) -> Any:
        return self._bucket_search(op=self._BUCKET_SEARCH_GET, entries_info=self._get_bucket(key), key=key)

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

    def _remove_item(self, key) -> None:
        self._bucket_search(op=self._BUCKET_SEARCH_REMOVE, entries_info=self._get_bucket(key), key=key)

    def remove_item(self, key: int) -> None:
        """ Removes the entry with key 'key'. """

        self._remove_item(key)

    def remove_item(self, key: str) -> None:
        """ Removes the entry with key 'key'. """

        self._remove_item(key)

if __name__ == "__main__":
    pass
