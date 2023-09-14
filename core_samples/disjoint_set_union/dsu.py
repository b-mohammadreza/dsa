#!/usr/bin/python

from typing import Any

class DisjointSetUnion:
    """ Implements Disjoint-set Union data structure """

    def __init__(self, init_list: list) -> None:                        # O(n)
        """ There must not be any duplicate value in init_list """

        self._collection: list[dict] = []
        self._ranks: dict = {}
        for node in init_list:
            self.make_set(node)

    def make_set(self, node) -> None:                                   # O(1)
        """ Makes a new set using 'node' """

        d_set: dict = {}
        d_set[node] = node
        self._collection.append(d_set)
        self._ranks[node] = 0

    def find(self, node) -> (bool, int, Any):                           # O(n)
        """ Finds 'node' in the collections and returns
        the corresponding set representative (set ID).
        (May apply path compression optimization) """

        set_id: Any = None
        init_node = node

        for index, d_set in enumerate(self._collection):                # If the inner while loop
                                                                        # takes O(n), it means all the
                                                                        # entries already merged.\
                                                                        # outer_loop O * inner_loop O = O(n)
            if node in d_set:
                parent = d_set[node]

                while parent != node:                                   # Max: O(n)
                    node = parent
                    parent = d_set[node]

                set_id = parent
                d_set[init_node] = set_id   # Performs path compression
                break
        else:
            print(f"'{node}' not found in the collection!")
            return (False, -1, None)
        

        return (True, index, set_id)

    def union(self, node_1, node_2) -> bool:                            # O(n)
        """ Finds both 'node_1' and 'node_2' in the collection,
        if they belong to different sets, merges the corresponding sets
        (May uses self._ranks heuristic). In practice both 'node_1'
        and 'node_2' should be set IDs """

        result, index_1, set_id_1 = self.find(node_1)                   # O(n)
        if result == False:
            return False

        result, index_2, set_id_2 = self.find(node_2)                   # O(n)
        if result == False:
            return False
        
        if set_id_1 == set_id_2:
            return True
        
        rank_1 = self._ranks.get(set_id_1)
        rank_2 = self._ranks.get(set_id_2)

        # The tree with lower rank will be merged into the tree with higher rank
        d_set_1 = self._collection[index_1]
        d_set_2 = self._collection[index_2]

        if rank_1 < rank_2:
            d_set_1[set_id_1] = set_id_2
            d_set_2 |= d_set_1                                          # Max: O(n/2)
            self._collection[index_2] = d_set_2
            self._collection.pop(index_1)                               # Max: O(n) - due to shift elements
            self._ranks.pop(set_id_1)

        else:
            d_set_2[set_id_2] = set_id_1
            d_set_1 |= d_set_2                                          # Max: O(n/2)
            self._collection[index_1] = d_set_1
            self._collection.pop(index_2)                               # Max: O(n) - due to shift elements
            self._ranks.pop(set_id_2)

            if rank_1 == rank_2:
                self._ranks[set_id_1] = rank_1 + 1

        return True
    
if __name__ == '__main__':
    pass