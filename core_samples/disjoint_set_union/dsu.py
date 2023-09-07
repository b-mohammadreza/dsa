#!/usr/bin/python

from typing import Any

class DisjointSetUnion:
    """ Implements Disjoint-set Union data structure """

    def __init__(self, init_list: list) -> None:
        self._collection: list[dict] = []
        self._ranks: dict = {}

    def make_set(self, node) -> None:
        """ Makes a new set using 'node' """

        d_set: dict = {}
        d_set[node] = node
        self._collection.append(d_set)
        self._ranks[node] = 0

    def find(self, node) -> (bool, Any):
        """ Finds 'node' in the collections and returns
        the corresponding set representative (set ID).
        (May apply path compression optimization) """

        set_id: Any = None

        for d_set in self._collection:
            if node in d_set:
                parent = d_set[node]

                while parent != node:
                    node = parent
                    parent = d_set[node]

                set_id = parent
                break
        else:
            print(f"'{node}' not found in the collection!")
            return (False, None)
        
        return (True, set_id)

    def union(self, node_1, node_2) -> bool:
        """ Finds both 'node_1' and 'node_2' in the collection,
        if they belong to different sets, merges the corresponding sets
        (May uses self._ranks heuristic) """

        result, set_id_1 = self.find(node_1)
        if result == False:
            return False

        result, set_id_2 = self.find(node_2)
        if result == False:
            return False
        
        rank_1 = self._ranks.get(set_id_1)
        rank_2 = self._ranks.get(set_id_2)

        # TODO: read more about rank to have a solid understanding of it
    
if __name__ == '__main__':
    pass